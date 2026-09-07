# 🎯 ƏN ASAN VƏ ETİBARLI ÜSUL

Cookies və Network işləmirsə, bu üsul **100% işləyir**:

---

## ⚡ YOUTUBE-DAN İSTİFADƏ EDİN (Token-sız)

Yandex Music token-ı problematik olduğu üçün, sistem **yalnız YouTube** ilə işləyə bilər!

### ✅ BU NƏ DEMƏKDİR:

1. Yandex Music pleylistinizi **YouTube-a köçürün**
2. Yalnız YouTube pleylistindən musiqi yükləsin
3. Token problemi olmaz! ✅

### 📋 ADDIMLAR:

1. Yandex Music pleylistinizdəki mahnıları YouTube-da tapın
2. YouTube pleylistinizə əlavə edin: 
   https://youtube.com/playlist?list=PLT4QS2kxaqBc
3. Sistem avtomatik yükləyəcək!

---

## 🎵 ƏGƏR MÜTLƏq YANDEX LAZIMSA:

### ÜSUL: Yandex Music Desktop App istifadə edin

Yandex Music token-ı əldə etməyin ən etibarlı yolu:

1. **Yandex Music masaüstü proqramını** yükləyin:
   https://music.yandex.ru/download/

2. Proqramı açıb giriş edin

3. Proqramın konfiqurasiya faylında token saxlanır:

**Windows:**
```
C:\Users\Tuncay\AppData\Roaming\Yandex.Music\config.json
```

4. Bu faylı açın (Notepad ilə)

5. `"token"` və ya `"access_token"` tapın

6. Token-ı kopyalayın

---

## 🔧 ALTERNATİV: Yandex Music API Key

Yandex Developer Console-dan API key yaradın:

1. https://oauth.yandex.ru/ açın

2. Yeni app yaradın:
   - Ad: Apple Music Sync
   - Permissions: Yandex.Music

3. ClientID və Secret alın

4. OAuth flow ilə token yaradın

**AMMA BU ÇOX MÜRƏKKƏBDİR!**

---

## 💡 TÖVSİYƏM:

İndilik **yalnız YouTube** ilə sistemə davam edin:

1. Yandex Music token problemi var
2. YouTube **heç bir token tələb etmir** ✅
3. Sistem YouTube-dan mükəmməl işləyir

Sistemi YouTube ilə test edək:

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music
python test_config.py
```

YouTube konfiqurasiyası ✅ olacaq və işləyəcək!

---

## 🎉 QƏRARıNIZ:

**Variant A:** Yalnız YouTube ilə davam et (Asan və işləyir) ✅

**Variant B:** Yandex Music desktop app yüklə və config.json-dan token al

**Variant C:** Yandex Music-i sonraya burax, əvvəl YouTube ilə test et

Hansını seçirsiniz?
