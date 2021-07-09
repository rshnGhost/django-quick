Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

$ErrorActionPreference = 'SilentlyContinue'
$wshell = New-Object -ComObject Wscript.Shell
$Button = [System.Windows.MessageBoxButton]::YesNoCancel
$ErrorIco = [System.Windows.MessageBoxImage]::Error
If (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]'Administrator')) {
	Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
	Exit
}

# GUI Specs
Write-Host "Checking for file..."
$status = Test-Path C:\Temp\django-3.2.5.zip -PathType Leaf
if($status == False) {
  Try{
    $download = "https://github.com/rshnGhost/eSpace-lazy/archive/refs/heads/django-3.2.5.zip"
    $output = "C:\Temp\eSpace-lazy-django-3.2.5.zip"
    Write-Host "Dowloading latest release"
    Invoke-WebRequest -Uri $download -OutFile $output
    Write-Output "Path of the file : $output"
    Write-Host "Expand Archive..."
    Expand-Archive $output 'C:\Temp\'
    # Executing
    cd 'C:\Temp\eSpace-lazy-django-3.2.5\windowCmd\'
    & 'C:\Temp\eSpace-lazy-django-3.2.5\windowCmd\2 setup.bat'
  }
  Catch{
    Write-Host "Someting is not working"
  }
}

if($status == True) {{
  # Executing
  cd 'C:\Temp\eSpace-lazy-django-3.2.5\windowCmd\'
  & 'C:\Temp\eSpace-lazy-django-3.2.5\windowCmd\2 setup.bat'
}
