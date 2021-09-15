## Django Quick
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rshnGhost/django-quick?style=plastic)
![GitHub branch checks state](https://img.shields.io/github/checks-status/rshnGhost/django-quick/django-3.2.5?style=plastic)
![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/rshnGhost/django-quick/powerShell/django-3.2.5?style=plastic)

A simple django with ssl, project which should be exended to future website as needed.

## Requirements
Python 3.9

## Installation (Windows)
Double click on install.bat (should have internet connection)

## Setup (Windows)
Double click on setup.bat (should have internet connection)

Fill all credentials in the Notepad that pops up.

Give the details for superuser to be created.

## Usage (Windows)
Double click on run.bat

open browser and goto https://127.0.0.1:8000/

## Usage (Windows)[powershell]
```markdown
Get-ExecutionPolicy
```

```markdown
Set-ExecutionPolicy Bypass -Scope Process
```

```markdown
iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/JRqZX'))
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
