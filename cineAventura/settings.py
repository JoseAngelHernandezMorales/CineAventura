"""
Django settings para el proyecto AkaFilms.

Este archivo contiene la configuración principal de nuestro proyecto AkaFilms.

Variables de entorno requeridas (.env):
    SECRET_KEY: Clave secreta de Django (str)
    DEBUG: Modo de depuración (bool, default=False)
    ALLOWED_HOSTS: Hosts permitidos separados por coma (str)
"""

from pathlib import Path
import os
from decouple import config, Csv

# CONFIGURACIÓN DE RUTAS

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

# Hosts/dominios permitidos para servir la aplicación
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# DEFINICIÓN DE APLICACIONES

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'peliculas',  # Nuestra aplicación
]

# MIDDLEWARE

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Middlewares personalizados
    'peliculas.middleware.LoginRedirectMiddleware',
    'peliculas.middleware.TerminosMiddleware',
]

ROOT_URLCONF = 'cineAventura.urls'

# CONFIGURACIÓN DE TEMPLATES

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cineAventura.wsgi.application'

# CONFIGURACIÓN DE BASE DE DATOS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# VALIDACIÓN DE CONTRASEÑAS

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

# CONFIGURACIÓN INTERNACIONAL Y DE ZONA HORARIA

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# ARCHIVOS ESTÁTICOS Y MEDIA

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# MODELOS

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CONFIGURACIÓN DE SEGURIDAD ADICIONAL

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# LOGIN / LOGOUT

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Función personalizada para redirigir según tipo de usuario
def login_redirect(request):
    if request.user.is_staff:
        return '/admin/'
    return '/'

# API de Películas (TMDB)

TMDB_API_KEY = '644c139d5d96c949b4a56febe827abf3'
TMDB_BASE_URL = 'https://api.themoviedb.org/3'
TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'
