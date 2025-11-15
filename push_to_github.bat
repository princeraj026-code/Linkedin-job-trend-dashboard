@echo off
echo ========================================
echo GitHub Push Setup Script
echo Repository: Linkedin-job-trend-dashboard
echo Username: princeraj026-code
echo ========================================
echo.

REM Set Git path (update if Git is installed elsewhere)
set GIT_PATH=C:\Program Files\Git\cmd\git.exe

REM Check if Git exists
if exist "%GIT_PATH%" (
    echo Git found at: %GIT_PATH%
) else (
    echo ERROR: Git not found!
    echo Please install Git from: https://git-scm.com/download/win
    echo After installation, restart this terminal and run this script again.
    pause
    exit /b 1
)

echo.
echo Step 1: Configuring Git user...
"%GIT_PATH%" config --global user.name "princeraj026-code"
"%GIT_PATH%" config --global user.email "rajputprincesingh026@gmail.com"
echo ✓ Git user configured

echo.
echo Step 2: Initializing Git repository...
"%GIT_PATH%" init
echo ✓ Repository initialized

echo.
echo Step 3: Adding all files...
"%GIT_PATH%" add .
echo ✓ Files staged

echo.
echo Step 4: Creating initial commit...
"%GIT_PATH%" commit -m "Initial commit: LinkedIn Job Trends Dashboard with AI features"
echo ✓ Commit created

echo.
echo Step 5: Setting branch to main...
"%GIT_PATH%" branch -M main
echo ✓ Branch set to main

echo.
echo Step 6: Adding remote repository...
"%GIT_PATH%" remote add origin https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git
echo ✓ Remote repository added

echo.
echo Step 7: Pushing to GitHub...
echo NOTE: GitHub will ask for authentication!
echo Use one of these methods:
echo   1. Personal Access Token (recommended)
echo   2. GitHub Desktop
echo   3. GitHub CLI (gh auth login)
echo.
"%GIT_PATH%" push -u origin main

echo.
echo ========================================
echo ✓ DONE! Check your repository at:
echo https://github.com/princeraj026-code/Linkedin-job-trend-dashboard
echo ========================================
pause
