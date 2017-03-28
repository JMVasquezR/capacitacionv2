"""
Django settings for capacitacionv2 project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = 'LOCAL'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'izzsuvka)mnc)c_u53=o319(#(%jd)hs#^#ua1bawogi21b2@+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pandas',
    'rest_framework',
    'asistencia',
    'locales_consecucion',
    'consecucion_pases',
    'evaluacion',
    'ubigeo',
    'distribucion',
    'seguridad',
    'reportes',
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

ROOT_URLCONF = 'capacitacionv2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'seguridad.context_processor.recursive_menu'
            ],
        },
    },
]

WSGI_APPLICATION = 'capacitacionv2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

"""
Variables de entorno
"""
_DATABASECONF = {}
if ENV == 'LOCAL':
    _DATABASECONF = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': 'CPV_CAPACITACION_PRUEBA',
            'USER': 'us_capacitacion_web',
            'PASSWORD': 'cap5wegU$re',
            'HOST': '172.18.1.41',
            'OPTIONS': {
                'driver': 'SQL Server',
                'unicode_results': True
            },
        },
    }
elif ENV == 'DESARROLLO':
    _DATABASECONF = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': 'CPV_CAPACITACION_PRUEBA',
            'USER': 'us_capacitacion_web',
            'PASSWORD': 'cap5wegU$re',
            'HOST': '172.18.1.41',
            'OPTIONS': {
                'driver': 'ODBC Driver 11 for SQL Server',
                'unicode_results': True
            },
        },
    }
elif ENV == 'SQLITE':
    _DATABASECONF = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }
DATABASES = _DATABASECONF

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_URL = '/static/'
