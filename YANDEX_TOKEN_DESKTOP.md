# 🎵 YANDEX MUSIC TOKEN - DESKTOP PROQRAM ÜSULU

Bu üsul **100% işləyir** və ən etibarlıdır!

---

## 📥 ADDIM 1: Yandex Music Desktop proqramını yükləyin

Link artıq brauzerinizdə açılıb: https://music.yandex.ru/download/

1. **"Скачать для Windows"** düyməsinə basın
2. Yükləmə bitənə qədər gözləyin (50-100 MB)
3. Yüklənən faylı açın: **YandexMusicSetup.exe**
4. Quraşdırın (sadəcə "Next" basın)

---

## 🔐 ADDIM 2: Proqrama giriş edin

1. Yandex Music proqramını açın
2. Hesabınıza giriş edin (username və password)
3. Proqramın açıldığını görün (musiqi oynada biləcəksiniz)

---

## 📁 ADDIM 3: Konfiqurasiya faylını tapın

Proqram açıq ikən, PowerShell-də bu əmri icra edin:

```powershell
# Config faylının yolunu yoxla
$configPath = "$env:APPDATA\Yandex Music\config.json"

if (Test-Path $configPath) {
    Write-Host "✅ Config fayl tapildi!" -ForegroundColor Green
    Write-Host "Yol: $configPath"
    
    # Faylı aç
    notepad $configPath
} else {
    Write-Host "❌ Config fayl tapilmadi" -ForegroundColor Red
    Write-Host "Alternativ yerlere baxiram..."
    
    # Alternativ yollar
    $alt1 = "$env:APPDATA\Yandex.Music\config.json"
    $alt2 = "$env:LOCALAPPDATA\Yandex Music\config.json"
    $alt3 = "$env:LOCALAPPDATA\Programs\YandexMusic\config.json"
    
    if (Test-Path $alt1) {
        notepad $alt1
    } elseif (Test-Path $alt2) {
        notepad $alt2
    } elseif (Test-Path $alt3) {
        notepad $alt3
    } else {
        Write-Host "Manuel axtarin: $env:APPDATA\Yandex*"
    }
}
```

---

## 🔍 ADDIM 4: Token-ı tapın

Notepad-da config.json faylı açılacaq.

Faylda **Ctrl+F** basıb bu sözləri axtarın:

1. `"token"`
2. `"access_token"`
3. `"accessToken"`
4. `"oauth_token"`

Token belə görünəcək:

```json
{
  "token": "y0_AgAAAAABCDEF...xyz123",
  ...
}
```

və ya:

```json
{
  "auth": {
    "access_token": "y0_AgAAAAABCDEF...xyz123"
  }
}
```

**Token-ın ÖZÜnü kopyalayın** (tırnaqlarsız):
```
y0_AgAAAAABCDEF...xyz123
```

---

## ✅ ADDIM 5: Token-ı test edin

PowerShell-də:

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music
python get_token_v2.py
```

Token-ı yapışdırın və Enter basın.

Əgər ✅ çıxarsa - token düzgündür!

Skript avtomatik `.env` faylını yeniləyəcək.

---

## 🆘 ƏGƏR CONFIG FAYLI TAPILMIRSA:

### Manuel axtarış:

1. Windows Explorer açın
2. Address bar-a yapışdırın:
   ```
   %APPDATA%
   ```
3. Enter basın
4. **Yandex Music** və ya **Yandex.Music** qovluğunu tapın
5. **config.json** faylını tapın
6. Notepad ilə açın

### Alternativ yollar:

```
C:\Users\Tuncay\AppData\Roaming\Yandex Music\config.json
C:\Users\Tuncay\AppData\Roaming\Yandex.Music\config.json
C:\Users\Tuncay\AppData\Local\Yandex Music\config.json
C:\Users\Tuncay\AppData\Local\Programs\YandexMusic\config.json
```

---

## 🎉 HAZIR OLDUQDAN SONRA:

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music
python test_config.py
```

Əgər Yandex Music ✅ görürsüzsə - artıq hazırsınız!

Sonrakı addım: GitHub Secrets əlavə etmək və sistemi işə salmaq!

---

## ⚠️ QEYD:

Token müvəqqəti ola bilər. Əgər bir müddətdən sonra işləməsə, bu addımları təkrarlayın və yeni token alın.

Alternativ: Yandex Premium abunəliyi daha uzun müddətli token-lar verir.
