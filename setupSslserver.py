import subprocess, os, re

def touch(file, content=''):
    lines=[]
    content = content.replace("\\n", "\n")
    lines = content.replace("\\t", "\t")
    with open(file, 'w') as fp:
        fp.writelines(lines)

def installRequirments(file=""):#python -m pipenv install -r requirments.txt
    if file == "":
        subprocess.run(['python', '-m', 'pipenv', 'install', '-r', 'requirments.txt'])
        os.system("python -m pipenv run pip freeze > requirments.txt")
    else:
        subprocess.run(['python', '-m', 'pipenv', 'install', '-r', file])
        os.system("python -m pipenv run pip freeze > "+file)
    #os.system("python -m pipenv run pip freeze > requirments.txt")
    #subprocess.run(['pipenv', 'install', '-r', 'requirments.txt'])
    #subprocess.run(['python', '-m', 'pipenv', 'run', 'pip', 'freeze', '>', 'requirments.txt'])

def install(package):#python -m pipenv install <name(s)>
    os.system("python -m pipenv install "+package)
    #subprocess.run(['pipenv', 'install', package])
    os.system("python -m pipenv run pip freeze > requirments.txt")
    #os.system("python -m pipenv run pip freeze > requirments.txt")
    #subprocess.run(['python', '-m', 'pipenv', 'run', 'pip', 'freeze', '>', 'requirments.txt'])

def createProject(name):#python -m pipenv run django-admin startproject <name>
    subprocess.run(['python', '-m', 'pipenv', 'run', 'django-admin', 'startproject', name])
    os.rename(name, 'src')
    touch(os.path.join("src", name, "password.py"), content="from credentials.credentials import credentials\n\ndef fetch(argument):\n    return credentials.get(argument)")
    lines = []
    with open(os.path.join("src", name, "settings.py"), 'r') as fp:
        lines = fp.readlines()
    index = lines.index('from pathlib import Path\n')
    lines[index] = "import os, sys\nfrom pathlib import Path\nfrom .password import fetch\n"

    index = lines.index("        'DIRS': [],\n")
    lines[index] = "\t\t'DIRS': [BASE_DIR / 'templates'],\n"

    index = lines.index('BASE_DIR = Path(__file__).resolve().parent.parent\n')
    lines[index] = "BASE_DIR = Path(__file__).resolve().parent.parent\nROOT_DIR = Path(__file__).resolve().parent.parent.parent\n"

    index = lines.index('# SECURITY WARNING: keep the secret key used in production secret!\n')
    lines[index+1] = "SECRET_KEY = fetch('secret_key')\n"

    index = lines.index("STATIC_URL = '/static/'\n")
    lines[index] = "STATIC_URL = '/static/'\nMEDIA_URL = '/media/'\nSTATICFILES_DIRS = [\n	BASE_DIR / 'static',\n	BASE_DIR / 'media',\n]\nSTATIC_ROOT = ROOT_DIR / 'Files/staticFile'\nMEDIA_ROOT = ROOT_DIR / 'Files/mediaFile'\n\nLOGIN_REDIRECT_URL = '/'\n"

    with open(os.path.join("src", name, "settings.py"), 'w') as fp:
        fp.writelines(lines)

def createApp(projName, appName):#python -m pipenv run django-admin startapp <name>
    os.chdir('src')
    subprocess.run(['python', '-m', 'pipenv', 'run', 'django-admin', 'startapp', appName])
    os.chdir('..')
    #registerApp(projName, appName)

def registerApp(projName, appName):#
    #os.chdir('src\'+projName)
    lines = []
    with open(os.path.join("src", projName, "settings.py"), 'r') as fp:
        lines = fp.readlines()
    indexS = lines.index('INSTALLED_APPS = [\n')
    indexE = lines.index(']\n')
    lines[indexE] = "\t'"+appName+"',\n"+lines[indexE]
    with open(os.path.join("src", projName, "settings.py"), 'w') as fp:
        fp.writelines(lines)
    #print(os.getcwd())

def makeFolder(folderName):#
    os.mkdir(folderName)

def setup():#
    subprocess.run(['python', '-m', 'pipenv', 'sync'])
    subprocess.run(['python', '-m', 'pipenv', 'run', 'python', os.path.join("src", "manage.py"), 'makemigrations'])
    subprocess.run(['python', '-m', 'pipenv', 'run', 'python', os.path.join("src", "manage.py"), 'migrate'])
    subprocess.run(['python', '-m', 'pipenv', 'run', 'python', os.path.join("src", "manage.py"), 'collectstatic'])
    print('Enter following details for root user')
    subprocess.run(['python', '-m', 'pipenv', 'run', 'python', os.path.join("src", "manage.py"), 'createsuperuser'])

def run(option):
    if option == "0":
        subprocess.run(['python', '-m', 'pipenv', 'run', 'python', os.path.join("src", "manage.py"), 'runserver'])
    elif option == "1":
        subprocess.run(['python', '-m', 'pipenv', 'run', 'python', os.path.join("src", "manage.py"), 'runsslserver'])

