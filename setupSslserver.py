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
    lines[index] = lines[index]+"ROOT_DIR = Path(__file__).resolve().parent.parent.parent\n"

    index = lines.index('# SECURITY WARNING: keep the secret key used in production secret!\n')
    lines[index+1] = "SECRET_KEY = fetch('secret_key')\n"

    index = lines.index("STATIC_URL = '/static/'\n")
    #lines[index] = "STATIC_URL = '/static/'\nMEDIA_URL = '/media/'\nSTATICFILES_DIRS = [\n	BASE_DIR / 'static',\n	BASE_DIR / 'media',\n]\nSTATIC_ROOT = ROOT_DIR / 'Files/staticFile'\nMEDIA_ROOT = ROOT_DIR / 'Files/mediaFile'\n\nLOGIN_REDIRECT_URL = '/'\n"
    lines[index] = lines[index]+"MEDIA_URL = '/media/'\n"
    lines[index] = lines[index]+"STATICFILES_DIRS = [\n\tBASE_DIR / 'static',\n"
    lines[index] = lines[index]+"\tBASE_DIR / 'media',\n]\n"
    lines[index] = lines[index]+"STATIC_ROOT = ROOT_DIR / 'Files/staticFile'\n"
    lines[index] = lines[index]+"MEDIA_ROOT = ROOT_DIR / 'Files/mediaFile'\n"
    lines[index] = lines[index]+"\nLOGIN_REDIRECT_URL = '/'\n"
    lines[index] = lines[index]+"SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'\n"
    lines[index] = lines[index]+"SESSION_EXPIRE_AT_BROWSER_CLOSE = True\n"
    lines[index] = lines[index]+"CRISPY_TEMPLATE_PACK = 'bootstrap4'"

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
    elif option == "2":
        subprocess.run(['python', '-m', 'pipenv', 'run', 'python', os.path.join("src", "manage.py"), 'runsslserver', '0.0.0.0:8000'])

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
            "\nfrom knox import views as knox_views",
            "\nurlpatterns = [",
            "\n\t#path('/', login_required(iViews.familyList.as_view()), name='familyList'),",
            "\n\tpath('', views.home, name='home'),",
            "\n\tpath('api/login/', views.KnoxLoginAPI.as_view(), name='api_login'),",
            "\n\tpath('api/rflogin/', views.RFLoginAPI.as_view(), name='api_login'),",
            "\n\tpath('api/home/', views.HomeView.as_view(), name='api_home'),",
            "\n\tpath('api/logout/', knox_views.LogoutView.as_view(), name='api_logout'),",
            "\n\tpath('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),",
            "\n]"]
    with open(os.path.join("src", appName, "urls.py"), 'w') as fp:
        fp.writelines(lines)

    lines = ["from django.shortcuts import render",
    "\nfrom django.contrib import messages",
    "\nfrom django.urls import reverse, get_resolver",
    "\nfrom django.views.decorators.csrf import csrf_exempt",
    "\nfrom django.contrib.auth.decorators import login_required",
    "\nfrom django.contrib.auth.signals import user_logged_out, user_logged_in, user_login_failed"
    "\nfrom django.dispatch import receiver"
    "\n",
    "\n@receiver(user_logged_out)",
    "\ndef on_user_logged_out(sender, request, **kwargs):",
    "\n\tmessages.info(request, '['+request.user.username+'] Logged out.')",
    "\n",
    "\n@receiver(user_logged_in)",
    "\ndef on_user_logged_in(sender, request, **kwargs):",
    "\n\tmessages.success(request, '['+request.user.username+'] Logged in.')",
    "\n",
    "\n@receiver(user_login_failed)",
    "\ndef on_user_login_failed(sender, request, **kwargs):",
    "\n\tmessages.warning(request, 'Logged in failed.')",
    "\n",
    "\n@login_required",
    "\ndef home(request):",
    "\n\tcontext = {}",
    "\n\t#messages.info(request, 'Information')",
    "\n\t#messages.success(request, 'Successful')",
    "\n\t#messages.warning(request, 'Warning')",
    "\n\treturn render(request, 'home.html', context)",
    "\n\nfrom rest_framework.views import APIView",
    "\nfrom rest_framework.response import Response",
    "\nfrom rest_framework.permissions import IsAuthenticated, AllowAny",
    "\nfrom rest_framework.authtoken.serializers import AuthTokenSerializer",
    "\nfrom knox.views import LoginView as KnoxLoginView",
    "\nfrom django.contrib.auth import login",
    "\nfrom knox.auth import TokenAuthentication",
    "\n",
    "\nclass KnoxLoginAPI(KnoxLoginView):",
    "\n\tpermission_classes = (AllowAny,)",
    "\n",
    "\n\tdef post(self, request, format=None):",
    "\n\t\tserializer = AuthTokenSerializer(data=request.data)",
    "\n\t\tserializer.is_valid(raise_exception=True)",
    "\n\t\tuser = serializer.validated_data['user']",
    "\n\t\tlogin(request, user)",
    "\n\t\treturn super(KnoxLoginAPI, self).post(request, format=None)",
    "\n",
    "\nfrom rest_framework.authtoken.views import ObtainAuthToken",
    "\nfrom rest_framework.authtoken.models import Token",
    "\nclass RFLoginAPI(ObtainAuthToken):",
    "\n",
    "\n	def post(self, request, *args, **kwargs):",
    "\n\t\tserializer = self.serializer_class(data=request.data, context={'request': request})",
    "\n\t\tserializer.is_valid(raise_exception=True)",
    "\n\t\tuser = serializer.validated_data['user']",
    "\n\t\ttoken, created = Token.objects.get_or_create(user=user)",
    "\n\t\tfrom knox.models import AuthToken",
    "\n\t\tknoxToken = AuthToken.objects.create(user)[1]",
    "\n\t\treturn Response({",
    "\n\t\t\t'token': token.key,",
    "\n\t\t\t'created': created,",
    "\n\t\t\t'knoxToken': knoxToken,",
    "\n\t\t})",
    "\n",
    "\nclass HomeView(APIView):",
    "\n\tauthentication_classes = [TokenAuthentication]",
    "\n",
    "\n\tdef get(self, request):",
    "\n\t\tcontent = {'message': 'Hello, World!'}",
    "\n\t\treturn Response(content)"]

    with open(os.path.join("src", appName, "views.py"), 'w') as fp:
        fp.writelines(lines)

