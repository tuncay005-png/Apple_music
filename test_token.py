#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yandex Music Token Test
Token duzgun ishliyir ya yox yoxlayir
"""

import sys

print("=" * 60)
print("🔑 YANDEX MUSIC TOKEN TEST")
print("=" * 60)
print()

# Token-i daxil edin
print("Token-inizi yapishdir (Enter basin):")
token = input().strip()

if not token:
    print("❌ Token bosh ola bilmez!")
    sys.exit(1)

print()
print(f"Token uzunluqu: {len(token)} simvol")
print(f"Token baslangici: {token[:20]}...")
print()
print("⏳ Yoxlanilir...")
print()

try:
    from yandex_music import Client
    
    # Token-i yoxla
    client = Client(token).init()
    
    # Istifadeci melumatlari
    me = client.me.account
    
    print("=" * 60)
    print("✅ TOKEN DUZGUNDUR!")
    print("=" * 60)
    print()
    print(f"👤 Istifadeci: {me.display_name}")
    print(f"📧 Login: {me.login}")
    print(f"🎵 Premium: {'Bəli' if me.service_available else 'Xeyr'}")
    print()
    
    # .env faylini yenile
    print("⚠️  .env faylini yenilemek isteyirsiniz? (y/n): ", end='')
    update = input().strip().lower()
    
    if update == 'y':
        try:
            with open('.env', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Kohne token-i tap ve deyishdir
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
            print("İndi test edin:")
            print("  python test_config.py")
            
        except Exception as e:
            print(f"❌ Fayl yenileme xetasi: {e}")
    else:
        print()
        print("💡 Manual olaraq .env faylinda YANDEX_TOKEN-i deyishdin:")
        print(f"   YANDEX_TOKEN={token}")
    
    print()
    
except ImportError:
    print("❌ yandex-music kitabxanasi tapilmadi!")
    print("   Qurashdirin: pip install yandex-music")
    
except Exception as e:
    print("=" * 60)
    print("❌ TOKEN SEHVDIR!")
    print("=" * 60)
    print()
    print(f"Xeta: {e}")
    print()
    print("💡 Duzgun token almaq ucun:")
    print("   1. https://music.yandex.ru/ - acin")
    print("   2. F12 basin (Console)")
    print("   3. Bu kodu yapishdir:")
    print("      console.log(localStorage.getItem('access_token'));")
    print("   4. Cixan token-i kopyalayin")
    print()
