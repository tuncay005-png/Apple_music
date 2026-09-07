# 🎯 SON HƏ LL - YANDEX TOKEN

Microsoft Store versiyası token-ı şifrələnmiş saxlayır. 

**ƏN ASAN 2 YOL:**

---

## ✅ YOL 1: YANDEX-SİZ DAVAM ET (Tövsiyə edilir!)

Sistem YouTube ilə **tam işləyir**!

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music

# Konfiqurasiyanı test et (YouTube ✅ olacaq)
python test_config.py

# GitHub-a push et (artıq edilib ✅)

# GitHub Secrets əlavə et (yalnız YouTube)
```

**Yandex-i sonra əlavə edərik!**

---

## 🔧 YOL 2: cURL METODU (5 dəqiqə)

### Addım 1: Brauzerdə Yandex Music açın

https://music.yandex.ru/

Giriş edin.

### Addım 2: F12 → Network tab

### Addım 3: Pleylistinizi açın

https://music.yandex.ru/playlists/ed505ebb-11bf-3df9-9440-0a6c960cdf83

### Addım 4: Network-da request tapın

Siyahıda bu adlardan BİRİNİ tapın:
- **playlists**
- **account**
- **feed**

Və ya **HƏR HANSI** request (hansı olursa-olsun)

### Addım 5: SAĞ KLİK → Copy as cURL

Request-ə SAĞ KLİK:
- **Copy** → **Copy as cURL (bash)**

### Addım 6: Skripti işə salın

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music
python get_token_simple.py
```

cURL soruşanda **Ctrl+V** basın

---

## 💡 MƏNİM TÖVSİYƏM:

**YOL 1** - Yandex-siz davam et!

Səbəb:
- ✅ YouTube artıq işləyir
- ✅ GitHub-a push edilib
- ✅ Sistem hazırdır
- ✅ Yandex-i sonra əlavə edə bilərik

**İndicə edək:**

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music

# Test et
python test_config.py

# Nəticə:
# ❌ Yandex (skip olacaq)
# ✅ YouTube (işləyir!)
# ✅ Rclone (hazır)
```

Sonra GitHub Secrets əlavə edək və sistem işləsin!

Yandex token-ı **istədiyiniz zaman** əlavə edə bilərik.

---

## 🚀 DAVAM EDƏK?

Hansını seçirsiniz:

**A) Yandex-siz davam et** - Sistem işləsin, Yandex sonra ✅

**B) cURL metodu ilə Yandex token al** - 5 dəqiqə

Mən **A** tövsiyə edirəm!
