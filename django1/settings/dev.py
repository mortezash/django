# project/settings/dev.py
from .base import *

DEBUG = True

SECRET_KEY = 'dev-secret-key'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        # use sqlite
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',

        #use Mysql
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django1',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3307',

        #use postgresql
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'mydatabase',
        #'USER': 'myuser',
        #'PASSWORD': 'mypassword',
        #'HOST': 'localhost',
        #'PORT': '5432',

        #pip install mysqlclient
        #python manage.py makemigrations
        #python manage.py migrate
    }
}
