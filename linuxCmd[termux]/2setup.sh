cd ..
pipenv run python setup-django-sslserver.py
cd linuxCmd[termux]
mkdir ../src/credentials
mkdir ../src/static
mkdir ../src/media
echo 'credentials = {"secret_key" : "required"}' >>../src/credentials/credentials.py
pipenv sync
pipenv install
pipenv run python ../src/manage.py makemigrations
pipenv run python ../src/manage.py migrate
echo "Enter following details for user"
pipenv run python ../src/manage.py createsuperuser
