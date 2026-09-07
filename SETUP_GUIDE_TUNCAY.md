# 🎯 TUNCAY ÜÇÜN ADDIM-ADDIM TƏLİMAT

## ✅ HAZIRDA NƏ VAR:

- ✅ GitHub repository: https://github.com/tuncay005-png/Apple_music
- ✅ Yandex Music token: `y0__wgBENiDg8cHGIqPSSD86ff5GDDLm_ifCJZV9IbpHhSps_glxbeGg9EVMtzc`
- ✅ Yandex Playlist ID: `ed505ebb-11bf-3df9-9440-0a6c960cdf83`
- ✅ YouTube Playlist ID: `PLT4QS2kxaqBc`

---

## 📤 ADDIM 1: GITHUB-A YÜKLƏ (5 dəqiqə)

### PowerShell-i açın və bu əmrləri ardıcıl icra edin:

```powershell
# Layihə qovluğuna keçin
cd c:\Users\Tuncay\Desktop\Apple_music

# Git repository başladın
git init

# Remote əlavə edin (sizin GitHub linkiniz)
git remote add origin https://github.com/tuncay005-png/Apple_music.git

# Bütün faylları stage edin
git add .

# İlk commit
git commit -m "🎵 İlkin konfiqurasiya - avtomatik musiqi yükləmə sistemi"

# Main branch yaradın
git branch -M main

# GitHub-a push edin
git push -u origin main
```

### ⚠️ Əgər GitHub autentifikasiya soruşsa:

**Üsul 1: GitHub CLI (Tövsiyə edilir)**
```powershell
# GitHub CLI quraşdırın
winget install GitHub.cli

# Giriş edin
gh auth login
# Browser seçin və təlimatları izləyin

# Sonra yenidən push edin
git push -u origin main
```

**Üsul 2: Personal Access Token**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Repo tam hüquqları verin
4. Token-i kopyalayın
5. Push zamanı password olaraq istifadə edin

---

## 🔐 ADDIM 2: RCLONE QURAŞDIR VƏ KONFİQURASİYA ET (10 dəqiqə)

### 2.1: Rclone quraşdırın

PowerShell-də:
```powershell
winget install Rclone.Rclone
```

Və ya https://rclone.org/downloads/ səhifəsindən endirin.

### 2.2: Rclone konfiqurasiyası

```powershell
rclone config
```

İndi bu addımları DİQQƏTLƏ izləyin:

```
Sual: n/s/q> 
Cavab: n (yeni remote)

Sual: name>
Cavab: googledrive

Sual: Storage>
Cavab: drive (və ya nömrəsi 18)

Sual: client_id>
Cavab: (Boş buraxın, Enter basın)

Sual: client_secret>
Cavab: (Boş buraxın, Enter basın)

Sual: scope>
Cavab: 1 (Full access)

Sual: root_folder_id>
Cavab: (Boş buraxın, Enter basın)

Sual: service_account_file>
Cavab: (Boş buraxın, Enter basın)

Sual: Edit advanced config?>
Cavab: n

Sual: Use web browser to automatically authenticate?>
Cavab: y

>>> Brauzerdə Google hesabınıza giriş edəcəksiniz <<<
>>> "Allow" düyməsinə basın <<<

Sual: Configure this as a Shared Drive (Team Drive)?>
Cavab: n

Sual: Keep this "googledrive" remote?>
Cavab: y

Sual: e/n/d/r/c/s/q>
Cavab: q (çıxış)
```

### 2.3: Google Drive-da qovluq yaradın

```powershell
rclone mkdir googledrive:/Apple_Music
```

Yoxlama:
```powershell
rclone lsd googledrive:
```

`Apple_Music` qovluğunu görməlisiniz.

### 2.4: Rclone konfiqurasiyasını Base64-ə çevirin

