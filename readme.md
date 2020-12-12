#### :wrench: Criando Projeto
```
$ python -m venv myvenv
$ myvenv\Scripts\activate
$ pip install Django
$ pip install djangorestframework
$ mkdir backend
$ cd backend
$ django-admin startproject backend .
$ django-admin startapp api
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```
#### :wrench: Fazendo Deploy  de api simples no Heroku

```
$ heroku login -i
$ git init
$ heroku git:remote -a <nome criado no site do heroku>
$ git add .
$ git commit -m "deploy"
$ git branch
$ git push -u heroku main
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
```

