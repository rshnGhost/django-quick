import sys, getopt, shutil
from setupSslserver import *
#from setup_heroku import *

touchVar = []
packageVar = []
folderVar = []

def help():
    print("usage: "+os.path.basename(__file__)+" [-h] [-t <file_name>,<optional_file_content>] [-i] \
    \n\t[--ireqfile <file_name>] [-p <package_name>] [--package <package_name>] [-c <project_name>]\
    \n\t[--project <project_name>] [--cred] [-a <application_name>] [--app <application_name>]\
    \n\t[-r <project_name>,<application_name>] [--reg <project_name>,<application_name>] [--url <project_name>,<application_name>]\
    \n\t[--copy <source>,<destination>] [--replace <file_path>,<search_string>,<replace_string>] [--folder <folder_path>]\
    \n\t[--setup] [--run <option{0, 1}>]")
    file_name = os.path.basename(__file__)
    d = {
        "Help": [file_name+" -h", "", ""],
        "Create file": [file_name+" -t", "<file_name>",",<optional_file_content>"],
        "Install Requirments from Requirments file": [file_name+" -i", "", ""],
        "Install Requirments from user Requirments file": [file_name+" --ireqfile", "<file_name>", ""],
        "Install Package": [file_name+" -p", "<package_name>", ""],
        "Install Package": [file_name+" --package", "<package_name>", ""],
        "Create Project": [file_name+" -c", "<project_name>", ""],
        "Create Project": [file_name+" --project", "<project_name>", ""],
        "Create Credentials File(default)": [file_name+" --cred", "", ""],
        "Create Application": [file_name+" -a", "<project_name>,<application_name>", ""],
        "Create Application": [file_name+" --app", "<project_name>,<application_name>", ""],
        "Register Application": [file_name+" -r", "<project_name>,<application_name>", ""],
        "Register Application": [file_name+" --reg", "<project_name>,<application_name>", ""],
        "Setup Application Url": [file_name+" --url", "<project_name>,<application_name>", ""],
        "Copy Directory": [file_name+" --copy", "<source>,<destination>", ""],
        "Find and Replace At": [file_name+" --replace", "<file_path>,<search_string>,<replace_string>", ""],
        "Create Folder": [file_name+" -f", "<folder_path>", ""],
        "Create Folder": [file_name+" --folder", "<folder_path>", ""],
        "Run Setup": [file_name+" -s", "", ""],
        "Run Setup": [file_name+" --setup", "", ""],
        "Run Server": [file_name+" --run", "<option{0, 1}>", ""]
    }
    print("{:<46} {:<24} {:<33} {:<6}".format('Action','Usage','Argument','Optional/Required Argument'))
    for action, help in d.items():
        usage, argument, optional = help
        print("{:<46} {:<24} {:<33} {:6}".format(action, usage, argument, optional))
    '''
    print("Help:\t  "+os.path.basename(__file__)+" -h")
    print("Create file:\t  "+os.path.basename(__file__)+" -t <file_name>,<file_content>")
    print("Install Requirments from Requirments file:\t  "+os.path.basename(__file__)+" -i")
    print("Install Requirments from user Requirments file:\t  "+os.path.basename(__file__)+" --ireqfile <file_name>")
    print("Install Package:\t  "+os.path.basename(__file__)+" -p <package_name>")
    print("Install Package:\t  "+os.path.basename(__file__)+" --package <package_name>")
    print("Create Project:\t  "+os.path.basename(__file__)+" -c <project_name>")
    print("Create Project:\t  "+os.path.basename(__file__)+" --project <project_name>")
    print("Create Credentials File(default):\t  "+os.path.basename(__file__)+" --cred")
    print("Create Application:\t  "+os.path.basename(__file__)+" -a <project_name>,<application_name>")
    print("Create Application:\t  "+os.path.basename(__file__)+" --app <project_name>,<application_name>")
    print("Register Application:\t  "+os.path.basename(__file__)+" -r <project_name>,<application_name>")
    print("Register Application:\t  "+os.path.basename(__file__)+" --reg <project_name>,<application_name>")
    #print("Setup Application Url:\t  "+os.path.basename(__file__)+" --url <project_name>,<application_name>")
    #print("Copy Directory:\t  "+os.path.basename(__file__)+" --copy <source>,<destination>")
    #findReplaceAt('src/main/urls.py', "]\n", "\tpath('accounts/', include('registration.backends.simple.urls')),\n")
    #print("Find and Replace At:\t  "+os.path.basename(__file__)+" --replace <file_path>,<search_string>,<replace_string>")
    print("Create Folder:\t  "+os.path.basename(__file__)+" -f <folder_path>")
    print("Create Folder:\t  "+os.path.basename(__file__)+" --folder <folder_path>")
    print("Run Setup:\t  "+os.path.basename(__file__)+" -s")
    print("Run Setup:\t  "+os.path.basename(__file__)+" --setup")
    print("Run Server:\t  "+os.path.basename(__file__)+" --run <option>")
    '''

