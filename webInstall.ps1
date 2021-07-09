If (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]'Administrator')) {
	Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
	Exit
}

# GUI Specs
Write-Host "Checking for file..."
$status = Test-Path C:\Temp\django-3.2.5.zip -PathType Leaf
If (!$status) {
  Try{
    $download = "https://github.com/rshnGhost/eSpace-lazy/archive/refs/heads/django-3.2.5.zip"
    $output = "C:\Temp\eSpace-lazy-django-3.2.5.zip"
    Write-Host "Dowloading latest release"
    Invoke-WebRequest -Uri $download -OutFile $output
    Write-Output "Path of the file : $output"
    Write-Host "Expand Archive..."
    Expand-Archive $output 'C:\Temp\'
    Write-Host "Executing..."
    cd 'C:\Temp\eSpace-lazy-django-3.2.5\windowCmd\'
    & 'C:\Temp\eSpace-lazy-django-3.2.5\windowCmd\2 setup.bat'
  }
  Catch{
    Write-Host "Someting is not working"
  }
}

If ($status) {
  Write-Host "Executing..."
  cd 'C:\Temp\eSpace-lazy-django-3.2.5\windowCmd\'
  & 'C:\Temp\eSpace-lazy-django-3.2.5\windowCmd\2 setup.bat'
}
