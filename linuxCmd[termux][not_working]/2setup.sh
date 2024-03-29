python main-setup.py --touch Pipfile
python main-setup.py --install requirments.txt
python main-setup.py --project main
python main-setup.py --cred
python main-setup.py --app main,dataStorage
python main-setup.py --reg main,dataStorage
python main-setup.py --reg main,sslserver
python main-setup.py --reg main,registration
python main-setup.py --reg main,crispy_forms
python main-setup.py --url main,dataStorage
python main-setup.py --copy temp/static,src/static
python main-setup.py --copy temp/templates,src/templates
python main-setup.py --replace src/main/urls.py,]\\n,\\tpath\(\'accounts/\',include\(\'registration.backends.simple.urls\'\)\),\\n
python main-setup.py --folder src/media
python main-setup.py --heroku main,python-3.9.5
python main-setup.py --clean
python main-setup.py --setup --secure main
