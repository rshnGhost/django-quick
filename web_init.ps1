powershell.exe -Command "InvokeWebRequest (https://github.com/rshnGhost/eSpace-lazy.git) -Outfile eSpace-lazy.zip"
powershell.exe -NoP -NonI -Command "Expand-Archive '.\eSpace-lazy.zip' '.\eSpace-lazy\'"
pause
