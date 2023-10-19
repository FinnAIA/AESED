@echo off
py -m pip install pycryptodome
py -m pip install --upgrade pycryptodome
py -m pip install tk
py -m pip install --upgrade tk
timeout /t 2 /NOBREAK >nul