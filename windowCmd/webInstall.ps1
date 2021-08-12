## iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/JRia7'))

function getAdmin {
	Add-Type -AssemblyName System.Windows.Forms
	[System.Windows.Forms.Application]::EnableVisualStyles()
	$ErrorActionPreference = 'SilentlyContinue'
	$Button = [System.Windows.MessageBoxButton]::YesNoCancel
	$ErrorIco = [System.Windows.MessageBoxImage]::Error
	$Ask = 'Do you want to run this as an Administrator?
        Select "Yes" to Run as an Administrator
        Select "No" to not run this as an Administrator
        Select "Cancel" to stop the script.'
	If (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]'Administrator')) {
		$Prompt = [System.Windows.MessageBox]::Show($Ask, "Run as an Administrator or not?", $Button, $ErrorIco) 
		Switch ($Prompt) {
			Yes {
				Write-Host "You didn't run this script as an Administrator. This script will self elevate to run as an Administrator and continue."
				Start-Process PowerShell.exe -ArgumentList ("-NoProfile -ExecutionPolicy Bypass -File `"{0}`"" -f $PSCommandPath) -Verb RunAs
				Exit
			}
			No {
				Break
			}
		}
	}
}

function getSha {
	$url = "https://api.github.com/repos/rshnGhost/django-quick/commits"
	$webData = Invoke-WebRequest -Uri $url -UseBasicParsing
	$releases = ConvertFrom-Json $webData.content
	return $releases.sha[0].substring(0, [System.Math]::Min(7, $releases.Length))
}

function deleteOldFolder {
	$statusFolder = Test-Path C:\Temp\$dName
	if ($statusFolder) {
		Write-Host -NoNewline "Deleting old Folder`t`t"
		Remove-Item C:\Temp\$dName -Recurse
		Write-Host "[Deleted old Files]"
	}
}

function setupProject {
	Write-Host "Executing..."
	cd "C:\Temp\$dName\$pName-$fName\windowCmd\"
	Write-Host "Setting up..."
    & "C:\Temp\$dName\$pName-$fName\windowCmd\2 setup.bat"
    Write-Host "Running..."
    & "C:\Temp\$dName\$pName-$fName\windowCmd\3 run.bat"
}

function expandZip {
	Write-Host -NoNewline "Expand Archive`t`t`t"
	Expand-Archive $output C:\Temp\$dName
	Write-Host "[Done]"
}

function installPython{
	Write-Host -NoNewline "Installing latest release`t"
	$args = '/passive', 'install', 'InstallAllUsers=1', 'PrependPath=1', 'Include_test=0'
	Start-Process -Wait $outputExe -ArgumentList $args
	Start-Process -Wait refreshenv
	Try{
		$er = (invoke-expression "python -V") 2>&1
		if ($lastexitcode) {throw $er}
		Write-Host "[Installed]"
	}
	Catch{
		Write-Host "[Not Installed]"
	}
}

getAdmin
$fName = 'django-3.2.5'
$pName = 'django-quick'
$sha = getSha
$dName = $pName+'-'+$sha
$output = "C:\Temp\$dName.zip"
$download = "https://github.com/rshnGhost/"+$pName+"/archive/refs/heads/"+$fName+".zip"
$pythonVersion = '3.9.6'
# Check if operating system architecture
Write-Host -NoNewline "Checking architecture`t`t"
if (($env:PROCESSOR_ARCHITECTURE -eq "AMD64") -and ([Environment]::Is64BitOperatingSystem)) {
	Write-Host "[64bit Found]"
	$url = "https://www.python.org/ftp/python/"+$pythonVersion+"/python-"+$pythonVersion+"-amd64.exe"
	$outputExe = "C:\Temp\python-"+$pythonVersion+"-amd64.exe"
}
else{
	Write-Host "[32bit Found]"
	$url = "https://www.python.org/ftp/python/"+$pythonVersion+"/python-"+$pythonVersion+".exe"
	$outputExe = "C:\Temp\python-"+$pythonVersion+".exe"
}

Try{
	# Check if pipenv is already installed
	Write-Host -NoNewline "Checking pipenv`t`t`t"
	$er = (invoke-expression "python -m pipenv --version") 2>&1
	if ($lastexitcode) {throw $er}
	Write-Host "[Found]"
	$pip = 1
}
Catch{
	Write-Host "[Not Found]"
	$pip = 0
	## checking python
	Write-Host -NoNewline "Checking python`t`t`t"
	Try{
		# Check if python is already installed
		$er = (invoke-expression "python -V") 2>&1
		if ($lastexitcode) {throw $er}
		Write-Host "[Found]"
		$python = 1
		Write-Host -NoNewline "Installing pipenv`t`t"
		Try{
			$er = (invoke-expression "python -m pip install pipenv") 2>&1
			if ($lastexitcode) {throw $er}
			Write-Host "[Done]"
		}
		Catch{
			Write-Host "[Failed]"
		}
	}
	Catch{
		Write-Host "[Not Found]"
		$python = 0
		$statusFile = Test-Path $output -PathType Leaf
		Write-Host -NoNewline "Checking latest release`t`t"
		If (!$statusFile){
			Write-Host "[File not Found]"
			Write-Host -NoNewline "Dowloading latest release`t"
			Invoke-WebRequest -Uri $url -OutFile $outputExe
			Write-Host "[Downloaded]"
			installPython
		}
		else{
			Write-Host "[File Found]"
			installPython
		}
		Try{
			Write-Host -NoNewline "Checking python`t`t`t"
			$er = (invoke-expression "python -V") 2>&1
			if ($lastexitcode) {throw $er}
			if (!$lastexitcode) {
				Write-Host "[Done]"
				Write-Host -NoNewline "Installing pipenv`t`t"
				$er = (invoke-expression "python -m pip install pipenv") 2>&1
				if ($lastexitcode) {throw $er}
				Write-Host "[Done]"
			}
		}
		Catch{
			Write-Host "[Failed]"
		}
	}
}
deleteOldFolder
Write-Host -NoNewline "Checking for file`t`t"
$statusFile = Test-Path $output -PathType Leaf
if (!$statusFile) {
	Write-Host "[File not Found]"
	Write-Host -NoNewline "Dowloading latest release`t"
	Invoke-WebRequest -Uri $download -OutFile $output
	$statusFile = Test-Path $output -PathType Leaf
	if (!$statusFile) {
		Write-Host "[Failed]"
		pause
		exit
	}
	if ($statusFile) {
		Write-Host "[Dowloaded]"
		expandZip
		setupProject
	}
}
if ($statusFile) {
	Write-Host "[File Found]"
	expandZip
	setupProject
}
