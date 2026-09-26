@echo off
setlocal enabledelayedexpansion

title PocketSmart AI - 1-Click Windows Launcher

echo ======================================================================
echo           PocketSmart AI - Context-Aware Budgeting Platform
echo ======================================================================
echo.

cd /d "%~dp005_Project_Development"

if not exist "venv\Scripts\python.exe" (
    echo [INFO] Virtual environment not detected. Creating venv in 05_Project_Development\venv...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment. Ensure Python 3.10+ is installed and on PATH.
        pause
        exit /b 1
    )
    echo [INFO] Installing required dependencies...
    venv\Scripts\python.exe -m pip install --upgrade pip
    venv\Scripts\python.exe -m pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install dependencies.
        pause
        exit /b 1
    )
)

echo [INFO] Starting PocketSmart AI Server...
echo [INFO] Open your browser to: http://127.0.0.1:8000
echo.
venv\Scripts\python.exe run_server.py

pause