def main(argv):
    try:
        opts, args = getopt.getopt(argv,
                                    "hti:p:c:a:r:f:s:",
                                    ["touch=","ireqfile=","package=","project=",
                                    "cred","app=","reg=","folder=","move=","setup",
                                    "run=","copy=","url=","replace="]
                                    )
    except getopt.GetoptError:
        help()
        sys.exit(2)
    print(len(opts))
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-t", "--touch"):
            touchVar.append(arg)
        elif opt == '-i':
            installRequirments()
        elif opt == '--ireqfile':
            installRequirments(arg)
        elif opt in ("-p", "--package"):
            packageVar.append(arg)
        elif opt in ("-c", "--project"):
            createProject(arg)
        elif opt == "--cred":
            makeFolder("src\credentials")
            touch("src\credentials\credentials.py",'credentials = {\n\t"email_username" : "optional",\n\t"email_password" : "optional",\n\t"postgresql_name" : "optional",\n\t"postgresql_username" : "optional",\n\t"postgresql_password" : "optional",\n\t"postgresql_host" : "optional",\n\t"postgresql_port" : "optional",\n\t"secret_key" : "required",\n\t"consumer_key" : "optional",\n\t"consumer_secret" : "optional",\n\t"access_token" : "optional",\n\t"access_token_secret" : "optional",\n}')
            print("created")
        elif opt in ("-a", "--app"):
            if arg.find(',') >= 0:
                proj = arg[:arg.find(',')]
                app = arg[arg.find(',')+1:]
                createApp(proj, app)
        elif opt == "--copy":
            if arg.find(',') >= 0:
                src = arg[:arg.find(',')]
                dest = arg[arg.find(',')+1:]
                shutil.copytree(src, dest)#, copy_function = shutil.copytree)
        elif opt == "--url":
            if arg.find(',') >= 0:
                proj = arg[:arg.find(',')]
                app = arg[arg.find(',')+1:]
                setupUrl(proj, app)
        elif opt == "--replace":
            first = arg.find(',')
            file_path = arg[:first]
            str2 = arg[first+1:]
            second = str2.find(',')
            search_string = str2[:second]
            replace_string = str2[second+1:]
            print(file_path, search_string, replace_string)
            findReplaceAt(file_path, search_string, replace_string)
        elif opt in ("-r", "--reg"):
            if arg.find(',') >= 0:
                proj = arg[:arg.find(',')]
                app = arg[arg.find(',')+1:]
                registerApp(proj, app)
        elif opt in ("-f", "--folder"):
            folderVar.append(arg)
        elif opt in ("-s", "--setup"):
            setup()
        elif opt == "--run":
            if(arg =="0" or arg == '1'):
                run(arg)

if __name__ == "__main__":
    main(sys.argv[1:])
    for file in touchVar:
        content = ''
        if file.find(',') >= 0:
            content = file[file.find(',')+1:]
            file = file[:file.find(',')]
        touch(file, content)

    for package in packageVar:
        install(package)

    for folderName in folderVar:
        makeFolder(folderName)

#import getopt
#print getopt.getopt([ '--noarg', '--witharg', 'val', '--witharg2=another' ],'',[ 'noarg', 'witharg=', 'witharg2=' ])
