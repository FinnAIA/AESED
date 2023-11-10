@echo off
title pip installer.bat
py -m pip install --upgrade pip
py -m pip install pycryptodome
py -m pip install tk
timeout /t 5 /NOBREAK >nul
exit