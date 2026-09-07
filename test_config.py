#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Konfiqurasiya test skripti
GitHub Actions və lokal mühitdə konfiqurasiyanı yoxlayır
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# .env faylını yüklə
load_dotenv()

def test_yandex_config():
    """Yandex Music konfiqurasiyasını test et"""
    token = os.getenv('YANDEX_TOKEN')
    playlist_id = os.getenv('YANDEX_PLAYLIST_ID')
    
    if not token:
        print("❌ YANDEX_TOKEN təyin edilməyib")
        return False
    
    if not playlist_id:
        print("❌ YANDEX_PLAYLIST_ID təyin edilməyib")
        return False
    
    print(f"✅ Yandex Token: {token[:10]}...{token[-10:]}")
    print(f"✅ Yandex Playlist ID: {playlist_id}")
    
    # Yandex Music API-ni yoxla
    try:
        from yandex_music import Client
        client = Client(token).init()
        me = client.me.account
        print(f"✅ Yandex hesab: {me.display_name} (@{me.login})")
        
        # Pleylisti yoxla
        try:
            playlist = client.users_playlists(playlist_id)
            print(f"✅ Pleylist: {playlist.title} ({len(playlist.tracks)} mahnı)")
            return True
        except Exception as e:
            print(f"❌ Pleylist tapılmadı: {e}")
            return False
            
    except Exception as e:
        print(f"❌ Yandex Music bağlantısı xətası: {e}")
        return False

def test_youtube_config():
    """YouTube konfiqurasiyasını test et"""
    playlist_id = os.getenv('YOUTUBE_PLAYLIST_ID')
    
    if not playlist_id:
        print("⚠️  YOUTUBE_PLAYLIST_ID təyin edilməyib (istəyə bağlı)")
        return True
    
    print(f"✅ YouTube Playlist ID: {playlist_id}")
    
    # yt-dlp-ni yoxla
    try:
        import yt_dlp
        
        playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
        
        with yt_dlp.YoutubeDL({'quiet': True, 'extract_flat': 'in_playlist'}) as ydl:
            info = ydl.extract_info(playlist_url, download=False)
            
            if info and 'entries' in info:
                video_count = len([e for e in info['entries'] if e])
                print(f"✅ YouTube pleylist: {info.get('title', 'Unknown')} ({video_count} video)")
                return True
            else:
                print("❌ YouTube pleylist məlumatı əldə edilə bilmədi")
                return False
                
    except Exception as e:
        print(f"❌ YouTube bağlantısı xətası: {e}")
        return False

def test_rclone_config():
    """Rclone konfiqurasiyasını test et"""
    config_content = os.getenv('RCLONE_CONFIG_CONTENT')
    remote_name = os.getenv('RCLONE_REMOTE_NAME', 'googledrive')
    remote_path = os.getenv('RCLONE_REMOTE_PATH', '/Apple_Music')
    
    if not config_content:
        print("⚠️  RCLONE_CONFIG_CONTENT təyin edilməyib (GitHub Actions üçün vacibdir)")
        print(f"   Remote: {remote_name}")
        print(f"   Path: {remote_path}")
        return True
    
    print(f"✅ Rclone Config: {len(config_content)} simvol (Base64)")
    print(f"✅ Remote: {remote_name}")
    print(f"✅ Path: {remote_path}")
    return True

def main():
    """Əsas test funksiyası"""
    print("=" * 60)
    print("🧪 KONFİQURASİYA TESTİ")
    print("=" * 60)
    print()
    
    results = []
    
    print("1️⃣  Yandex Music konfiqurasiyası...")
    results.append(('Yandex Music', test_yandex_config()))
    print()
    
    print("2️⃣  YouTube konfiqurasiyası...")
    results.append(('YouTube', test_youtube_config()))
    print()
    
    print("3️⃣  Rclone konfiqurasiyası...")
    results.append(('Rclone', test_rclone_config()))
    print()
    
    # Nəticələr
    print("=" * 60)
    print("📊 TEST NƏTİCƏLƏRİ:")
    print()
    
    for name, result in results:
        status = "✅ UĞURLU" if result else "❌ UĞURSUZ"
        print(f"  {name}: {status}")
    
    print()
    
    if all(r for _, r in results):
        print("✅ Bütün testlər uğurla keçdi!")
        print("   İndi `python main.py` ilə musiqi yükləyə bilərsiniz")
        return 0
    else:
        print("⚠️  Bəzi testlər uğursuz oldu")
        print("   README.md faylına baxaraq konfiqurasiyanı düzəldin")
        return 1

if __name__ == '__main__':
    sys.exit(main())
