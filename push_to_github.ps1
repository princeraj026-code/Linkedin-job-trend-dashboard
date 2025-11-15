# ========================================
# GitHub Push Setup Script (PowerShell)
# Repository: Linkedin-job-trend-dashboard
# Username: princeraj026-code
# ========================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "GitHub Push Setup Script" -ForegroundColor Cyan
Write-Host "Repository: Linkedin-job-trend-dashboard" -ForegroundColor Cyan
Write-Host "Username: princeraj026-code" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Navigate to project directory
Set-Location "N:\Hackathon\Job-Trend"

# Find Git executable
$gitPaths = @(
    "C:\Program Files\Git\cmd\git.exe",
    "C:\Program Files (x86)\Git\cmd\git.exe",
    "$env:LOCALAPPDATA\Programs\Git\cmd\git.exe",
    "C:\Git\cmd\git.exe"
)

$gitExe = $null
foreach ($path in $gitPaths) {
    if (Test-Path $path) {
        $gitExe = $path
        Write-Host "✓ Git found at: $path`n" -ForegroundColor Green
        break
    }
}

if (-not $gitExe) {
    Write-Host "ERROR: Git not found!" -ForegroundColor Red
    Write-Host "`nPlease install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "After installation, restart PowerShell and run this script again.`n" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Create alias for git command
Set-Alias -Name git -Value $gitExe -Scope Script

try {
    Write-Host "Step 1: Configuring Git user..." -ForegroundColor Yellow
    & $gitExe config --global user.name "princeraj026-code"
    & $gitExe config --global user.email "rajputprincesingh026@gmail.com"
    Write-Host "✓ Git user configured`n" -ForegroundColor Green

    Write-Host "Step 2: Initializing Git repository..." -ForegroundColor Yellow
    & $gitExe init
    Write-Host "✓ Repository initialized`n" -ForegroundColor Green

    Write-Host "Step 3: Adding all files..." -ForegroundColor Yellow
    & $gitExe add .
    Write-Host "✓ Files staged`n" -ForegroundColor Green

    Write-Host "Step 4: Creating initial commit..." -ForegroundColor Yellow
    & $gitExe commit -m "Initial commit: LinkedIn Job Trends Dashboard with AI features"
    Write-Host "✓ Commit created`n" -ForegroundColor Green

    Write-Host "Step 5: Setting branch to main..." -ForegroundColor Yellow
    & $gitExe branch -M main
    Write-Host "✓ Branch set to main`n" -ForegroundColor Green

    Write-Host "Step 6: Adding remote repository..." -ForegroundColor Yellow
    & $gitExe remote add origin https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git
    Write-Host "✓ Remote repository added`n" -ForegroundColor Green

    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "AUTHENTICATION REQUIRED" -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "GitHub will ask for authentication. Use one of these:" -ForegroundColor White
    Write-Host "`n1. Personal Access Token (RECOMMENDED):" -ForegroundColor Green
    Write-Host "   - Go to: https://github.com/settings/tokens" -ForegroundColor White
    Write-Host "   - Click 'Generate new token (classic)'" -ForegroundColor White
    Write-Host "   - Select scope: 'repo' (full control)" -ForegroundColor White
    Write-Host "   - Copy the token" -ForegroundColor White
    Write-Host "   - When prompted for password, paste the TOKEN (not your GitHub password)" -ForegroundColor White
    Write-Host "`n2. GitHub CLI:" -ForegroundColor Green
    Write-Host "   - Install: winget install --id GitHub.cli" -ForegroundColor White
    Write-Host "   - Run: gh auth login" -ForegroundColor White
    Write-Host "`n3. GitHub Desktop (EASIEST):" -ForegroundColor Green
    Write-Host "   - Download: https://desktop.github.com/" -ForegroundColor White
    Write-Host "   - Sign in and add this repository`n" -ForegroundColor White
    Write-Host "========================================`n" -ForegroundColor Cyan

    Write-Host "Step 7: Pushing to GitHub..." -ForegroundColor Yellow
    & $gitExe push -u origin main

    Write-Host "`n========================================" -ForegroundColor Green
    Write-Host "✓ SUCCESS! Your code is on GitHub!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "`nView your repository at:" -ForegroundColor White
    Write-Host "https://github.com/princeraj026-code/Linkedin-job-trend-dashboard`n" -ForegroundColor Cyan

} catch {
    Write-Host "`n❌ ERROR: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "`nIf you see authentication errors, please set up authentication first." -ForegroundColor Yellow
}

Write-Host "`nPress Enter to exit..." -ForegroundColor Gray
Read-Host
