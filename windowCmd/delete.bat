@echo off
cd ..
del /f env.txt
del /f runtime.txt
del /f Pipfile
del /f Pipfile.lock
del /f Procfile
RMDIR /Q/S src
RMDIR /Q/S Files
RMDIR /Q/S __pycache__
del /f eSpace[lazy].7z
7z -t7z -mmt8 -mx9 a eSpace[lazy].7z -x!.git
