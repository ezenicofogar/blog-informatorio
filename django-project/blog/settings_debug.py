from os import getenv as env
from .settings import BASE_DIR


SECRET_KEY = env('SECRET_KEY')
if SECRET_KEY is None:
    SECRET_KEY = 'django-insecure-*b+s*b7)#ccwkyol+2r=e9947$91&xf&fq_bglw#3j$u)3pa&y'

ALLOWED_HOSTS = []


# Base de datos
# https://docs.djangoproject.com/es/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/es/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = None
