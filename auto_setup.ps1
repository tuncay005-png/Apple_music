# Avtomatik quraşdırma skripti - Tuncay üçün
# Bu skript bütün prosesi avtomatlaşdırır

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host "🎵 MUSİQİ YÜKLƏMƏ SİSTEMİ - AVTOMATIK QURAŞDIRMA" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""

# Məkan yoxla
$currentPath = Get-Location
if ($currentPath.Path -ne "c:\Users\Tuncay\Desktop\Apple_music") {
    Write-Host "⚠️  Xəta: Bu skript layihə qovluğunda işləməlidir" -ForegroundColor Red
    Write-Host "   cd c:\Users\Tuncay\Desktop\Apple_music" -ForegroundColor Yellow
    exit 1
}

# 1. Git quraşdırılıbmı?
Write-Host "1️⃣  Git yoxlanılır..." -ForegroundColor Cyan
try {
    $gitVersion = git --version
    Write-Host "   ✅ Git quraşdırılıb: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Git tapılmadı!" -ForegroundColor Red
    Write-Host "   Quraşdırın: winget install Git.Git" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# 2. FFmpeg quraşdırılıbmı?
Write-Host "2️⃣  FFmpeg yoxlanılır..." -ForegroundColor Cyan
try {
    $ffmpegVersion = ffmpeg -version 2>&1 | Select-Object -First 1
    Write-Host "   ✅ FFmpeg quraşdırılıb" -ForegroundColor Green
} catch {
    Write-Host "   ⚠️  FFmpeg tapılmadı" -ForegroundColor Yellow
    Write-Host "   Quraşdırmaq istəyirsiniz? (y/n): " -NoNewline
    $install = Read-Host
    if ($install -eq "y") {
        winget install ffmpeg
    }
}

Write-Host ""

# 3. Python kitabxanaları
Write-Host "3️⃣  Python kitabxanaları quraşdırılır..." -ForegroundColor Cyan
try {
    pip install -r requirements.txt --quiet
    Write-Host "   ✅ Kitabxanalar quraşdırıldı" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Xəta: Kitabxanalar quraşdırıla bilmədi" -ForegroundColor Red
}

Write-Host ""

# 4. Git repository
Write-Host "4️⃣  Git repository konfiqurasiyası..." -ForegroundColor Cyan

if (Test-Path ".git") {
    Write-Host "   ⚠️  Git repository artıq mövcuddur" -ForegroundColor Yellow
    Write-Host "   Yenidən başlatmaq istəyirsiniz? (y/n): " -NoNewline
    $reinit = Read-Host
    if ($reinit -eq "y") {
        Remove-Item -Recurse -Force .git
        git init
        Write-Host "   ✅ Repository yenidən başladıldı" -ForegroundColor Green
    }
} else {
    git init
    Write-Host "   ✅ Repository başladıldı" -ForegroundColor Green
}

# Remote əlavə et
try {
    git remote remove origin 2>$null
} catch {}

git remote add origin https://github.com/tuncay005-png/Apple_music.git
Write-Host "   ✅ Remote əlavə edildi" -ForegroundColor Green

Write-Host ""

# 5. GitHub autentifikasiya yoxla
Write-Host "5️⃣  GitHub autentifikasiyası yoxlanılır..." -ForegroundColor Cyan
try {
    gh --version | Out-Null
    $authStatus = gh auth status 2>&1
    if ($authStatus -match "Logged in") {
        Write-Host "   ✅ GitHub CLI autentifikasiya olunub" -ForegroundColor Green
    } else {
        Write-Host "   ⚠️  GitHub CLI autentifikasiya olunmayıb" -ForegroundColor Yellow
        Write-Host "   İndi autentifikasiya etmək istəyirsiniz? (y/n): " -NoNewline
        $doAuth = Read-Host
        if ($doAuth -eq "y") {
            gh auth login
        }
    }
} catch {
    Write-Host "   ⚠️  GitHub CLI quraşdırılmayıb" -ForegroundColor Yellow
    Write-Host "   Quraşdırmaq istəyirsiniz? (y/n): " -NoNewline
    $installGH = Read-Host
    if ($installGH -eq "y") {
        winget install GitHub.cli
        Write-Host "   ✅ GitHub CLI quraşdırıldı" -ForegroundColor Green
        Write-Host "   İndi autentifikasiya edin: gh auth login" -ForegroundColor Yellow
    }
}

Write-Host ""

# 6. Git commit və push
Write-Host "6️⃣  Faylları GitHub-a yükləmək istəyirsiniz? (y/n): " -NoNewline -ForegroundColor Cyan
$doPush = Read-Host

if ($doPush -eq "y") {
    Write-Host "   📦 Fayllar stage edilir..." -ForegroundColor Cyan
    git add .
    
    Write-Host "   💾 Commit yaradılır..." -ForegroundColor Cyan
    git commit -m "🎵 İlkin konfiqurasiya - avtomatik musiqi yükləmə sistemi"
    
    Write-Host "   📤 GitHub-a push edilir..." -ForegroundColor Cyan
    git branch -M main
    
    try {
        git push -u origin main
        Write-Host "   ✅ Uğurla GitHub-a yükləndi!" -ForegroundColor Green
        Write-Host ""
        Write-Host "   🔗 Repository: https://github.com/tuncay005-png/Apple_music" -ForegroundColor Blue
    } catch {
        Write-Host "   ❌ Push xətası!" -ForegroundColor Red
        Write-Host "   Manuel cəhd edin:" -ForegroundColor Yellow
        Write-Host "   gh auth login" -ForegroundColor White
        Write-Host "   git push -u origin main" -ForegroundColor White
    }
}

Write-Host ""

# 7. Rclone yoxla
Write-Host "7️⃣  Rclone konfiqurasiyası..." -ForegroundColor Cyan
try {
    $rcloneVersion = rclone version 2>&1 | Select-Object -First 1
    Write-Host "   ✅ Rclone quraşdırılıb" -ForegroundColor Green
    
    # Remote-ləri yoxla
    $remotes = rclone listremotes
    if ($remotes -match "googledrive:") {
        Write-Host "   ✅ 'googledrive' remote konfiqurasiya olunub" -ForegroundColor Green
        
        # Base64 string yarat
        Write-Host ""
        Write-Host "   🔐 Rclone konfiqurasiyasını Base64-ə çevirmək istəyirsiniz? (y/n): " -NoNewline
        $doBase64 = Read-Host
        
        if ($doBase64 -eq "y") {
            $configPath = "$env:USERPROFILE\.config\rclone\rclone.conf"
            if (-not (Test-Path $configPath)) {
                $configPath = "$env:APPDATA\rclone\rclone.conf"
            }
            
            if (Test-Path $configPath) {
                $base64 = [Convert]::ToBase64String([System.IO.File]::ReadAllBytes($configPath))
                $base64 | Set-Clipboard
                
                Write-Host ""
                Write-Host "   ✅ Base64 string clipboard-a kopyalandı!" -ForegroundColor Green
                Write-Host ""
                Write-Host "   📋 İlk 100 simvol:" -ForegroundColor Yellow
                Write-Host "   $($base64.Substring(0, [Math]::Min(100, $base64.Length)))..." -ForegroundColor White
                Write-Host ""
                Write-Host "   ⚠️  İNDİ BU ADDIMI İZLƏYİN:" -ForegroundColor Yellow
                Write-Host "   1. https://github.com/tuncay005-png/Apple_music/settings/secrets/actions açın" -ForegroundColor White
                Write-Host "   2. 'New repository secret' düyməsinə basın" -ForegroundColor White
                Write-Host "   3. Name: RCLONE_CONFIG_CONTENT" -ForegroundColor White
                Write-Host "   4. Secret: Ctrl+V basın (clipboard-dan yapışdırılacaq)" -ForegroundColor White
                Write-Host "   5. 'Add secret' basın" -ForegroundColor White
                Write-Host ""
            } else {
                Write-Host "   ❌ Rclone konfiqurasiya faylı tapılmadı!" -ForegroundColor Red
            }
        }
    } else {
        Write-Host "   ⚠️  'googledrive' remote tapılmadı" -ForegroundColor Yellow
        Write-Host "   Konfiqurasiya etmək istəyirsiniz? (y/n): " -NoNewline
        $configRclone = Read-Host
        if ($configRclone -eq "y") {
            Write-Host "   📝 rclone config əmrini işə salın və təlimatları izləyin" -ForegroundColor Cyan
            rclone config
        }
    }
} catch {
    Write-Host "   ❌ Rclone quraşdırılmayıb!" -ForegroundColor Red
    Write-Host "   Quraşdırmaq istəyirsiniz? (y/n): " -NoNewline
    $installRclone = Read-Host
    if ($installRclone -eq "y") {
        winget install Rclone.Rclone
        Write-Host "   ✅ Rclone quraşdırıldı" -ForegroundColor Green
        Write-Host "   İndi konfiqurasiya edin: rclone config" -ForegroundColor Yellow
    }
}

Write-Host ""

# 8. Lokal test
Write-Host "8️⃣  Lokal test etmək istəyirsiniz? (y/n): " -NoNewline -ForegroundColor Cyan
$doTest = Read-Host

if ($doTest -eq "y") {
    Write-Host ""
    Write-Host "   🧪 Konfiqurasiya testi..." -ForegroundColor Cyan
    python test_config.py
    
    Write-Host ""
    Write-Host "   ▶️  Musiqi yükləməni başlatmaq istəyirsiniz? (y/n): " -NoNewline
    $doRun = Read-Host
    
    if ($doRun -eq "y") {
        python main.py
    }
}

Write-Host ""
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host "✅ QURAŞDIRMA TAMAMLANDI!" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""
Write-Host "📝 NÖVBƏT ADDIMLAR:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. GitHub Secrets əlavə edin:" -ForegroundColor White
Write-Host "   https://github.com/tuncay005-png/Apple_music/settings/secrets/actions" -ForegroundColor Blue
Write-Host ""
Write-Host "   Lazım olan 6 secret:" -ForegroundColor White
Write-Host "   - YANDEX_TOKEN" -ForegroundColor Gray
Write-Host "   - YANDEX_PLAYLIST_ID" -ForegroundColor Gray
Write-Host "   - YOUTUBE_PLAYLIST_ID" -ForegroundColor Gray
Write-Host "   - RCLONE_CONFIG_CONTENT" -ForegroundColor Gray
Write-Host "   - RCLONE_REMOTE_NAME" -ForegroundColor Gray
Write-Host "   - RCLONE_REMOTE_PATH" -ForegroundColor Gray
Write-Host ""
Write-Host "2. İlk workflow-u işə salın:" -ForegroundColor White
Write-Host "   https://github.com/tuncay005-png/Apple_music/actions" -ForegroundColor Blue
Write-Host "   'Run workflow' düyməsinə basın" -ForegroundColor White
Write-Host ""
Write-Host "📖 Ətraflı təlimat: SETUP_GUIDE_TUNCAY.md" -ForegroundColor Cyan
Write-Host ""
Write-Host "🎉 Uğurlar! 🎵" -ForegroundColor Green
