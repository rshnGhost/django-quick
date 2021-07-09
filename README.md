## eSpace[lazy]
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
`iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/JcdHv'))`

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