```powershell
# Konfiqurasiya faylının yolunu tapın
$configPath = "$env:USERPROFILE\.config\rclone\rclone.conf"

# Əgər fayl tapılmazsa, alternativ yol:
if (-not (Test-Path $configPath)) {
    $configPath = "$env:APPDATA\rclone\rclone.conf"
}

# Faylı Base64-ə çevirin
$base64 = [Convert]::ToBase64String([System.IO.File]::ReadAllBytes($configPath))

# Nəticəni göstərin və clipboard-a kopyalayın
$base64 | Set-Clipboard
Write-Host "✅ Base64 string clipboard-a kopyalandı!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Base64 string (ilk 100 simvol):" -ForegroundColor Yellow
Write-Host $base64.Substring(0, [Math]::Min(100, $base64.Length))
Write-Host "..."
Write-Host ""
Write-Host "⚠️  Tam string clipboard-dadır, GitHub Secrets-ə yapışdırın!" -ForegroundColor Cyan
```

Bu əmr:
- ✅ Rclone konfiqurasiyasını Base64-ə çevirir
- ✅ Avtomatik clipboard-a kopyalayır
- ✅ Ekranda ilk 100 simvolu göstərir

**⚠️ ÖNƏMLİ:** Bu string çox uzundur (1000+ simvol). Clipboard-da saxlanır, GitHub-a keçəndə Ctrl+V basın.

---

## 🔑 ADDIM 3: GITHUB SECRETS ƏLAVƏ ET (5 dəqiqə)

### 3.1: GitHub-da Secrets səhifəsinə gedin

1. https://github.com/tuncay005-png/Apple_music açın
2. **Settings** düyməsinə klikləyin (yuxarıda sağda)
3. Sol menyudan **Secrets and variables** → **Actions** seçin
4. **New repository secret** düyməsinə basın

### 3.2: Bu 6 secret-i ARDICIAL əlavə edin:

#### Secret #1: YANDEX_TOKEN
```
Name: YANDEX_TOKEN
Secret: y0__wgBENiDg8cHGIqPSSD86ff5GDDLm_ifCJZV9IbpHhSps_glxbeGg9EVMtzc
```
**Add secret** basın.

#### Secret #2: YANDEX_PLAYLIST_ID
```
Name: YANDEX_PLAYLIST_ID
Secret: ed505ebb-11bf-3df9-9440-0a6c960cdf83
```
**Add secret** basın.

#### Secret #3: YOUTUBE_PLAYLIST_ID
```
Name: YOUTUBE_PLAYLIST_ID
Secret: PLT4QS2kxaqBc
```
**Add secret** basın.

#### Secret #4: RCLONE_CONFIG_CONTENT
```
Name: RCLONE_CONFIG_CONTENT
Secret: (Addım 2.4-dən aldığınız uzun Base64 string-i Ctrl+V ilə yapışdırın)
```
**Add secret** basın.

#### Secret #5: RCLONE_REMOTE_NAME
```
Name: RCLONE_REMOTE_NAME
Secret: googledrive
```
**Add secret** basın.

#### Secret #6: RCLONE_REMOTE_PATH
```
Name: RCLONE_REMOTE_PATH
Secret: /Apple_Music
```
**Add secret** basın.

### 3.3: Yoxlayın

**Secrets and variables** → **Actions** səhifəsində 6 secret görməlisiniz:
- ✅ YANDEX_TOKEN
- ✅ YANDEX_PLAYLIST_ID
- ✅ YOUTUBE_PLAYLIST_ID
- ✅ RCLONE_CONFIG_CONTENT
- ✅ RCLONE_REMOTE_NAME
- ✅ RCLONE_REMOTE_PATH

---

## 🚀 ADDIM 4: İLK TESTİ İŞƏ SALIN! (2 dəqiqə)

### 4.1: GitHub Actions səhifəsinə gedin

1. https://github.com/tuncay005-png/Apple_music/actions
2. Sol tərəfdə **"Avtomatik Musiqi Yükləmə"** workflow-unu seçin
3. Sağ tərəfdə **"Run workflow"** düyməsi var
4. Dropdown açılacaq → **"Run workflow"** düyməsinə basın

