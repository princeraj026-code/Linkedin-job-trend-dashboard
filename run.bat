@echo off
REM Job Trends Analyzer - Quick Start Script for Windows
REM This script sets up and runs the complete pipeline

echo.
echo ========================================
echo   Job Trends Analyzer - Quick Start
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Verifying environment...
python src/verify_setup.py
if errorlevel 1 (
    echo.
    echo Environment verification failed!
    echo Please fix the issues above before continuing.
    pause
    exit /b 1
)

echo.
echo [2/4] Installing dependencies...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [3/4] Running data pipeline...
python src/run_pipeline.py
if errorlevel 1 (
    echo ERROR: Pipeline execution failed
    pause
    exit /b 1
)

echo.
echo [4/4] Starting Streamlit dashboard...
echo.
echo ========================================
echo   Dashboard will open in your browser
echo   Press Ctrl+C to stop the server
echo ========================================
echo.

streamlit run app/streamlit_app.py

pause
