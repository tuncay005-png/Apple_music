@echo off
chcp 65001 >nul
echo.
echo 🎵 YouTube Mahnılarını Yüklə
echo ================================
echo.

cd /d "%~dp0"

REM Virtual environment aktivləşdir
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo ⚠️ Virtual environment tapılmadı!
    echo Əvvəlcə: python -m venv venv
    pause
    exit /b 1
)

REM YouTube-dan yüklə
echo 📥 YouTube-dan yüklənir...
python -c "import os; os.environ['YANDEX_TOKEN']='SKIP'; from main import MusicDownloader; d=MusicDownloader(); print(f'✅ {d.download_from_youtube()} mahnı yükləndi')"

echo.
echo 📁 Fayllar: downloads\
dir downloads\ /b

echo.
echo ✅ Hazır! İndi faylları Google Drive-a köçürün:
echo    https://drive.google.com/drive/folders/1P6xoCpHS3zFPAMqDICcZN3vK33_1WH_P
echo.
pause
