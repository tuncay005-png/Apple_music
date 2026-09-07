# 🎵 Avtomatik Musiqi Yükləmə Sistemi

Yandex Music və YouTube pleylistlərinizdən avtomatik olaraq mahnıları yükləyib Apple Music/iTunes üçün hazırlayan sistem.

## 🌟 Xüsusiyyətlər

- ✅ **Yandex Music-dən yükləmə**: Xam M4A (AAC) formatında, 1000x1000 qapaq şəkli ilə
- ✅ **YouTube-dan yükləmə**: Xam M4A formatında, qapaq şəkilsiz
- ✅ **Apple Music uyğunluğu**: iTunes-da qapaq şəkillərinin 100% görünməsi üçün Baseline JPEG formatı
- ✅ **Təkrar yükləmə qarşısı**: history.txt faylı ilə yüklənmiş mahnılar izlənir
- ✅ **GitHub Actions avtomatlaşdırması**: Hər gün gecə 12-də avtomatik işləyir
- ✅ **Google Drive inteqrasiyası**: Yüklənən fayllar avtomatik olaraq Google Drive-a yüklənir
- ✅ **Kompüter bağlı olsa belə işləyir**: Cloud-da tamamilə avtomatik

---

## 📋 Tələblər

### Lokal istifadə üçün:
- Python 3.9 və ya daha yeni versiya
- FFmpeg (audio emalı üçün)
- Git

### GitHub Actions üçün:
- GitHub hesabı
- Yandex Music hesabı və token
- Google Drive hesabı və rclone konfiqurasiyası

---

## 🚀 Quraşdırma

### 1. Repository-ni klonlayın

```bash
git clone https://github.com/SİZİN_İSTİFADƏÇİ_ADINIZ/Apple_music.git
cd Apple_music
```

### 2. Python kitabxanalarını quraşdırın

```bash
pip install -r requirements.txt
```

### 3. FFmpeg quraşdırın

**Windows:**
```powershell
# Chocolatey ilə
choco install ffmpeg

# Və ya winget ilə
winget install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg  # Debian/Ubuntu
sudo yum install ffmpeg  # CentOS/RHEL
```

---

## 🔑 Konfiqurasiya

### 1. Yandex Music Token əldə edin

**Asan üsul (Brauzerdə):**

