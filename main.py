#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Avtomatik Musiqi Yükləmə Sistemi
Yandex Music və YouTube-dan mahnıları yükləyib Apple Music üçün hazırlayır
"""

import os
import sys
import json
import logging
from pathlib import Path
from typing import Set, List, Dict, Optional
from dotenv import load_dotenv
import yt_dlp
from mutagen.mp4 import MP4, MP4Cover
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB
import requests
from io import BytesIO
from PIL import Image

# Yandex Music API
try:
    from yandex_music import Client
except ImportError:
    print("XƏBƏRDARLIQ: yandex-music kitabxanası tapılmadı")
    Client = None

# Logging konfiqurasiyası
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('music_downloader.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# .env faylını yüklə
load_dotenv()

# Konfiqurasiya
YANDEX_TOKEN = os.getenv('YANDEX_TOKEN')
YANDEX_PLAYLIST_ID = os.getenv('YANDEX_PLAYLIST_ID')
YOUTUBE_PLAYLIST_ID = os.getenv('YOUTUBE_PLAYLIST_ID')
DOWNLOAD_DIR = Path('downloads')
HISTORY_FILE = Path('history.txt')

# Qovluğu yarat
DOWNLOAD_DIR.mkdir(exist_ok=True)


class MusicDownloader:
    """Musiqi yükləmə və emal sinfi"""
    
    def __init__(self):
        self.history = self._load_history()
        self.yandex_client = None
        
        # Yandex Music müştərisini başlat
        if YANDEX_TOKEN and Client:
            try:
                self.yandex_client = Client(YANDEX_TOKEN).init()
                logger.info("✓ Yandex Music müştərisi uğurla başladıldı")
            except Exception as e:
                logger.warning(f"⚠ Yandex Music token işləmir - skip ediləcək: {e}")
                logger.info("💡 Yalnız YouTube istifadə ediləcək")
    
    def _load_history(self) -> Set[str]:
        """Yüklənmiş mahnıların tarixçəsini yüklə"""
        if HISTORY_FILE.exists():
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return set(line.strip() for line in f if line.strip())
        return set()
    
    def _save_to_history(self, track_id: str):
        """Mahnı ID-sini tarixçəyə əlavə et"""
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{track_id}\n")
        self.history.add(track_id)
    
    def _optimize_cover_for_apple(self, image_data: bytes) -> bytes:
        """
        Qapaq şəklini Apple Music/iTunes üçün optimallaşdır
        1000x1000 JPEG formatına çevir (Baseline JPEG)
        """
        try:
            img = Image.open(BytesIO(image_data))
            
            # RGB-yə çevir (RGBA və ya digər formatlardan)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # 1000x1000-ə ölçüləndir (aspect ratio saxlanılır)
            img.thumbnail((1000, 1000), Image.Resampling.LANCZOS)
            
            # Baseline JPEG olaraq saxla
            output = BytesIO()
            img.save(output, format='JPEG', quality=95, optimize=True, progressive=False)
            return output.getvalue()
        except Exception as e:
            logger.error(f"Şəkil optimallaşdırma xətası: {e}")
            return image_data
    
    def _embed_cover_to_m4a(self, file_path: Path, cover_data: bytes):
        """
        M4A faylına qapaq şəklini Apple Music formatında embed et
        """
        try:
            audio = MP4(str(file_path))
            
            # Şəkli optimallaşdır
            optimized_cover = self._optimize_cover_for_apple(cover_data)
            
            # Apple-ın Baseline JPEG formatında əlavə et
            audio['covr'] = [MP4Cover(optimized_cover, imageformat=MP4Cover.FORMAT_JPEG)]
            audio.save()
            logger.info(f"✓ Qapaq şəkli embed edildi: {file_path.name}")
        except Exception as e:
            logger.error(f"✗ Qapaq embed xətası ({file_path.name}): {e}")
    
    def download_from_yandex(self) -> int:
        """
        Yandex Music pleylistindən yeni mahnıları yüklə
        Format: Xam M4A (AAC), 1000x1000 qapaq şəkli ilə
        """
        if not self.yandex_client:
            logger.warning("Yandex Music müştərisi mövcud deyil")
            return 0
        
        if not YANDEX_PLAYLIST_ID:
            logger.warning("YANDEX_PLAYLIST_ID təyin edilməyib")
            return 0
        
        downloaded_count = 0
        
        try:
            # Pleylisti əldə et
            playlist = self.yandex_client.users_playlists(YANDEX_PLAYLIST_ID)
            logger.info(f"📋 Yandex pleylist: {playlist.title} ({len(playlist.tracks)} mahnı)")
            
            for track_short in playlist.tracks:
                track = track_short.track
                track_id = f"yandex_{track.id}"
                
                # Artıq yüklənibsə, keç
                if track_id in self.history:
                    logger.debug(f"⊘ Artıq mövcuddur: {track.title}")
                    continue
                
                try:
                    # Mahnı məlumatları
                    artists = ', '.join([artist.name for artist in track.artists])
                    title = track.title
                    album = track.albums[0].title if track.albums else 'Unknown Album'
                    
                    # Təmiz fayl adı
                    safe_filename = f"{artists} - {title}".replace('/', '-').replace('\\', '-')
                    safe_filename = "".join(c for c in safe_filename if c.isalnum() or c in (' ', '-', '_')).strip()
                    output_file = DOWNLOAD_DIR / f"{safe_filename}.m4a"
                    
                    logger.info(f"⬇ Yüklənir: {artists} - {title}")
                    
                    # Ən yüksək keyfiyyətdə yüklə (xam M4A/AAC)
                    track.download(str(output_file), codec='aac', bitrate_in_kbps=320)
                    
                    # Qapaq şəklini əldə et (1000x1000)
                    if track.cover_uri:
                        cover_url = f"https://{track.cover_uri.replace('%%', '1000x1000')}"
                        response = requests.get(cover_url, timeout=10)
                        if response.status_code == 200:
                            # Qapaq şəklini embed et
                            self._embed_cover_to_m4a(output_file, response.content)
                    
                    # Tarixçəyə əlavə et
                    self._save_to_history(track_id)
                    downloaded_count += 1
                    logger.info(f"✓ Uğurla yükləndi: {output_file.name}")
                    
                except Exception as e:
                    logger.error(f"✗ Xəta ({track.title}): {e}")
                    continue
        
        except Exception as e:
            logger.error(f"✗ Yandex pleylist xətası: {e}")
        
        return downloaded_count
    
    def download_from_youtube(self) -> int:
        """
        YouTube pleylistindən yeni mahnıları yüklə
        Format: Xam M4A (AAC), QAPaq şəkli OLMADAN
        """
        if not YOUTUBE_PLAYLIST_ID:
            logger.warning("YOUTUBE_PLAYLIST_ID təyin edilməyib")
            return 0
        
        downloaded_count = 0
        
        # yt-dlp konfiqurasiyası
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio',  # Xam M4A/AAC formatı
            'outtmpl': str(DOWNLOAD_DIR / '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
            'extract_flat': 'in_playlist',  # Əvvəlcə siyahını götür
            'ignoreerrors': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }],
            'writethumbnail': False,  # Qapaq şəkli YÜKLƏNMƏZ
            'embedthumbnail': False,  # Qapaq şəkli EMBED OLUNMAZ
        }
        
        try:
            playlist_url = f"https://www.youtube.com/playlist?list={YOUTUBE_PLAYLIST_ID}"
            
            with yt_dlp.YoutubeDL({'extract_flat': 'in_playlist', 'quiet': True}) as ydl:
                playlist_info = ydl.extract_info(playlist_url, download=False)
                
                if not playlist_info or 'entries' not in playlist_info:
                    logger.error("YouTube pleylist məlumatı əldə edilə bilmədi")
                    return 0
                
                total_tracks = len([e for e in playlist_info['entries'] if e])
                logger.info(f"📋 YouTube pleylist: {playlist_info.get('title', 'Unknown')} ({total_tracks} video)")
            
            # Hər bir mahnını yüklə
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                for entry in playlist_info['entries']:
                    if not entry:
                        continue
                    
                    video_id = entry.get('id')
                    track_id = f"youtube_{video_id}"
                    
                    # Artıq yüklənibsə, keç
                    if track_id in self.history:
                        logger.debug(f"⊘ Artıq mövcuddur: {entry.get('title', 'Unknown')}")
                        continue
                    
                    try:
                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                        logger.info(f"⬇ Yüklənir: {entry.get('title', 'Unknown')}")
                        
                        ydl.download([video_url])
                        
                        # Tarixçəyə əlavə et
                        self._save_to_history(track_id)
                        downloaded_count += 1
                        logger.info(f"✓ Uğurla yükləndi")
                        
                    except Exception as e:
                        logger.error(f"✗ Xəta ({entry.get('title', 'Unknown')}): {e}")
                        continue
        
        except Exception as e:
            logger.error(f"✗ YouTube pleylist xətası: {e}")
        
        return downloaded_count
    
    def run(self):
        """Əsas icra funksiyası"""
        logger.info("=" * 60)
        logger.info("🎵 MUSİQİ YÜKLƏMƏ SİSTEMİ BAŞLADI")
        logger.info("=" * 60)
        
        # Yandex Music-dən yüklə
        logger.info("\n📥 YANDEX MUSIC-DƏN YÜKLƏMƏ...")
        yandex_count = self.download_from_yandex()
        logger.info(f"✓ Yandex-dən {yandex_count} mahnı yükləndi\n")
        
        # YouTube-dan yüklə
        logger.info("📥 YOUTUBE-DAN YÜKLƏMƏ...")
        youtube_count = self.download_from_youtube()
        logger.info(f"✓ YouTube-dan {youtube_count} mahnı yükləndi\n")
        
        # Nəticə
        total = yandex_count + youtube_count
        logger.info("=" * 60)
        logger.info(f"✓ TOPLAM: {total} yeni mahnı yükləndi")
        logger.info("=" * 60)
        
        return total


def main():
    """Proqramın giriş nöqtəsi"""
    try:
        downloader = MusicDownloader()
        total_downloaded = downloader.run()
        
        if total_downloaded > 0:
            logger.info(f"\n🎉 Uğurlu! {total_downloaded} mahnı downloads/ qovluğundadır")
            logger.info("💡 İndi bu faylları iTunes-a əlavə edə bilərsiniz")
        else:
            logger.info("\n💤 Yeni mahnı tapılmadı")
        
        return 0
    
    except KeyboardInterrupt:
        logger.info("\n⚠ İstifadəçi tərəfindən dayandırıldı")
        return 1
    except Exception as e:
        logger.error(f"\n✗ Kritik xəta: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
