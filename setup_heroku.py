import subprocess, os

def touch(file, content=""):
    with open(file, 'w') as fp:
        fp.write(content)
        pass

def install(package):#python -m pipenv install <name(s)>
    subprocess.run(['python', '-m', 'pipenv', 'install', package])
    os.system("python -m pipenv run pip freeze > requirments.txt")
    #subprocess.run(['python', '-m', 'pipenv', 'run', 'pip', 'freeze', '>', 'requirments.txt'])

def setup(name):
    touch('Procfile', 'web: gunicorn --pythonpath src '+name+'.wsgi --log-file -')
    touch('env.txt', 'DISABLE_COLLECTSTATIC = 1')
    lines = []
    with open(os.path.join("src", name, "settings.py"), 'r') as fp:
        lines = fp.readlines()
    index = lines.index("    'django.middleware.security.SecurityMiddleware',\n")
    lines[index] = lines[index]+"\t'whitenoise.middleware.WhiteNoiseMiddleware',\n"
    with open(os.path.join("src", name, "settings.py"), 'w') as fp:
        fp.writelines(lines)


if __name__ == '__main__':
    install('whitenoise')
    install('gunicorn')
    setup('main')
