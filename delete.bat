del /f env.txt
del /f runtime.txt
del /f Pipfile
del /f Pipfile.lock
del /f Procfile
RMDIR /Q/S src
RMDIR /Q/S Files
RMDIR /Q/S __pycache__
