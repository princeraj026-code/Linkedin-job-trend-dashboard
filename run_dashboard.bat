@echo off
echo ========================================
echo Starting LinkedIn Job Trends Dashboard
echo ========================================
echo.
echo Dashboard will open in your browser at:
echo http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Activate virtual environment and run streamlit
call .venv\Scripts\activate.bat
python -c "import streamlit.web.cli as stcli; import sys; sys.argv = ['streamlit', 'run', 'app/streamlit_app.py']; sys.exit(stcli.main())"

pause
