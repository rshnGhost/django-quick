@echo off
rem powerShell.exe -NoProfile -Command "& {Start-Process powerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -WorkingDirectory '%~dp0' -Verb RunAs}"
powershell.exe -ExecutionPolicy Bypass -File %~dp0%~n0.ps1 -Verb RunAs
pause
