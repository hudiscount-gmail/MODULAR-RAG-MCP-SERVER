@echo off
setlocal

REM Activates the local venv in cmd.exe.
REM Usage: scripts\activate_venv.cmd

cd /d %~dp0\..

if not exist .venv\Scripts\activate.bat (
  echo [activate] .venv not found. Run: scripts\setup_venv.cmd
  exit /b 1
)

call .venv\Scripts\activate.bat
python -c "import sys; print('[activate] python:', sys.executable)"

endlocal
