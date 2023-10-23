@echo off
title pip_installer.bat
py -m pip install pycryptodome
py -m pip install --upgrade pycryptodome
py -m pip install tk
py -m pip install --upgrade tk
echo INFO -- You can close the program now!
timeout /t 10 /NOBREAK >nul
exit
