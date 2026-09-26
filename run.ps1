<#
.SYNOPSIS
    1-Click Windows PowerShell launcher for PocketSmart AI.
.DESCRIPTION
    Delegates execution to 05_Project_Development, creates virtual environment if missing,
    installs requirements, and launches the FastAPI application server.
#>

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$DevDir = Join-Path $ScriptDir "05_Project_Development"
$VenvPython = Join-Path $DevDir "venv\Scripts\python.exe"

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "          PocketSmart AI - Context-Aware Budgeting Platform            " -ForegroundColor Yellow
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

Set-Location $DevDir

if (-not (Test-Path $VenvPython)) {
    Write-Host "[INFO] Creating virtual environment in 05_Project_Development\venv..." -ForegroundColor Green
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Error "[ERROR] Python virtual environment creation failed. Ensure Python 3.10+ is in PATH."
        exit 1
    }
    Write-Host "[INFO] Installing dependencies from requirements.txt..." -ForegroundColor Green
    & $VenvPython -m pip install --upgrade pip
    & $VenvPython -m pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Error "[ERROR] Failed to install dependencies."
        exit 1
    }
}

Write-Host "[INFO] Starting PocketSmart AI Server..." -ForegroundColor Green
Write-Host "[INFO] Local URL: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "[INFO] API Docs:  http://127.0.0.1:8000/docs" -ForegroundColor Cyan
Write-Host ""

& $VenvPython run_server.py
