# ⚡ TEZ BAŞLAMA (5 dəqiqə)

Bu təlimat sizə ən qısa yolla sistemin işlək vəziyyətə gətirilməsini göstərir.

---

## 🎯 1-ci Addım: Repository-ni GitHub-a yüklə (2 dəq)

```bash
cd c:\Users\Tuncay\Desktop\Apple_music

# Git repository başlat
git init

# Remote əlavə et (SİZİN repository link-inizi yazın!)
git remote add origin https://github.com/SİZİN_İSTİFADƏÇİ_ADINIZ/Apple_music.git

# İlk commit
git add .
git commit -m "🎵 İlkin konfiqurasiya"

# GitHub-a push et
git branch -M main
git push -u origin main
```

---

## 🔑 2-ci Addım: Token və ID-ləri əldə et (2 dəq)

### Yandex Music Token:

1. [music.yandex.ru](https://music.yandex.ru/) - daxil ol
2. **F12** bas (Console aç)
3. Yapışdır: `console.log(localStorage.getItem('access_token'));`
4. Token-i kopyala

### Yandex Playlist ID:

1. Pleylistini aç
2. URL-dən ID-ni götür: `https://music.yandex.ru/users/XXX/playlists/1234`
   - `1234` - bu sizin ID-nizdir

### YouTube Playlist ID:

1. YouTube pleylistini aç
2. URL-dən ID-ni götür: `https://www.youtube.com/playlist?list=PLxxxx...`
   - `PLxxxx...` - bu sizin ID-nizdir

---

## 🔐 3-cü Addım: Rclone konfiqurasiyası (1 dəq)

### Windows PowerShell-də:

```powershell
# Rclone quraşdır
winget install Rclone.Rclone

# Konfiqurasiya et
rclone config

# n → googledrive → drive → Enter Enter → 1 → Enter → y (brauzerdə giriş)
```

### Konfiqurasiyanı Base64-ə çevir:

```powershell
$configPath = "$env:USERPROFILE\.config\rclone\rclone.conf"
[Convert]::ToBase64String([System.IO.File]::ReadAllBytes($configPath))
```

Çıxan **uzun string-i kopyala!**

---

## 🎮 4-cü Addım: GitHub Secrets əlavə et (1 dəq)

1. GitHub-da repository-nizə get
2. **Settings** → **Secrets and variables** → **Actions**
3. **New repository secret** - 6 dənə əlavə et:

| Ad | Dəyər |
|----|-------|
| `YANDEX_TOKEN` | Yandex token-iniz |
| `YANDEX_PLAYLIST_ID` | `1234` (sizin ID) |
| `YOUTUBE_PLAYLIST_ID` | `PLxxxx...` (sizin ID) |
| `RCLONE_CONFIG_CONTENT` | Base64 string (uzun) |
| `RCLONE_REMOTE_NAME` | `googledrive` |
| `RCLONE_REMOTE_PATH` | `/Apple_Music` |

---

## ✅ HAZIRSINIZ! 

### GitHub Actions avtomatik işləyəcək:
- ✅ Hər gün gecə saat 00:00 (UTC)
- ✅ Və ya **Actions** → **Run workflow** düyməsi ilə

### İlk testi indicə işə sal:
1. GitHub repository → **Actions**
2. Sol tərəfdə **Avtomatik Musiqi Yükləmə** seç
3. Sağ tərəfdə **Run workflow** → **Run workflow**
4. 2-3 dəqiqə gözlə
5. Yaşıl ✅ görərsənsə - UĞURLUDUR!

### Mahnılar haradadır?
- **Google Drive** → **Apple_Music** qovluğunda
- Oradan kompüterinizə endirəcək və **iTunes-a sürükləyəcəksiniz**

---

## 🧪 Lokal test (istəyə bağlı)

Kompüterinizdə test etmək istəyirsinizsə:

```bash
# .env faylı yarat
copy .env.example .env

# .env-i düzənlə (Notepad ilə aç və doldur)

# Quraşdır
pip install -r requirements.txt

# Test et
python test_config.py

# İşə sal
python main.py
```

Mahnılar `downloads/` qovluğunda olacaq.

---

## 🆘 Problem oldu?

1. **Actions** səhifəsində xətalı workflow-a klik et
2. Qırmızı addıma bax
3. Logs-u oxu
4. README.md-də həll yolu var

---

## 🎉 Həvəs Verin!

Artıq sizin musiqi yükləmə robotunuz var! 🤖🎵

**Zövq alın! 🎧**
