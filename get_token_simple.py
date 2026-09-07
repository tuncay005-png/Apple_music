#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yandex Music Token - Sadə Üsul
Brauzerdən HAR fayl import edir
"""

import sys
import json
import re

print("=" * 60)
print("🔑 YANDEX MUSIC TOKEN - HAR FILE METHOD")
print("=" * 60)
print()
print("Bu üsul brauzerdən network activity export edir.")
print()
print("📋 ADDIMLAR:")
print()
print("1. Brauzerdə https://music.yandex.ru/ açın və giriş edin")
print("2. F12 → Network tab")
print("3. Səhifədə bir şey edin (playlist açın)")
print("4. Network-da hər hansı request-ə sağ klik")
print("5. 'Copy' → 'Copy as cURL (bash)'")
print("6. Buraya yapışdırın")
print()
print("=" * 60)
print()
print("cURL əmrini yapışdırın (və ya 'skip' yazın):")
print()

curl_command = input().strip()

if curl_command.lower() == 'skip' or not curl_command:
    print()
    print("=" * 60)
    print("📖 ALTERNATİV ÜSUL")
    print("=" * 60)
    print()
    print("Əgər cURL çətin gəlirsə, sadəcə SESSION_ID istifadə edə bilərik:")
    print()
    print("1. F12 → Application → Cookies → music.yandex.ru")
    print("2. 'Session_id' cookie-nin VALUE-sini kopyalayın")
    print("3. Bu skripti yenidən işə salın")
    print()
    print("Session ID (və ya Enter - çıxış):")
    session_id = input().strip()
    
    if not session_id:
        sys.exit(0)
    
    # Session ID ilə fake token yarat
    print()
    print("⏳ Session ID test edilir...")
    
    try:
        from yandex_music import Client
        
        # Session ID-ni OAuth token kimi işlət
        client = Client(session_id).init()
        me = client.me.account
        
        print()
        print("✅ İŞLƏYİR!")
        print(f"👤 İstifadəçi: {me.display_name}")
        print()
        print(f"Token: {session_id}")
        
        # .env yenilə
        print()
        print(".env faylını yeniləmək istəyirsiniz? (y/n): ", end='')
        if input().strip().lower() == 'y':
            with open('.env', 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = re.sub(r'YANDEX_TOKEN=.*', f'YANDEX_TOKEN={session_id}', content)
            
            with open('.env', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Yeniləndi!")
    
    except Exception as e:
        print(f"❌ İşləmir: {e}")
        print()
        print("💡 Yandex Music Desktop proqramı quraşdırın:")
        print("   https://music.yandex.ru/download/")
    
    sys.exit(0)

# cURL əmrindən token çıxart
print()
print("⏳ Token axtarılır...")

# Authorization header tap
auth_match = re.search(r"-H\s+'Authorization:\s*OAuth\s+([^']+)'", curl_command)
if not auth_match:
    auth_match = re.search(r'-H\s+"Authorization:\s*OAuth\s+([^"]+)"', curl_command)

if auth_match:
    token = auth_match.group(1)
    print()
    print("=" * 60)
    print("✅ TOKEN TAPILDI!")
    print("=" * 60)
    print()
    print(f"Token: {token}")
    print()
    
    # Test et
    try:
        from yandex_music import Client
        client = Client(token).init()
        me = client.me.account
        
        print(f"✅ Token işləyir!")
        print(f"👤 İstifadəçi: {me.display_name}")
        print()
        
        # .env yenilə
        print(".env faylını yeniləmək istəyirsiniz? (y/n): ", end='')
        if input().strip().lower() == 'y':
            with open('.env', 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = re.sub(r'YANDEX_TOKEN=.*', f'YANDEX_TOKEN={token}', content)
            
            with open('.env', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Yeniləndi!")
    
    except Exception as e:
        print(f"⚠️ Token test xətası: {e}")

else:
    print()
    print("❌ Token tapılmadı!")
    print()
    print("💡 Yenidən cəhd edin və tam cURL əmrini kopyalayın")

print()
