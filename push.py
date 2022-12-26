import os
import sys

os.system("git init")
os.system("git remote add origin https://github.com/rshnGhost/django-quick.git")
os.system("git config --local user.name 'rshnGhost'")
os.system("git config --local user.email '31742263+rshnGhost@users.noreply.github.com'")
os.system("git branch -m django-4.1.4")
os.system("git status")
os.system("git add .")
os.system("git status")
os.system(f'git commit -m "{str("".join(sys.argv[1:]))}"')
os.system("git switch django-4.1.4")
os.system("git push origin django-4.1.4")
