# 📋 MANUAL ADDIM-ADDIM (Sadə təlimat)

Skriptlər işləmirsə, bu addımları əl ilə edin.

---

## ✅ ADDIM 1: Python kitabxanalarını quraşdırın

PowerShell açın və:

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music
pip install -r requirements.txt
```

⏳ Bu 2-3 dəqiqə çəkə bilər. Gözləyin.

---

## ✅ ADDIM 2: FFmpeg quraşdırın (əgər yoxdursa)

```powershell
winget install ffmpeg
```

Yoxlamaq üçün:
```powershell
ffmpeg -version
```

---

## ✅ ADDIM 3: Konfiqurasiyanı test edin

```powershell
python test_config.py
```

Əgər yaşıl ✅ görürsüzsə - məlumatlar düzgündür!

---

## ✅ ADDIM 4: Lokal test (istəyə bağlı)

```powershell
python main.py
```

Mahnılar `downloads/` qovluğunda olacaq.

---

## ✅ ADDIM 5: GitHub-a push edin

```powershell
# Git repository başladın
git init

# Remote əlavə edin
git remote add origin https://github.com/tuncay005-png/Apple_music.git

# Faylları əlavə edin
git add .

# Commit yaradın
git commit -m "Initial setup"

# Main branch
git branch -M main

# Push edin
git push -u origin main
```

### ⚠️ Əgər autentifikasiya soruşsa:

**Üsul A: GitHub CLI (Tövsiyə edilir)**
```powershell
winget install GitHub.cli
gh auth login
git push -u origin main
```

**Üsul B: Personal Access Token**
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Repo hüquqları verin
4. Token-i kopyalayın
5. Push zamanı password olaraq yapışdırın

---

## ✅ ADDIM 6: Rclone quraşdırın

```powershell
winget install Rclone.Rclone
```

---

## ✅ ADDIM 7: Rclone konfiqurasiyası

```powershell
rclone config
```

### Təlimatlar:

```
Sual: n/s/q>
Cavab: n

Sual: name>
Cavab: googledrive

Sual: Storage>
Cavab: drive     (və ya nömrəsi, məs: 18)

Sual: client_id>
Cavab: (Boş - Enter basın)

Sual: client_secret>
Cavab: (Boş - Enter basın)

Sual: scope>
Cavab: 1

Sual: root_folder_id>
Cavab: (Boş - Enter basın)

Sual: service_account_file>
Cavab: (Boş - Enter basın)

Sual: Edit advanced config?>
Cavab: n

Sual: Use web browser to automatically authenticate?>
Cavab: y

>>> Brauzerdə Google hesabınıza giriş edin <<<
>>> "Allow" düyməsinə basın <<<

Sual: Configure this as a Shared Drive?>
Cavab: n

Sual: Keep this "googledrive" remote?>
Cavab: y

Sual: e/n/d/r/c/s/q>
Cavab: q
```

---

## ✅ ADDIM 8: Google Drive qovluğu yaradın

```powershell
rclone mkdir googledrive:/Apple_Music
```

Yoxlayın:
```powershell
rclone lsd googledrive:
```

---

## ✅ ADDIM 9: Rclone Base64 string yaradın

```powershell
$configPath = "$env:USERPROFILE\.config\rclone\rclone.conf"
if (-not (Test-Path $configPath)) {
    $configPath = "$env:APPDATA\rclone\rclone.conf"
}

$base64 = [Convert]::ToBase64String([System.IO.File]::ReadAllBytes($configPath))
$base64 | Set-Clipboard

Write-Host "OK - Clipboard-a kopyalandi!" -ForegroundColor Green
Write-Host "Ilk 100 simvol:"
Write-Host $base64.Substring(0, 100)
```

✅ Base64 string clipboard-dadır!

---

## ✅ ADDIM 10: GitHub Secrets əlavə edin

1. Linki açın:
   https://github.com/tuncay005-png/Apple_music/settings/secrets/actions

2. "New repository secret" düyməsi

3. Bu 6 secret-i əlavə edin:

### SECRET 1:
```
Name: YANDEX_TOKEN
Secret: y0__wgBENiDg8cHGIqPSSD86ff5GDDLm_ifCJZV9IbpHhSps_glxbeGg9EVMtzc
```
**Add secret** basın.

### SECRET 2:
```
Name: YANDEX_PLAYLIST_ID
Secret: ed505ebb-11bf-3df9-9440-0a6c960cdf83
```
**Add secret** basın.

### SECRET 3:
```
Name: YOUTUBE_PLAYLIST_ID
Secret: PLT4QS2kxaqBc
```
**Add secret** basın.

### SECRET 4:
```
Name: RCLONE_CONFIG_CONTENT
Secret: (Ctrl+V basın - clipboard-dakı Base64 string)
```
**Add secret** basın.

### SECRET 5:
```
Name: RCLONE_REMOTE_NAME
Secret: googledrive
```
**Add secret** basın.

### SECRET 6:
```
Name: RCLONE_REMOTE_PATH
Secret: /Apple_Music
```
**Add secret** basın.

---

## ✅ ADDIM 11: İlk workflow-u işə salın

1. https://github.com/tuncay005-png/Apple_music/actions

2. Sol tərəfdə "Avtomatik Musiqi Yükleme" seçin

3. Sağ tərəfdə "Run workflow" düyməsi

4. Dropdown-da "Run workflow" basın

5. 2-5 dəqiqə gözləyin

6. ✅ Yaşıl işarə = UĞURLU!

---

## 🎯 NƏTİCƏ:

Google Drive-ı açın:
https://drive.google.com

**Apple_Music** qovluğunda mahnılarınız olacaq! 🎉

---

## 🔄 AVTOMATLAŞDIRMA:

Artıq hər gün gecə saat 00:00 (UTC) sistem avtomatik:
- Yandex pleylistinizi yoxlayacaq
- YouTube pleylistinizi yoxlayacaq
- Yeni mahnıları yükləyəcək
- Google Drive-a əlavə edəcək

---

## 🆘 PROBLEMLƏR:

### "pip install" xəta verir:
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### "git push" xəta verir:
```powershell
gh auth login
```

### Rclone konfiqurasiya faylı tapılmır:
```powershell
# Manuel yoxlayın:
dir $env:USERPROFILE\.config\rclone\rclone.conf
dir $env:APPDATA\rclone\rclone.conf
```

---

## 🎉 UĞURLAR!

Bu addımları izləyərək tam işləyən sistem əldə edəcəksiniz!
