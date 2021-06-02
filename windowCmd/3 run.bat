python -m pipenv run python ..\src\manage.py makemigrations
python -m pipenv run python ..\src\manage.py migrate
python -m pipenv run python ..\src\manage.py runsslserver
pause
