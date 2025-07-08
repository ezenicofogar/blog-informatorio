from os import getenv as env
from base64 import b64decode
from .settings import BASE_DIR


SECRET_KEY = env('SECRET_KEY')
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY must be correctly set in .env file")

# TODO: configurar origenes
ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# TODO: configurar database
DATABASES = {
    ...
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# TODO: configurar archivos estaticos
STATIC_URL = ...
# TODO: configurar directorio para collectstatic
STATIC_ROOT = ...
