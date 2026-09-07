#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yandex Music Token - Alternative Method
Brauzerdən cookies ilə token alır
"""

import sys
import json

print("=" * 60)
print("🔑 YANDEX MUSIC TOKEN - ALTERNATIVE METHOD")
print("=" * 60)
print()
print("Bu üsul brauzerdən cookie istifadə edir.")
print()

# Cookie üsulu
print("📋 ADDIMLAR:")
print()
print("1. Brauzerə keçin və https://music.yandex.ru/ açın")
print("2. Hesabınıza giriş edin")
print("3. F12 basın → Application tab (Chrome) və ya Storage tab (Firefox)")
print("4. Sol tərəfdə: Cookies → https://music.yandex.ru")
print("5. 'access_token' və ya 'yandex_login' cookie-ni tapın")
print("6. Value-nu kopyalayın")
print()
print("=" * 60)
print()

# Manuel token daxil etmə
print("Və ya artıq token əldə etmisinizsə, buraya yapışdırın:")
print()
print("Token (boş buraxsanız, təlimatları göstərəcək): ", end='')
token = input().strip()

if not token:
    print()
    print("=" * 60)
    print("📖 ASAN ÜSUL - ŞƏKİLLƏRLƏ TƏLİMAT")
    print("=" * 60)
    print()
    print("🌐 Brauzerdə (Chrome/Edge):")
    print()
    print("Addım 1: https://music.yandex.ru/ açın və giriş edin")
    print()
    print("Addım 2: F12 basın (Developer Tools)")
    print()
    print("Addım 3: Yuxarıda 'Application' tabına klikləyin")
    print("         (Firefox-da 'Storage' tab)")
    print()
    print("Addım 4: Sol menüdə 'Cookies' açın")
    print("         → 'https://music.yandex.ru' seçin")
    print()
    print("Addım 5: Sağ tərəfdə cookies siyahısı görəcəksiniz")
    print("         Bu adlardan birini tapın:")
    print("         - access_token")
    print("         - yandex_login")  
    print("         - Session_id")
    print()
    print("Addım 6: Cookie-yə klikləyin")
    print("         Aşağıda 'Value' sahəsi görünəcək")
    print("         Value-nu seçib Ctrl+C ilə kopyalayın")
    print()
    print("Addım 7: Bu skripti yenidən işə salın:")
    print("         python get_token_v2.py")
    print("         Token-ı yapışdırın")
    print()
    print("=" * 60)
    print()
    print("⚠️  ƏGƏR COOKIES TAPILMIRSA:")
    print()
    print("Alternativ: Network method")
    print()
    print("1. F12 → Network tab")
    print("2. music.yandex.ru-da bir şeyə klikləyin (məs: pleylist)")
    print("3. Network-da 'account' və ya 'status' request-i tapın")
    print("4. Headers bölməsinə keçin")
    print("5. 'Authorization: OAuth TOKEN_BURADADIR' tapın")
    print("6. TOKEN hissəsini kopyalayın")
    print()
    sys.exit(0)

print()
print("⏳ Token yoxlanılır...")
print()

# Token-i test et
try:
    from yandex_music import Client
    
    client = Client(token).init()
    me = client.me.account
    
    print("=" * 60)
    print("✅ TOKEN İŞLƏYİR!")
    print("=" * 60)
    print()
    print(f"👤 İstifadəçi: {me.display_name}")
    print(f"📧 Login: {me.login}")
    print()
    print(f"🔑 Token: {token}")
    print()
    
    # .env faylını yenilə
    print("💾 .env faylını yeniləmək istəyirsiniz? (y/n): ", end='')
    update = input().strip().lower()
    
    if update == 'y':
        try:
            with open('.env', 'r', encoding='utf-8') as f:
                content = f.read()
            
            import re
            new_content = re.sub(
                r'YANDEX_TOKEN=.*',
                f'YANDEX_TOKEN={token}',
                content
            )
            
            with open('.env', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print()
            print("✅ .env faylı yeniləndi!")
            print()
            print("🎉 Hazırsınız! İndi test edin:")
            print("   python test_config.py")
            
        except Exception as e:
            print(f"⚠️  Xəta: {e}")
            print()
            print("💡 Manuel olaraq .env faylında dəyişdirin:")
            print(f"   YANDEX_TOKEN={token}")
    else:
        print()
        print("💡 Bu token-ı .env faylına əlavə edin:")
        print(f"   YANDEX_TOKEN={token}")
    
    print()

except ImportError:
    print("❌ yandex-music kitabxanası tapılmadı!")
    sys.exit(1)

except Exception as e:
    print("=" * 60)
    print("❌ TOKEN DÜZGÜN DEYİL!")
    print("=" * 60)
    print()
    print(f"Xəta: {e}")
    print()
    print("💡 Token yenidən əldə edin və cəhd edin.")
    print()
    sys.exit(1)
