# ========================================
# LinkedIn Job Trends Dashboard Launcher
# ========================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "LinkedIn Job Trends Dashboard" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if virtual environment exists
if (-not (Test-Path ".venv\Scripts\Activate.ps1")) {
    Write-Host "ERROR: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run: python -m venv .venv" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✓ Virtual environment found" -ForegroundColor Green
Write-Host "✓ Starting dashboard...`n" -ForegroundColor Green

Write-Host "Dashboard will open at: " -NoNewline
Write-Host "http://localhost:8501`n" -ForegroundColor Yellow

Write-Host "Press Ctrl+C to stop the server`n" -ForegroundColor Gray
Write-Host "========================================`n" -ForegroundColor Cyan

# Activate venv and run streamlit
& .\.venv\Scripts\Activate.ps1
python -c "import streamlit.web.cli as stcli; import sys; sys.argv = ['streamlit', 'run', 'app/streamlit_app.py']; sys.exit(stcli.main())"
