#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quraşdırma və test skripti
İlk dəfə istifadə üçün avtomatik yoxlama və konfiqurasiya
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Python versiyasını yoxla"""
    if sys.version_info < (3, 9):
        print("❌ Python 3.9 və ya daha yeni versiya tələb olunur")
        print(f"   Sizin versiyanız: {sys.version}")
        return False
    print(f"✅ Python versiyası: {sys.version_info.major}.{sys.version_info.minor}")
    return True

def check_ffmpeg():
    """FFmpeg quraşdırılıb-quraşdırılmadığını yoxla"""
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            print("✅ FFmpeg quraşdırılıb")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    
    print("❌ FFmpeg tapılmadı")
    print("   Quraşdırmaq üçün:")
    print("   - Windows: choco install ffmpeg  və ya  winget install ffmpeg")
    print("   - macOS:   brew install ffmpeg")
    print("   - Linux:   sudo apt install ffmpeg")
    return False

def check_env_file():
    """env faylını yoxla"""
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_file.exists():
        print("⚠️  .env faylı tapılmadı")
        if env_example.exists():
            print("   .env.example faylını .env olaraq kopyalayın:")
            print("   cp .env.example .env")
        return False
    
    # .env faylında vacib açarları yoxla
    with open(env_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    required_keys = ['YANDEX_TOKEN', 'YANDEX_PLAYLIST_ID', 'YOUTUBE_PLAYLIST_ID']
    missing_keys = []
    
    for key in required_keys:
        if f'{key}=your_' in content or f'{key}=' not in content:
            missing_keys.append(key)
    
    if missing_keys:
        print(f"⚠️  .env faylında bu açarlar düzgün doldurulmayıb:")
        for key in missing_keys:
            print(f"   - {key}")
        print("\n   README.md faylına baxaraq bu açarları doldurun")
        return False
    
    print("✅ .env faylı konfiqurasiya edilib")
    return True

def install_requirements():
    """Python kitabxanalarını quraşdır"""
    req_file = Path('requirements.txt')
    if not req_file.exists():
        print("❌ requirements.txt tapılmadı")
        return False
    
    print("📦 Python kitabxanaları quraşdırılır...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
                      check=True)
        print("✅ Bütün kitabxanalar quraşdırıldı")
        return True
    except subprocess.CalledProcessError:
        print("❌ Kitabxanalar quraşdırıla bilmədi")
        return False

def check_directories():
    """Lazımi qovluqları yarat"""
    downloads = Path('downloads')
    if not downloads.exists():
        downloads.mkdir()
        print("✅ downloads/ qovluğu yaradıldı")
    else:
        print("✅ downloads/ qovluğu mövcuddur")
    
    history = Path('history.txt')
    if not history.exists():
        history.touch()
        print("✅ history.txt faylı yaradıldı")
    else:
        print("✅ history.txt faylı mövcuddur")
    
    return True

def main():
    """Əsas quraşdırma funksiyası"""
    print("=" * 60)
    print("🎵 MUSİQİ YÜKLƏMƏ SİSTEMİ - QURAŞDIRMA")
    print("=" * 60)
    print()
    
    checks = []
    
    # Python versiyası
    print("1️⃣  Python versiyasını yoxlayırıq...")
    checks.append(check_python_version())
    print()
    
    # FFmpeg
    print("2️⃣  FFmpeg-i yoxlayırıq...")
    checks.append(check_ffmpeg())
    print()
    
    # Kitabxanaları quraşdır
    print("3️⃣  Python kitabxanalarını quraşdırırıq...")
    checks.append(install_requirements())
    print()
    
    # Qovluqlar
    print("4️⃣  Qovluqları yoxlayırıq...")
    checks.append(check_directories())
    print()
    
    # .env faylı
    print("5️⃣  Konfiqurasiya faylını yoxlayırıq...")
    env_ok = check_env_file()
    checks.append(env_ok)
    print()
    
    # Nəticə
    print("=" * 60)
    if all(checks):
        print("✅ QURAŞDIRMA TAMAMLANDI!")
        print()
        print("Növbəti addım:")
        print("  python main.py")
        print()
        print("və ya README.md faylına baxın")
    else:
        print("⚠️  QURAŞDIRMA TAMAMLANMADI")
        print()
        print("Yuxarıdakı xətaları düzəldib yenidən cəhd edin:")
        print("  python setup.py")
        if not env_ok:
            print()
            print("💡 İlk növbədə .env faylını konfiqurasiya edin!")
            print("   README.md faylında ətraflı təlimat var")
    print("=" * 60)

if __name__ == '__main__':
    main()
