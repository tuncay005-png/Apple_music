# Yandex Music token tapici
# Desktop proqraminin config faylinda token axtarir

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   YANDEX MUSIC TOKEN AXTAR" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Mumkin yollar
$paths = @(
    "$env:APPDATA\Yandex Music\config.json",
    "$env:APPDATA\Yandex.Music\config.json",
    "$env:LOCALAPPDATA\Yandex Music\config.json",
    "$env:LOCALAPPDATA\Programs\YandexMusic\config.json",
    "$env:USERPROFILE\AppData\Roaming\Yandex Music\config.json"
)

$found = $false

foreach ($path in $paths) {
    if (Test-Path $path) {
        Write-Host "OK: Config fayl tapildi!" -ForegroundColor Green
        Write-Host "Yol: $path" -ForegroundColor Yellow
        Write-Host ""
        
        $found = $true
        
        # Fayli oxu
        try {
            $content = Get-Content $path -Raw
            
            # Token axtar
            if ($content -match '"token":\s*"([^"]+)"') {
                $token = $matches[1]
                Write-Host "OK: Token tapildi!" -ForegroundColor Green
                Write-Host ""
                Write-Host "Token:" -ForegroundColor Yellow
                Write-Host $token -ForegroundColor White
                Write-Host ""
                
                # Clipboard-a kopyala
                $token | Set-Clipboard
                Write-Host "OK: Token clipboard-a kopyalandi!" -ForegroundColor Green
                Write-Host ""
                
                # Test et
                Write-Host "Token-i test etmek isteyirsiniz? (y/n): " -NoNewline
                $test = Read-Host
                
                if ($test -eq "y") {
                    Write-Host ""
                    Write-Host "Test edilir..." -ForegroundColor Cyan
                    python get_token_v2.py
                }
                
                break
            }
            elseif ($content -match '"access_token":\s*"([^"]+)"') {
                $token = $matches[1]
                Write-Host "OK: Access token tapildi!" -ForegroundColor Green
                Write-Host ""
                Write-Host "Token:" -ForegroundColor Yellow
                Write-Host $token -ForegroundColor White
                Write-Host ""
                
                $token | Set-Clipboard
                Write-Host "OK: Token clipboard-a kopyalandi!" -ForegroundColor Green
                Write-Host ""
                
                Write-Host "Token-i test etmek isteyirsiniz? (y/n): " -NoNewline
                $test = Read-Host
                
                if ($test -eq "y") {
                    Write-Host ""
                    Write-Host "Test edilir..." -ForegroundColor Cyan
                    python get_token_v2.py
                }
                
                break
            }
            else {
                Write-Host "XETA: Config faylda token tapilmadi" -ForegroundColor Red
                Write-Host "Fayli acmaq isteyirsiniz? (y/n): " -NoNewline
                $open = Read-Host
                
                if ($open -eq "y") {
                    notepad $path
                }
            }
        }
        catch {
            Write-Host "XETA: Fayl oxuna bilmedi: $_" -ForegroundColor Red
        }
        
        break
    }
}

if (-not $found) {
    Write-Host "XETA: Config fayl tapilmadi!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Mumkin sebeb:" -ForegroundColor Yellow
    Write-Host "  - Yandex Music desktop proqrami qurasdirilmayib" -ForegroundColor White
    Write-Host "  - Proqrama giris edilmeyib" -ForegroundColor White
    Write-Host ""
    Write-Host "Hell:" -ForegroundColor Yellow
    Write-Host "  1. https://music.yandex.ru/download/ - proqrami yukleyin" -ForegroundColor White
    Write-Host "  2. Proqrami acib giris edin" -ForegroundColor White
    Write-Host "  3. Bu skripti yeniden isle salin" -ForegroundColor White
    Write-Host ""
    
    # Manuel axtaris
    Write-Host "Manuel axtarmaq isteyirsiniz? (y/n): " -NoNewline
    $manual = Read-Host
    
    if ($manual -eq "y") {
        Write-Host ""
        Write-Host "Windows Explorer acilir..." -ForegroundColor Cyan
        Start-Process "explorer.exe" "$env:APPDATA"
        Write-Host ""
        Write-Host "'Yandex Music' qovlugunu tapib config.json faylini acin" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