1. [Yandex Music](https://music.yandex.ru/) saytına daxil olun
2. Brauzer Console-unu açın (F12 basın)
3. Console-da bu kodu yapışdırın:

```javascript
console.log(localStorage.getItem('access_token'));
```

4. Çıxan token-i kopyalayın (uzun hərflər və rəqəmlər)

**Alternativ üsul (Python ilə):**

```bash
pip install yandex-music
python -c "from yandex_music import Client; print(Client().generate_token_by_username_and_password('USERNAME', 'PASSWORD'))"
```

### 2. Yandex Playlist ID əldə edin

1. Yandex Music-də öz pleylistinizi açın
2. URL-dən ID-ni kopyalayın:
   ```
   https://music.yandex.ru/users/USERNAME/playlists/1234
                                                        ^^^^
                                                   Bu sizin ID-nizdir
   ```

### 3. YouTube Playlist ID əldə edin

1. YouTube-da öz pleylistinizi açın
2. URL-dən ID-ni kopyalayın:
   ```
   https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxxxxxxx
                                          ^^^^^^^^^^^^^^^^^^^^^^^
                                       Bu sizin Playlist ID-nizdir
   ```

### 4. Rclone ilə Google Drive konfiqurasiyası

**Addım 1: Rclone quraşdırın**

```bash
# Windows (PowerShell)
winget install Rclone.Rclone

# macOS
brew install rclone

# Linux
curl https://rclone.org/install.sh | sudo bash
```

**Addım 2: Google Drive-ı konfiqurasiya edin**

```bash
rclone config
```

Sonra bu addımları izləyin:

1. `n` (new remote)
2. Ad verin: `googledrive`
3. Storage növü seçin: `drive` (Google Drive)
4. Client ID və Secret: boş buraxın (Enter basın)
5. Scope seçin: `1` (Full access)
6. Root folder: boş buraxın
7. Service account: `n`
8. Auto config: `y` (brauzerdə açılacaq, hesabınıza giriş edin)
9. Team Drive: `n`
10. `y` (Yes this is OK)
11. `q` (Quit)

**Addım 3: Google Drive-da qovluq yaradın**

```bash
rclone mkdir googledrive:/Apple_Music
```

**Addım 4: Konfiqurasiya faylını Base64-ə çevirin** (GitHub Secrets üçün)

```bash
# Windows (PowerShell)
$configPath = "$env:USERPROFILE\.config\rclone\rclone.conf"
[Convert]::ToBase64String([System.IO.File]::ReadAllBytes($configPath))

# macOS/Linux
base64 -w 0 ~/.config/rclone/rclone.conf
```

Çıxan uzun string-i kopyalayın.

---

## 🔐 GitHub Secrets konfiqurasiyası

1. GitHub-da repository-nizə gedin
2. **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Aşağıdakı secret-ləri əlavə edin:

| Secret adı | Dəyəri | Harada əldə etmək olar |
|-----------|--------|------------------------|
| `YANDEX_TOKEN` | Yandex Music token-iniz | Yuxarıdakı "Yandex Music Token" bölməsinə baxın |
| `YANDEX_PLAYLIST_ID` | Yandex pleylist ID-niz | Pleylist URL-indən (məs: `1234`) |
| `YOUTUBE_PLAYLIST_ID` | YouTube pleylist ID-niz | Pleylist URL-indən (məs: `PLxxxx...`) |
| `RCLONE_CONFIG_CONTENT` | Base64 encoded rclone.conf | Yuxarıdakı "Rclone" bölməsinin Addım 4-ə baxın |
| `RCLONE_REMOTE_NAME` | `googledrive` | Rclone config zamanı verdiyiniz ad |
| `RCLONE_REMOTE_PATH` | `/Apple_Music` | Google Drive-dakı qovluq yolu |

---

## 🎮 İstifadə

### Lokal istifadə (Kompüterinizde)

1. `.env` faylı yaradın:

```bash
cp .env.example .env
```

2. `.env` faylını düzənləyin və məlumatları doldur un:

```env
YANDEX_TOKEN=sizin_yandex_token
YANDEX_PLAYLIST_ID=1234
YOUTUBE_PLAYLIST_ID=PLxxxxxxxxxxxx
```

3. Proqramı işə salın:

```bash
python main.py
```

4. Yüklənən fayllar `downloads/` qovluğunda olacaq

5. İndi bu faylları iTunes-a sürükləyib Apple Music-ə əlavə edə bilərsiniz!

### GitHub Actions ilə avtomatik istifadə

1. Yuxarıdakı GitHub Secrets-i konfiqurasiya edin
2. Repository-ni GitHub-a push edin:

```bash
git add .
git commit -m "🎵 İlkin konfiqurasiya"
git push origin main
```

3. **GitHub Actions avtomatik işə düşəcək:**
   - Hər gün gecə saat 00:00 (UTC)
   - Və ya **Actions** səhifəsindən manual olaraq "Run workflow" düyməsi ilə

4. Yüklənən fayllar avtomatik olaraq Google Drive-dakı `Apple_Music` qovluğuna yüklənəcək

5. Sonra Google Drive-dan kompüterinizə endirəcək və iTunes-a əlavə edəcəksiniz

---

## 📁 Qovluq strukturu

```
Apple_music/
├── .github/
│   └── workflows/
│       └── auto_download.yml    # GitHub Actions konfiqurasiyası
├── downloads/                   # Yüklənən musiqi faylları (git-də yoxdur)
├── .env                         # Lokal konfiqurasiya (git-də yoxdur)
├── .env.example                 # Konfiqurasiya nümunəsi
├── .gitignore                   # Git ignore qaydaları
├── history.txt                  # Yüklənmiş mahnıların ID-ləri
├── main.py                      # Əsas proqram
├── music_downloader.log         # Log faylı
├── README.md                    # Bu fayl
└── requirements.txt             # Python asılılıqları
```

---

## 🔍 Necə işləyir?

### Yandex Music-dən yükləmə:

1. Yandex Music pleylistinizdəki bütün mahnıları skan edir
2. `history.txt`-də olmayan (yəni yeni) mahnıları tapır
3. Hər mahnını **xam M4A (AAC)** formatında yükləyir
4. **1000x1000** ölçülü qapaq şəklini Yandex-dən əldə edir
5. Qapaq şəklini **Apple-ın Baseline JPEG** formatına çevirib faylın içinə embed edir
6. iTunes-da şəkil 100% görünür ✅

### YouTube-dan yükləmə:

1. YouTube pleylistinizdəki bütün videoları skan edir
2. `history.txt`-də olmayan yeni videoları tapır
3. Hər videodan **xam M4A (AAC)** audio-nu çıxarır
4. **Qapaq şəkli əlavə etmir** (sizin istəyiniz üzrə)
5. Təmiz audio faylı hazırdır ✅

---

## 🛠️ Troubleshooting (Problem həlli)

### ❌ "yandex-music kitabxanası tapılmadı"

```bash
pip install --upgrade yandex-music
```

### ❌ "FFmpeg tapılmadı"

FFmpeg-in PATH-ə əlavə olunduğundan əmin olun:

```bash
ffmpeg -version
```

Əgər xəta versə, FFmpeg-i yenidən quraşdırın.

### ❌ "Google Drive-a yükləmə xətası"

Rclone konfiqurasiyasını yoxlayın:

```bash
rclone listremotes
rclone lsd googledrive:
```

### ❌ "Qapaq şəkli iTunes-da görünmür"

- Yandex Music-dən yüklənənlərdə bu problem olmamalıdır (Baseline JPEG)
- YouTube-dan yüklənənlərdə qapaq şəkli yoxdur (sizin istəyiniz)
- Əgər hələ də problem varsa, [TagScanner](https://www.xdlab.ru/en/) proqramı ilə manual olaraq əlavə edin

---

## 📊 Log faylları

- **music_downloader.log**: Proqramın log faylı (lokal)
- **GitHub Actions logs**: Actions səhifəsində hər run üçün ayrı log

---

## ⏰ Cron schedule dəyişdirmə

`.github/workflows/auto_download.yml` faylında bu sətrə baxın:

```yaml
schedule:
  - cron: '0 0 * * *'  # Hər gün saat 00:00 (UTC)
```

**Başqa vaxt seçmək üçün:**

- Hər 6 saatda bir: `'0 */6 * * *'`
- Hər gün səhər saat 6: `'0 6 * * *'`
- Həftədə bir dəfə (Bazar): `'0 0 * * 0'`

**⚠️ Qeyd:** UTC saat qurşağıdır. Azərbaycan üçün +4 saat əlavə edin.

---

## 🤝 Töhfələr

Pull request-lər qəbul edilir! Böyük dəyişikliklər üçün əvvəlcə issue açın.

---

## 📜 Lisenziya

Bu layihə şəxsi istifadə üçün açıq mənbəlidir. Kommersiya məqsədləri üçün müəllif ilə əlaqə saxlayın.

---

## 📞 Dəstək

Problemlə qarşılaşsanız:

1. **Əvvəlcə log fayllarını yoxlayın**: `music_downloader.log`
2. **GitHub Actions logs**: Repository → Actions → son workflow run
3. **Issue açın**: Problemi təsvir edin və log-dan əlaqəli hissəni əlavə edin

---

## 🎉 Uğurlar!

İndi sizin musiqi yükləmə sisteminiz tam avtomatikdir! Hər gün yeni mahnılar Google Drive-da səni gözləyəcək. 🎵

**Zövq alın! 🎧**
