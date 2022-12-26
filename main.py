import os
from setupSslserver import findReplaceAt

def setup_quick():
    os.system("python -m pipenv install")
    os.system("python -m pipenv shell")
    os.system("python main-setup.py --project main")
    os.system("python main-setup.py --cred")
    os.system("python main-setup.py --app main,dataStorage --reg main,dataStorage.apps.DatastorageConfig --url main,dataStorage")
    os.system("python main-setup.py --reg main,sslserver")
    os.system("python main-setup.py --reg main,registration")
    os.system("python main-setup.py --reg main,crispy_forms")
    os.system("python main-setup.py --reg main,rest_framework")
    os.system("python main-setup.py --reg main,rest_framework.authtoken")
    os.system("python main-setup.py --reg main,knox")
    os.system("python main-setup.py --copy temp/static,src/static --copy temp/templates,src/templates")
    # os.system("python main-setup.py --replace src/main/urls.py,]\n,\tpath\('accounts/',include\('registration.backends.simple.urls'\)\),\n")
    findReplaceAt(os.path.join("src", "main", "urls.py"), "]\n", "\tpath('accounts/', include('registration.backends.simple.urls')),\n")
    os.system("python main-setup.py --folder src/media")
    os.system("python main-setup.py --touch src/media/.nomedia")
    os.system("python main-setup.py --heroku main,python-3.11.1")
    os.system("python main-setup.py --clean")
    os.system("python main-setup.py --secure main")
    os.system("python main-setup.py --setup")
    os.system("python main-setup.py --signal dataStorage")
    try:
        shutil.rmtree("temp")
        shutil.rmtree("test")
        # os.remove("main.py")
        # os.remove("main-setup.py")
        # os.remove("setupSslserver.py")
        # os.remove("setup_heroku.py")
        # os.remove("setup-django-sslserver.py")
    except:
        pass
    os.system("python main-setup.py --run 2")

if __name__ == '__main__':
    setup_quick()
