"""
Configuración de Django para el proyecto blog.

Generado por 'django-admin startproject' usando Django 5.2.4.

Para más información sobre este archivo, consulta
https://docs.djangoproject.com/es/5.2/topics/settings/

Para la lista completa de configuraciones y sus valores, consulta
https://docs.djangoproject.com/es/5.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
from os import getenv as env

# Construye rutas dentro del proyecto así: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent


# python-dotenv carga el archivo .env
load_dotenv(BASE_DIR.parent / '.env')


# DEBUG es False por defecto, a menos que esté definido en el archivo .env
DEBUG = env('DEBUG') is not None


# Definición de la aplicación

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Validación de contraseñas
# https://docs.djangoproject.com/es/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización
# https://docs.djangoproject.com/es/5.2/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Cordoba'

USE_I18N = True

USE_TZ = True


# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/es/5.2/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / 'public',
]


# Tipo de campo de clave primaria por defecto
# https://docs.djangoproject.com/es/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Cargar configuraciones específicas
if DEBUG:
    from .settings_debug import SECRET_KEY, ALLOWED_HOSTS, DATABASES, STATIC_URL, STATIC_ROOT
else:
    from .settings_production import SECRET_KEY, ALLOWED_HOSTS, DATABASES, STATIC_URL, STATIC_ROOT