def secure(name):
    lines = []
    with open(os.path.join("src", name, "settings.py"), 'r') as fp:
        lines = fp.readlines()
    lines[-1] = lines[-1]+"\nSECURE_HSTS_SECONDS = 10\nSECURE_SSL_REDIRECT = True\nSESSION_COOKIE_SECURE = True\n"
    lines[-1] = lines[-1]+"CSRF_COOKIE_SECURE = True\nSECURE_HSTS_INCLUDE_SUBDOMAINS = True\nSECURE_HSTS_PRELOAD = True"
    lines[-1] = lines[-1]+"\n# REST_FRAMEWORK = {\n#\t'DEFAULT_AUTHENTICATION_CLASSES':"
    lines[-1] = lines[-1]+"[\n#\t\t# 'rest_framework.authentication.TokenAuthentication',"
    lines[-1] = lines[-1]+"\n#\t\t'knox.auth.TokenAuthentication',\n#\t],\n# }"

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

def make_signal(name):
    lines = []
    with open(os.path.join("src", name, "apps.py"), 'r') as fp:
        lines = fp.readlines()

    lines = f"from django.apps import AppConfig\n\nclass {name.capitalize()}Config(AppConfig):\
        \n\tdefault_auto_field = 'django.db.models.BigAutoField'\
        \n\tname = '{name}'\
        \n\n\tdef ready(self):\
        \n\t\timport {name}.signals\n"

    with open(os.path.join("src", name, "apps.py"), 'w') as fp:
        fp.writelines(lines)

    lines = f"from django.db.models.signals import post_save\
        \nfrom django.dispatch import receiver\
        \nfrom django.conf import settings\
        \nfrom rest_framework.authtoken.models import Token\
        \n\n@receiver(post_save, sender=settings.AUTH_USER_MODEL)\
        \ndef updateOpenSearch(sender, instance, created, **kwargs):\
        \n\tif created:\
        \n\t\tToken.objects.create(user = instance)"

    with open(os.path.join("src", name, "signals.py"), 'w') as fp:
        fp.writelines(lines)

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