### 4.2: Gözləyin (2-5 dəqiqə)

- 🟡 Sarı dairə = İşləyir
- 🟢 Yaşıl işarə = Uğurlu!
- 🔴 Qırmızı X = Xəta

### 4.3: Nəticəni yoxlayın

**Əgər yaşıl ✅ gördüsəz:**

1. Google Drive-ı açın: https://drive.google.com
2. **Apple_Music** qovluğuna gedin
3. Yüklənən mahnıları görəcəksiniz! 🎉

**Əgər qırmızı ❌ gördüsəz:**

1. Xətalı workflow-a klikləyin
2. Qırmızı addıma klikləyin
3. Logs-u oxuyun
4. Ən çox rast gəlinən xətalar:
   - Yanlış token/ID
   - Rclone konfiqurasiyası düzgün deyil
   - Pleylist boşdur

---

## 🎯 AVTOMATLAŞDIRMA:

Artıq hər şey hazırdır! Sistem:

- ✅ **Hər gün gecə saat 00:00 (UTC)** avtomatik işləyəcək
- ✅ **Kompüter bağlı olsa belə** işləyir (GitHub serverində)
- ✅ **Yandex pleylistinizdəki yeni mahnıları** yükləyir
- ✅ **YouTube pleylistinizdəki yeni videoları** yükləyir
- ✅ **Google Drive-dakı Apple_Music qovluğuna** yüklə yir

### Siz nə edəcəksiniz?

1. Yandex Music-də mahnı bəyəndiniz → pleylistə əlavə edin
2. YouTube-da video bəyəndiniz → pleylistə əlavə edin
3. Sabah gecə sistem avtomatik yükləyəcək
4. Google Drive-dan kompüterinizə endirin
5. iTunes-a sürükləyib Apple Music-də dinləyin! 🎧

---

## 🧪 LOKAL TEST (İstəyə bağlı)

Kompüterinizdə də test etmək istəyirsinizsə:

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music

# FFmpeg quraşdırın (əgər yoxdursa)
winget install ffmpeg

# Python kitabxanalarını quraşdırın
pip install -r requirements.txt

# Konfiqurasiyanı test edin
python test_config.py

# İşə salın
python main.py
```

Mahnılar `downloads/` qovluğunda olacaq.

---

## 📊 SCHEDULE DƏYİŞDİRMƏK

Hər gün gecə deyil, başqa vaxt istəyirsinizsə:

1. `.github/workflows/auto_download.yml` faylını açın
2. Bu sətri tapın:
   ```yaml
   cron: '0 0 * * *'  # Hər gün saat 00:00 (UTC)
   ```
3. Dəyişdirin:
   - Hər 6 saatda: `'0 */6 * * *'`
   - Hər gün səhər 6: `'0 6 * * *'`
   - Həftədə bir: `'0 0 * * 0'`

⚠️ UTC saat qurşağıdır. Azərbaycan +4 saat.

---

## 🆘 PROBLEMLƏR?

### "git push" xəta verir
- GitHub CLI quraşdırın: `winget install GitHub.cli`
- Giriş edin: `gh auth login`

### "FFmpeg tapılmadı"
```powershell
winget install ffmpeg
# Və ya
choco install ffmpeg
```

### "Rclone config faylı tapılmadı"
Konfiqurasiya faylı bu yerlərdən birindədir:
- `C:\Users\Tuncay\.config\rclone\rclone.conf`
- `C:\Users\Tuncay\AppData\Roaming\rclone\rclone.conf`

Manuel yoxlayın:
```powershell
Get-ChildItem -Path $env:USERPROFILE -Filter "rclone.conf" -Recurse -ErrorAction SilentlyContinue
```

### GitHub Actions xəta verir
1. Actions səhifəsində xətalı workflow-a klikləyin
2. Hər addımın logs-unu oxuyun
3. Secret-lərin düzgün olduğunu yoxlayın

---

## 🎉 UĞURLAR!

Sualınız varsa, GitHub repository-də Issue açın!

**Zövq alın! 🎧**
