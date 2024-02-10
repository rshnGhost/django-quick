## Django Quick
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rshnGhost/django-quick?style=plastic)
![GitHub branch checks state](https://img.shields.io/github/checks-status/rshnGhost/django-quick/django-5.0.2?style=plastic)
[![powerShell](https://github.com/rshnGhost/django-quick/actions/workflows/powershell-app.yml/badge.svg)](https://github.com/rshnGhost/django-quick/actions/workflows/powershell-app.yml)

A simple django with ssl, project which should be exended to future website as needed.

## Requirements
Python 3.11.1

## Installation (Windows)
Double click on install.bat (should have internet connection)

## Setup (Windows)
Double click on setup.bat (should have internet connection)

Fill all credentials in the Notepad that pops up.

Give the details for superuser to be created.

## Usage (Windows)
Double click on run.bat

open browser and goto https://127.0.0.1:8000/

## Usage (Windows)[powershell] (obsolete)
```markdown
Get-ExecutionPolicy
```

```markdown
Set-ExecutionPolicy Bypass -Scope Process
```

```markdown
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/rshnGhost/django-quick/django-5.0.2/windowCmd/webInstall.ps1'))
```

```markdown
iwr -useb https://raw.githubusercontent.com/rshnGhost/django-quick/django-5.0.2/windowCmd/webInstall.ps1 | iex
```

```markdown
iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/JRqZX'))
```

## Using PyPI
[![Tests (ubuntu)](https://github.com/rshnGhost/django-space/actions/workflows/tests_ubuntu.yml/badge.svg)](https://github.com/rshnGhost/django-space/actions/workflows/tests_ubuntu.yml) [![Tests (windows)](https://github.com/rshnGhost/django-space/actions/workflows/tests_windows.yml/badge.svg)](https://github.com/rshnGhost/django-space/actions/workflows/tests_windows.yml)

```markdown
pip install django-space
```

```markdown
django-space
```

## Credential
### Username
```markdown
django
```
### Password
```markdown
space
```

## Addons
open src/urls.py in your editor.

# import your app urls
from myapp import urls

# include your app urls
urlpatterns = [

...

url(r'^myapp/', include('myapp.urls')),

...

]

Enjoy :)
