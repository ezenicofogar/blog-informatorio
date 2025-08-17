from os import getenv as env
from base64 import b64decode
from .settings import BASE_DIR


SECRET_KEY = env('SECRET_KEY')
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY must be correctly set in .env file")

ALLOWED_HOSTS = ['eze97.pythonanywhere.com']

# Base de datos
# https://docs.djangoproject.com/es/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':     env('DATABASE_NAME'),
        'USER':     env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST':     env('DATABASE_HOST'),
    },
}

# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/es/5.2/howto/static-files/
FS_ROOT = BASE_DIR.parent.parent / 'fileserver'
STATIC_URL = '/static/'
STATIC_ROOT = FS_ROOT / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = FS_ROOT / 'media'