def setupUrl(name, appName):
    lines = []
    with open(os.path.join("src", name, "urls.py"), 'r') as fp:
        lines = fp.readlines()

    #index = lines.index("urlpatterns = [\n")
    #lines[index] = "\nfrom "+appName+" import urls\n\n"+lines[index]
    index = lines.index("]\n")
    lines[index] = "\tpath('', include('"+appName+".urls')),\n"+lines[index]

    index = lines.index("urlpatterns = [\n")
    lines[index] = "\nfrom django.conf.urls import include\n"+lines[index]

    with open(os.path.join("src", name, "urls.py"), 'w') as fp:
        fp.writelines(lines)

    lines = ["from django.urls import path",
            "\nfrom . import views",
            "\nfrom django.contrib.auth.decorators import login_required",
            "\napp_name = 'dataStorage'",
            "\nurlpatterns = [",
            "\n\t#path('/', login_required(iViews.familyList.as_view()), name='familyList'),",
            "\n\tpath('', views.home, name='home'),",
            "\n]"]
    with open(os.path.join("src", appName, "urls.py"), 'w') as fp:
        fp.writelines(lines)

    lines = ["from django.shortcuts import render",
    "\nfrom django.contrib import messages",
    "\nfrom django.urls import reverse, get_resolver",
    "\nfrom django.views.decorators.csrf import csrf_exempt",
    "\nfrom django.contrib.auth.decorators import login_required",
    "\n@login_required",
    "\ndef home(request):",
    "\n\tcontext = {}",
    "\n\tmessages.info(request, 'Information')",
    "\n\tmessages.success(request, 'Successful')",
    "\n\tmessages.warning(request, 'Warning')",
    "\n\treturn render(request, 'home.html', context)"]

    with open(os.path.join("src", appName, "views.py"), 'w') as fp:
        fp.writelines(lines)

def secure(name):
    lines = []
    with open(os.path.join("src", name, "settings.py"), 'r') as fp:
        lines = fp.readlines()
    lines[-1] = lines[-1]+"\nSECURE_HSTS_SECONDS = 10\nSECURE_SSL_REDIRECT = True\nSESSION_COOKIE_SECURE = True\n"
    lines[-1] = lines[-1]+"CSRF_COOKIE_SECURE = True\nSECURE_HSTS_INCLUDE_SUBDOMAINS = True\nSECURE_HSTS_PRELOAD = True"
    with open(os.path.join("src", name, "settings.py"), 'w') as fp:
        fp.writelines(lines)

def findReplaceAt(location, search, replace, option=0):
    lines = []
    search = search.replace("\\n", "\n")
    search = search.replace("\\t", "\t")
    search = search.replace("\(", "(")
    search = search.replace("\)", ")")
    replace = replace.replace("\\n", "\n")
    replace = replace.replace("\\t", "\t")
    replace = replace.replace("\(", "(")
    replace = replace.replace("\)", ")")
    with open(location, 'r') as fp:
        lines = fp.readlines()
    if option == 0:
        index = lines.index(search)
        lines[index] = replace + lines[index]
    elif option == 1:
        index = lines.index(search)
        lines[index] = replace

    with open(location, 'w') as fp:
        fp.writelines(lines)

def setupHeroku(name, ver=""):
    touch('Procfile', 'web: gunicorn --pythonpath src '+name+'.wsgi --log-file -')
    touch('env.txt', 'DISABLE_COLLECTSTATIC = 1')
    if ver == "":
        import platform
        version = str(platform.python_version())
        version = "python-"+version
        touch('runtime.txt', version)
    else:
        touch('runtime.txt', ver)
    findReplaceAt(os.path.join("src", name, "settings.py"), "    'django.middleware.security.SecurityMiddleware',\n", "\t'whitenoise.middleware.WhiteNoiseMiddleware',\n", 0)

def clean():
    for (dirpath, dirnames, filenames) in os.walk("src"):
        for filename in filenames:
            if filename.endswith('.py'):
                url = os.sep.join([dirpath, filename])
                try:
                    lines = []
                    with open(url, 'r') as fp:
                        lines = fp.readlines()
                        frm = lines.index('"""\n')
                        if frm == 0:
                            to = lines[frm+1:].index('"""\n')
                        else:
                            frm = lines.index('"""main URL Configuration\n')
                            if frm == 0:
                                to = lines[frm+1:].index('"""\n')
                    lines = lines[to+2:]

                    with open(url, 'w') as fp:
                        fp.writelines(lines)
                        #print(url)
                except:
                    pass

if __name__ == '__main__':
    touch('Pipfile')
    installRequirments()
    install('django')
    install('django-sslserver')
    install('django-registration-redux')
    install('django-crispy-forms')
    createProject('main')
    registerApp('main', 'sslserver')
    registerApp('main', 'registration')
    findReplaceAt(os.path.join("src", "main", "urls.py"), "]\n", "\tpath('accounts/', include('registration.backends.simple.urls')),\n")
    registerApp('main', 'crispy_forms')
    createApp('main', 'dataStorage')
    setupUrl('main', 'dataStorage')
    makeFolder(os.path.join("src", "media"))
    makeFolder(os.path.join("src", "static"))
    import shutil
    dest = shutil.copytree(os.path.join("temp", "static"), os.path.join("src", "static"))#, copy_function = shutil.copytree)
    dest = shutil.copytree(os.path.join("temp", "templates"), os.path.join("temp", "templates"))#, copy_function = shutil.copytree)
    makeFolder(os.path.join("src", "credentials"))
    touch(os.path.join("src", "credentials", "credentials.py"), 'credentials = {\n\t"email_username" : "optional",\n\t"email_password" : "optional",\n\t"postgresql_name" : "optional",\n\t"postgresql_username" : "optional",\n\t"postgresql_password" : "optional",\n\t"postgresql_host" : "optional",\n\t"postgresql_port" : "optional",\n\t"secret_key" : "required",\n\t"consumer_key" : "optional",\n\t"consumer_secret" : "optional",\n\t"access_token" : "optional",\n\t"access_token_secret" : "optional",\n}')
    print('Enter credentials in '+os.path.join("src", "credentials", "credentials.py"))
    os.system("notepad "+os.path.join("src", "credentials", "credentials.py"))
    os.system("pause")
    setup()
    setupHeroku('main')
    clean()
