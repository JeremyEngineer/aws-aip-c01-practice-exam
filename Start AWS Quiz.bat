@echo off
REM Double-click to start the AWS AIP-C01 practice quiz. It then opens in your browser.
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py app.py
  goto :end
)
where python >nul 2>nul
if %errorlevel%==0 (
  python app.py
  goto :end
)
echo Python 3 was not found.
echo Install it from https://www.python.org/downloads/ and tick "Add python.exe to PATH" during setup.
pause
:end
