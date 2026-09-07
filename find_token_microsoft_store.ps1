# Yandex Music (Microsoft Store) token tapici

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   YANDEX MUSIC TOKEN (MS STORE)" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Microsoft Store app yollari
$storePaths = @(
    "$env:LOCALAPPDATA\Packages\A025C540.Yandex.Music*\LocalState\config.json",
    "$env:LOCALAPPDATA\Packages\A025C540.Yandex.Music*\RoamingState\config.json",
    "$env:LOCALAPPDATA\Packages\A025C540.Yandex.Music*\Settings\config.json",
    "$env:LOCALAPPDATA\Packages\*Yandex.Music*\LocalState\config.json",
    "$env:LOCALAPPDATA\Packages\*Yandex*Music*\LocalState\*.json"
)

Write-Host "Microsoft Store Yandex Music qovluqları axtarılır..." -ForegroundColor Cyan
Write-Host ""

$found = $false

foreach ($pattern in $storePaths) {
    $files = Get-ChildItem -Path (Split-Path $pattern) -Filter (Split-Path $pattern -Leaf) -Recurse -ErrorAction SilentlyContinue 2>$null
    
    foreach ($file in $files) {
        if (Test-Path $file.FullName) {
            Write-Host "✅ Fayl tapıldı: $($file.FullName)" -ForegroundColor Green
            Write-Host ""
            
            $found = $true
            
            try {
                $content = Get-Content $file.FullName -Raw
                
                # Token axtar - muxtəlif formatlar
                $tokenPatterns = @(
                    '"token":\s*"([^"]+)"',
                    '"access_token":\s*"([^"]+)"',
                    '"accessToken":\s*"([^"]+)"',
                    '"oauth_token":\s*"([^"]+)"',
                    '"authToken":\s*"([^"]+)"'
                )
                
                $tokenFound = $false
                
                foreach ($pattern in $tokenPatterns) {
                    if ($content -match $pattern) {
                        $token = $matches[1]
                        
                        if ($token -and $token.Length -gt 20) {
                            Write-Host "✅ TOKEN TAPILDI!" -ForegroundColor Green
                            Write-Host ""
                            Write-Host "Token:" -ForegroundColor Yellow
                            Write-Host $token -ForegroundColor White
                            Write-Host ""
                            
                            # Clipboard-a kopyala
                            $token | Set-Clipboard
                            Write-Host "✅ Token clipboard-a kopyalandı!" -ForegroundColor Green
                            Write-Host ""
                            
                            $tokenFound = $true
                            break
                        }
                    }
                }
                
                if (-not $tokenFound) {
                    Write-Host "⚠️  Faylda token tapılmadı" -ForegroundColor Yellow
                    Write-Host "Faylı açmaq istəyirsiniz? (y/n): " -NoNewline
                    $open = Read-Host
                    if ($open -eq "y") {
                        notepad $file.FullName
                    }
                }
                
            }
            catch {
                Write-Host "❌ Fayl oxuna bilmədi: $_" -ForegroundColor Red
            }
        }
    }
}

if (-not $found) {
    Write-Host "❌ Microsoft Store Yandex Music qovluğu tapılmadı" -ForegroundColor Red
    Write-Host ""
    Write-Host "Manuel axtarış..." -ForegroundColor Yellow
    
    # Packages qovlugunu ac
    $packagesPath = "$env:LOCALAPPDATA\Packages"
    
    if (Test-Path $packagesPath) {
        Write-Host ""
        Write-Host "Packages qovluğu açılır..." -ForegroundColor Cyan
        Write-Host "Yandex ilə başlayan qovluğu tapın" -ForegroundColor Yellow
        
        Start-Process "explorer.exe" $packagesPath
    }
    
    Write-Host ""
    Write-Host "💡 Alternativ: Yandex Music proqramını açın" -ForegroundColor Cyan
    Write-Host "   Sonra bu skripti yenidən işə salın" -ForegroundColor White
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "ƏGƏR TOKEN TAPILSA:" -ForegroundColor Yellow
Write-Host "  python get_token_v2.py" -ForegroundColor White
Write-Host "  (Token clipboard-dadır, Ctrl+V basın)" -ForegroundColor Gray
Write-Host ""
