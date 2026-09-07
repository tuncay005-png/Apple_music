#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yandex Music Token Alıcı
Username ve password ile token yaradır
"""

import sys

print("=" * 60)
print("🔑 YANDEX MUSIC TOKEN ALIN")
print("=" * 60)
print()
print("⚠️  Yandex Music username ve password lazimdir")
print()

# Username
print("Username (email ve ya telefon): ", end='')
username = input().strip()

if not username:
    print("❌ Username bosh ola bilmez!")
    sys.exit(1)

# Password
print("Password: ", end='')
password = input().strip()

if not password:
    print("❌ Password bosh ola bilmez!")
    sys.exit(1)

print()
print("⏳ Token yaradilir...")
print()

try:
    from yandex_music import Client
    
    # Token yarat
    token = Client().generate_token_by_username_and_password(username, password)
    
    print("=" * 60)
    print("✅ TOKEN YARADILDI!")
    print("=" * 60)
    print()
    print("🔑 Sizin token:")
    print()
    print(token)
    print()
    print("=" * 60)
    
    # Token-i test et
    print()
    print("⏳ Token test edilir...")
    
    client = Client(token).init()
    me = client.me.account
    
    print(f"✅ Token isleyir!")
    print(f"👤 Istifadeci: {me.display_name}")
    print()
    
    # .env faylini yenile
    print("💾 .env faylini yenilemek isteyirsiniz? (y/n): ", end='')
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
            
            print("✅ .env fayli yenilendi!")
            print()
            print("🎉 Hazirsiniz! Indi test edin:")
            print("   python test_config.py")
            
        except Exception as e:
            print(f"⚠️  Fayl yenileme xetasi: {e}")
            print()
            print("💡 Manual olaraq .env faylinda deyishdin:")
            print(f"   YANDEX_TOKEN={token}")
    else:
        print()
        print("💡 Bu token-i .env faylina kopyalayin:")
        print(f"   YANDEX_TOKEN={token}")
    
    print()
    
except ImportError:
    print("❌ yandex-music kitabxanasi tapilmadi!")
    print("   Qurashdirin: pip install yandex-music")
    sys.exit(1)
    
except Exception as e:
    print("=" * 60)
    print("❌ XETA!")
    print("=" * 60)
    print()
    print(f"Səbəb: {e}")
    print()
    print("💡 Yoxlayin:")
    print("   - Username duzgundurmu? (email ve ya telefon)")
    print("   - Password duzgundurmu?")
    print("   - İnternet baglantisi varmi?")
    print()
    sys.exit(1)
