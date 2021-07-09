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

Try{
  $download = "https://github.com/rshnGhost/eSpace-lazy/archive/refs/heads/django-3.2.5.zip"
  $output = $PSScriptRoot + "\django-3.2.5.zip"
  Write-Host "Dowloading latest release"
  Invoke-WebRequest -Uri $download -OutFile $output
  Write-Output "Path of the file : $output"
  Write-Output "Path of the script : $PSScriptRoot"
}
Catch{
	Write-Host "Someting is not working"
}
Finally {
	# Start installing the packages with winget
	#Get-Content .\winget.txt | ForEach-Object {
	#	iex ("winget install -e " + $_)
	#}
}
