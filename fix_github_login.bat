@echo off
echo ================================================
echo GITHUB LOGIN TROUBLESHOOTING
echo ================================================
echo.
echo This will help fix GitHub sign-in issues
echo.
pause

echo.
echo [1/4] Clearing DNS cache...
ipconfig /flushdns
timeout /t 2 >nul

echo.
echo [2/4] Opening GitHub in default browser...
start https://github.com/login
timeout /t 3 >nul

echo.
echo [3/4] Testing GitHub connectivity...
ping github.com -n 2
timeout /t 2 >nul

echo.
echo [4/4] Opening Streamlit Cloud...
start https://share.streamlit.io/
timeout /t 2 >nul

echo.
echo ================================================
echo TROUBLESHOOTING COMPLETE
echo ================================================
echo.
echo Try signing in now!
echo.
echo If still having issues:
echo   1. Wait 5-10 minutes (GitHub server issue)
echo   2. Try incognito/private browsing mode
echo   3. Use a different browser
echo   4. Check https://www.githubstatus.com/
echo.
pause
