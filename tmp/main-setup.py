import sys, getopt, shutil
from setupSslserver import *
#from setup_heroku import *

touchVar = []
packageVar = []
folderVar = []

def help():
    print("usage: "+os.path.basename(__file__)+" [--help] [--touch <file_name>,<optional_file_content>] [--install]\
    \n\t[--ireqfile <file_name>] [--package <package_name>] [--project <project_name>] [--cred]\
    \n\t[--app <application_name>] [--reg <project_name>,<application_name>] [--url <project_name>,<application_name>]\
    \n\t[--copy <source>,<destination>] [--replace <file_path>,<search_string>,<replace_string>] [--folder <folder_path>]\
    \n\t[--setup] [--run <option{0, 1}>] [--heroku <project_name>,<specfic_version>] [--clean]")
    file_name = os.path.basename(__file__)
    d = {
        "Help": [file_name+" --help", "", ""],
        "Create file": [file_name+" --touch", "<file_name>",",<optional_file_content>"],
        "Install Requirments from Requirments file": [file_name+" --install", "", ""],
        "Install Requirments from user Requirments file": [file_name+" --ireqfile", "<file_name>", ""],
        "Install Package": [file_name+" --package", "<package_name>", ""],
        "Create Project": [file_name+" --project", "<project_name>", ""],
        "Create Credentials File(default)": [file_name+" --cred", "", ""],
        "Create Application": [file_name+" --app", "<project_name>,<application_name>", ""],
        "Register Application": [file_name+" --reg", "<project_name>,<application_name>", ""],
        "Setup Application Url": [file_name+" --url", "<project_name>,<application_name>", ""],
        "Copy Directory": [file_name+" --copy", "<source>,<destination>", ""],
        "Find and Replace At": [file_name+" --replace", "<file_path>,<search_string>,<replace_string>", ""],
        "Create Folder": [file_name+" --folder", "<folder_path>", ""],
        "Run Setup": [file_name+" --setup", "", ""],
        "Run Server": [file_name+" --run", "<option{0, 1}>", ""],
        "Setup for Heroku": [file_name+" --heroku", "<project_name>",",<specfic_version>"],
        "Remove comments": [file_name+" --clean", "", ""]
    }
    print("{:<46} {:<24} {:<44} {:<6}".format('Action','Usage','Argument','Optional Argument'))
    for action, help in d.items():
        usage, argument, optional = help
        print("{:<46} {:<24} {:<44} {:6}".format(action, usage, argument, optional))
    '''
    print("Help:\t  "+os.path.basename(__file__)+" --help")
    print("Create file:\t  "+os.path.basename(__file__)+" --touch <file_name>,<file_content>")
    print("Install Requirments from Requirments file:\t  "+os.path.basename(__file__)+" --install")
    print("Install Requirments from user Requirments file:\t  "+os.path.basename(__file__)+" --ireqfile <file_name>")
    print("Install Package:\t  "+os.path.basename(__file__)+" --package <package_name>")
    print("Create Project:\t  "+os.path.basename(__file__)+" --project <project_name>")
    print("Create Credentials File(default):\t  "+os.path.basename(__file__)+" --cred")
    print("Create Application:\t  "+os.path.basename(__file__)+" --app <project_name>,<application_name>")
    print("Register Application:\t  "+os.path.basename(__file__)+" --reg <project_name>,<application_name>")
    #print("Setup Application Url:\t  "+os.path.basename(__file__)+" --url <project_name>,<application_name>")
    #print("Copy Directory:\t  "+os.path.basename(__file__)+" --copy <source>,<destination>")
    #findReplaceAt('src/main/urls.py', "]\n", "\tpath('accounts/', include('registration.backends.simple.urls')),\n")
    #print("Find and Replace At:\t  "+os.path.basename(__file__)+" --replace <file_path>,<search_string>,<replace_string>")
    print("Create Folder:\t  "+os.path.basename(__file__)+" --folder <folder_path>")
    print("Run Setup:\t  "+os.path.basename(__file__)+" --setup")
    print("Setup for Heroku:\t  "+os.path.basename(__file__)+" --heroku <project_name> ,<specfic_version>")
    print("Run Server:\t  "+os.path.basename(__file__)+" --run <option>")
    print("Remove comments:\t  "+os.path.basename(__file__)+" --clean")
    '''

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"",
                                    ["help","install","touch=","ireqfile=","package=","project=",
                                    "cred","app=","reg=","folder=","move=","setup","signal=",
                                    "run=","copy=","url=","replace=","secure=","heroku=","clean"]
                                    )
    except getopt.GetoptError:
        help()
        sys.exit(2)
    #print(len(opts))
    for opt, arg in opts:
        if opt == '--help':
            help()
            sys.exit()
        elif opt == "--touch":
            touchVar.append(arg)
        elif opt == '--install':
            installRequirments()
        elif opt == '--ireqfile':
            installRequirments(arg)
        elif opt == "--package":
            packageVar.append(arg)
        elif opt == "--project":
            createProject(arg)
        elif opt == "--cred":
            makeFolder(os.path.join("src", "credentials"))
            import secrets, string
            punctuation = "!#$%&()*+,-.:;<=>?@[]^_{|}~"
            secret_key = "".join(secrets.choice(string.digits + string.ascii_letters + punctuation)for i in range(100))
            touch(os.path.join("src", "credentials","credentials.py"),'credentials = {\n\t"secret_key" : "'+secret_key+'",\n}')
        elif opt == "--app":
            if arg.find(',') >= 0:
                proj = arg[:arg.find(',')]
                app = arg[arg.find(',')+1:]
                createApp(proj, app)
        elif opt == "--copy":
            if arg.find(',') >= 0:
                src = arg[:arg.find(',')]
                srclist = src.split('/')
                src = os.path.join(*srclist)
                dest = arg[arg.find(',')+1:]
                destlist = dest.split('/')
                dest = os.path.join(*destlist)
                shutil.copytree(src, dest)#, copy_function = shutil.copytree)
        elif opt == "--url":
            if arg.find(',') >= 0:
                proj = arg[:arg.find(',')]
                app = arg[arg.find(',')+1:]
                setupUrl(proj, app)
        elif opt == "--replace":
            first = arg.find(',')
            file_path = arg[:first]
            file_path = file_path.split('/')
            file_path = os.path.join(*file_path)
            str2 = arg[first+1:]
            second = str2.find(',')
            search_string = str2[:second]
            replace_string = str2[second+1:]
            #print(file_path, search_string, replace_string)
            findReplaceAt(file_path, search_string, replace_string)
        elif opt == "--reg":
            if arg.find(',') >= 0:
                proj = arg[:arg.find(',')]
                app = arg[arg.find(',')+1:]
                registerApp(proj, app)
        elif opt == "--folder":
            folderVar.append(arg)
        elif opt == "--setup":
            setup()
        elif opt == "--secure":
            secure(arg)
            try:
                findReplaceAt(os.path.join("src", arg, "settings.py"), "DEBUG = True\n", "DEBUG = False\n", 1)
                findReplaceAt(os.path.join("src", arg, "settings.py"), "ALLOWED_HOSTS = []\n", "ALLOWED_HOSTS = ['*']\n", 1)
            except:
                pass
        elif opt == "--run":
            if(arg =="0" or arg == '1' or arg == '2'):
                run(arg)
        elif opt == "--heroku":
            ver = ""
            if arg.find(',') >= 0:
                ver = arg[arg.find(',')+1:]
                arg = arg[:arg.find(',')]
            setupHeroku(arg, ver)
        elif opt == "--clean":
            clean()
        elif opt == "--signal":
            make_signal(arg)

if __name__ == "__main__":
    main(sys.argv[1:])
    for file in touchVar:
        content = ''
        if file.find(',') >= 0:
            content = file[file.find(',')+1:]
            file = file[:file.find(',')]
            file = file.split('/')
            file = os.path.join(*file)
        touch(file, content)

    for package in packageVar:
        install(package)

    for folderName in folderVar:
        folderName = folderName.split('/')
        folderName = os.path.join(*folderName)
        makeFolder(folderName)

#import getopt
#print getopt.getopt([ '--noarg', '--witharg', 'val', '--witharg2=another' ],'',[ 'noarg', 'witharg=', 'witharg2=' ])
