# 🚀 BURADAN BAŞLAYIN - TUNCAY

## ⚡ TƏZ BAŞLAMA (3 üsul)

---

### 🎯 ÜSUL 1: AVTOMATIK QURAŞDIRMA (Tövsiyə edilir)

PowerShell-i açın və bu əmri icra edin:

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music
.\auto_setup.ps1
```

Bu skript:
- ✅ Git və FFmpeg yoxlayır
- ✅ Python kitabxanalarını quraşdırır
- ✅ GitHub-a push edir
- ✅ Rclone Base64 string yaradır
- ✅ Lokal test imkanı verir

**Sadəcə ekrandakı təlimatları izləyin!**

---

### 📋 ÜSUL 2: ADDIM-ADDIM MANUAL

**SETUP_GUIDE_TUNCAY.md** faylını açın - orada hər şey ətraflı izah edilib.

Qısa xülasə:

1. **GitHub-a push edin:**
   ```powershell
   git init
   git remote add origin https://github.com/tuncay005-png/Apple_music.git
   git add .
   git commit -m "🎵 İlkin konfiqurasiya"
   git push -u origin main
   ```

2. **Rclone quraşdırın:**
   ```powershell
   winget install Rclone.Rclone
   rclone config
   ```

3. **Base64 string yaradın:**
   ```powershell
   $configPath = "$env:USERPROFILE\.config\rclone\rclone.conf"
   $base64 = [Convert]::ToBase64String([System.IO.File]::ReadAllBytes($configPath))
   $base64 | Set-Clipboard
   ```

4. **GitHub Secrets əlavə edin:**
   - https://github.com/tuncay005-png/Apple_music/settings/secrets/actions
   - **GITHUB_SECRETS_VALUES.txt** faylındakı dəyərləri kopyala-yapışdır

5. **İlk testi işə salın:**
   - https://github.com/tuncay005-png/Apple_music/actions
   - "Run workflow" düyməsi

---

### 🧪 ÜSUL 3: LOKAL TEST (GitHub olmadan)

```powershell
# Kitabxanaları quraşdırın
pip install -r requirements.txt

# Konfiqurasiyanı test edin
python test_config.py

# İşə salın
python main.py
```

Mahnılar `downloads/` qovluğunda olacaq.

---

## 📚 LAZIM OLAN FAYLLAR

| Fayl | Təsvir |
|------|--------|
| **START_HERE.md** | ← SİZ BURADASİNİZ |
| **SETUP_GUIDE_TUNCAY.md** | Ətraflı addım-addım təlimat |
| **GITHUB_SECRETS_VALUES.txt** | Kopyala-yapışdır secrets dəyərləri |
| **auto_setup.ps1** | Avtomatik quraşdırma skripti |
| **README.md** | Ümumi sənədləşdirmə |
| **QUICK_START_AZ.md** | 5 dəqiqəlik tez başlama |

---

## 🔗 LAZIM OLAN LİNKLƏR

| Link | Təsvir |
|------|--------|
| https://github.com/tuncay005-png/Apple_music | Sizin repository |
| https://github.com/tuncay005-png/Apple_music/settings/secrets/actions | GitHub Secrets |
| https://github.com/tuncay005-png/Apple_music/actions | GitHub Actions |
| https://music.yandex.ru/playlists/ed505ebb-11bf-3df9-9440-0a6c960cdf83 | Yandex pleylist |
| https://youtube.com/playlist?list=PLT4QS2kxaqBc | YouTube pleylist |
| https://drive.google.com | Google Drive |

---

## ✅ HAZIR OLAN KONFİQURASİYALAR

- ✅ Yandex Token: `y0__wgB...Mtzc`
- ✅ Yandex Playlist: `ed505ebb-11bf-3df9-9440-0a6c960cdf83`
- ✅ YouTube Playlist: `PLT4QS2kxaqBc`
- ✅ .env faylı konfiqurasiya olunub (lokal istifadə üçün)

---

## ❓ PROBLEM?

### "PowerShell skripti işə düşmür"

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### "Git push xəta verir"

```powershell
# GitHub CLI quraşdırın
winget install GitHub.cli

# Giriş edin
gh auth login

# Yenidən push edin
git push -u origin main
```

### "FFmpeg tapılmır"

```powershell
winget install ffmpeg
```

### "Python kitabxanaları quraşdırılmır"

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🎯 MƏQSƏD

Bu sistem:

1. **Yandex Music pleylistinizdəki** yeni mahnıları M4A + 1000x1000 qapaq şəkli ilə yükləyir
2. **YouTube pleylistinizdəki** yeni videoları M4A (qapaq şəkilsiz) yükləyir
3. **Google Drive-dakı Apple_Music** qovluğuna yüklə yir
4. **Hər gün gecə saat 00:00 (UTC)** avtomatik işləyir
5. **Kompüter bağlı olsa belə** işləyir (GitHub serverində)

---

## 🎉 UĞURLAR!

Sualınız varsa:
- **SETUP_GUIDE_TUNCAY.md** - ətraflı təlimat
- **README.md** - ümumi sənədləşdirmə
- GitHub Issues - problem bildir

**Zövq alın! 🎧**
