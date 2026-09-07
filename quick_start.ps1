# Quick Start Script - Simple Version
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   QUICK SETUP" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. Check Git
Write-Host "1. Checking Git..." -ForegroundColor Cyan
try {
    $gitVersion = git --version
    Write-Host "   OK: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "   ERROR: Git not found!" -ForegroundColor Red
    Write-Host "   Install: winget install Git.Git" -ForegroundColor Yellow
    exit 1
}
Write-Host ""

# 2. Install Python packages
Write-Host "2. Installing Python packages..." -ForegroundColor Cyan
pip install -r requirements.txt --quiet
Write-Host "   OK: Packages installed" -ForegroundColor Green
Write-Host ""

# 3. Test configuration
Write-Host "3. Testing configuration..." -ForegroundColor Cyan
python test_config.py
Write-Host ""

# 4. Git push option
Write-Host "4. Push to GitHub? (y/n): " -NoNewline -ForegroundColor Cyan
$doPush = Read-Host

if ($doPush -eq "y") {
    Write-Host ""
    Write-Host "   Initializing Git..." -ForegroundColor Cyan
    
    if (Test-Path ".git") {
        Write-Host "   Git already initialized" -ForegroundColor Yellow
    } else {
        git init
        Write-Host "   OK: Git initialized" -ForegroundColor Green
    }
    
    try {
        git remote remove origin 2>$null
    } catch {}
    
    git remote add origin https://github.com/tuncay005-png/Apple_music.git
    Write-Host "   OK: Remote added" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "   Adding files..." -ForegroundColor Cyan
    git add .
    
    Write-Host "   Creating commit..." -ForegroundColor Cyan
    git commit -m "Initial setup"
    
    Write-Host "   Pushing to GitHub..." -ForegroundColor Cyan
    git branch -M main
    
    try {
        git push -u origin main
        Write-Host "   OK: Pushed successfully!" -ForegroundColor Green
        Write-Host ""
        Write-Host "   Repository: https://github.com/tuncay005-png/Apple_music" -ForegroundColor Blue
    } catch {
        Write-Host "   ERROR: Push failed!" -ForegroundColor Red
        Write-Host ""
        Write-Host "   Try manual authentication:" -ForegroundColor Yellow
        Write-Host "   1. gh auth login" -ForegroundColor White
        Write-Host "   2. git push -u origin main" -ForegroundColor White
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   NEXT STEPS" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Setup Rclone:" -ForegroundColor Yellow
Write-Host "   winget install Rclone.Rclone" -ForegroundColor White
Write-Host "   rclone config" -ForegroundColor White
Write-Host ""
Write-Host "2. Get Base64 string:" -ForegroundColor Yellow
Write-Host '   $path = "$env:USERPROFILE\.config\rclone\rclone.conf"' -ForegroundColor White
Write-Host '   if (-not (Test-Path $path)) { $path = "$env:APPDATA\rclone\rclone.conf" }' -ForegroundColor White
Write-Host '   [Convert]::ToBase64String([IO.File]::ReadAllBytes($path)) | Set-Clipboard' -ForegroundColor White
Write-Host ""
Write-Host "3. Add GitHub Secrets:" -ForegroundColor Yellow
Write-Host "   https://github.com/tuncay005-png/Apple_music/settings/secrets/actions" -ForegroundColor Blue
Write-Host ""
Write-Host "4. See GITHUB_SECRETS_VALUES.txt for values" -ForegroundColor Yellow
Write-Host ""
