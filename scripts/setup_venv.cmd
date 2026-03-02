@echo off
setlocal

REM Create venv and install dependencies.
REM Usage: scripts\setup_venv.cmd

cd /d %~dp0\..

if not exist .venv (
  echo [setup] Creating .venv ...
  python -m venv .venv
) else (
  echo [setup] .venv already exists.
)

echo [setup] Activating .venv ...
call .venv\Scripts\activate.bat

echo [setup] Upgrading pip ...
python -m pip install --upgrade pip

if exist requirements.txt (
  echo [setup] Installing requirements.txt ...
  python -m pip install -r requirements.txt
) else (
  echo [setup] requirements.txt not found, skipping.
)

echo [setup] Done.
python -c "import sys; print('[setup] python:', sys.executable)"
endlocal
