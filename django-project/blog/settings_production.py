from os import getenv as env
from base64 import b64decode
from .settings import BASE_DIR


SECRET_KEY = env('SECRET_KEY')
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY must be correctly set in .env file")

# TODO: configurar origenes
ALLOWED_HOSTS = []


# Base de datos
# https://docs.djangoproject.com/es/5.2/ref/settings/#databases

# TODO: configurar base de datos
DATABASES = {
    ...
}


# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/es/5.2/howto/static-files/

# TODO: configurar archivos estaticos
STATIC_URL = ...
# TODO: configurar directorio para collectstatic
STATIC_ROOT = ...
