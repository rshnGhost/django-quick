@echo off
cd ..
rem python main-setup.py --help
rem python main-setup.py --ireqfile <file_name>
python main-setup.py --touch Pipfile
python main-setup.py --install requirments.txt
rem python main-setup.py --package django-sslserver
rem python main-setup.py --package django-registration-redux
rem python main-setup.py --package django-crispy-forms
rem python main-setup.py --package whitenoise
rem python main-setup.py --package gunicorn
python main-setup.py --project main
python main-setup.py --cred
python main-setup.py --app main,dataStorage --reg main,dataStorage --url main,dataStorage
python main-setup.py --reg main,sslserver
python main-setup.py --reg main,registration
python main-setup.py --reg main,crispy_forms
python main-setup.py --copy temp/static,src/static --copy temp/templates,src/templates
python main-setup.py --replace src/main/urls.py,]\n,\tpath\('accounts/',include\('registration.backends.simple.urls'\)\),\n
python main-setup.py --folder src/media
python main-setup.py --touch src/media/.nomedia
python main-setup.py --heroku main,python-3.9.5
python main-setup.py --clean
python main-setup.py --setup --secure main
pause
