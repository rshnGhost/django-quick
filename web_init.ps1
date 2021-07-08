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
Write-Host "Checking winget..."

# winget is not installed. Install it from the Github release
Write-Host "winget is not found, installing it right now."

$download = "https://github.com/rshnGhost/eSpace-lazy.git"
$output = $PSScriptRoot + "\eSpace-lazy.zip"
Write-Host "Dowloading latest release"
Invoke-WebRequest -Uri $download -OutFile $output
Expand-Archive $output '.\eSpace-lazy\'
