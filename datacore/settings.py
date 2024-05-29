"""
Django settings for datacore project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import sys
import configparser
from pathlib import Path

from django.core.management.color import color_style

style = color_style()

SITE_ID = 1

APP_NAME = 'datacore'

ETC_DIR = os.path.join('/etc/', APP_NAME)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'celery_progress.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'celery_progress': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOGIN_URL = ''

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vdm8v(v#esw$y2$iqt_8&6p$o+^299f!srgo3yj^_@n1%a#x&d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'datacore.bhp.org.bw']

CONFIG_FILE = f'{APP_NAME}.ini'

CONFIG_PATH = os.path.join(ETC_DIR, CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_FILE}\n'))
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'corsheaders',
    'anymail',
    'authentication.apps.AuthenticationConfig',
    'tsepamo.apps.TsepamoConfig',
    'datacore'
]

CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'authentication.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'datacore.urls'

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
                'datacore.context_processors.navbar_links',
            ],
        },
    },
]

WSGI_APPLICATION = 'datacore.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'datacore',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Authentication options

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_ADAPTER = 'authentication.adapter.CustomAccountAdapter'

REST_AUTH = {
    'REGISTER_SERIALIZER': 'authentication.serializers.CustomRegisterSerializer',
    'LOGIN_SERIALIZER': 'authentication.serializers.CustomLoginSerializer'}

# Email configurations

EMAIL_BACKEND = 'anymail.backends.postmark.EmailBackend'
# EMAIL_HOST = config['email_conf'].get('email_host')
# EMAIL_USE_TLS = config['email_conf'].get('email_use_tls')
# EMAIL_PORT = config['email_conf'].get('email_port')
# DEFAULT_FROM_EMAIL = config['email_conf'].get('email_user')
# EMAIL_HOST_USER = config['email_conf'].get('email_user')
# EMAIL_HOST_PASSWORD = config['email_conf'].get('email_host_pwd')
# EMAIL_USE_SSL = False

ANYMAIL = {
    'POSTMARK_SERVER_TOKEN': '8ed81295-95bd-4929-a2d4-4698cdb33dd3',
}

DEFAULT_FROM_EMAIL = 'adiphoko@bhp.org.bw'
EMAIL_PORT = 587

EMAIL_CONFIRM_REDIRECT_BASE_URL = 'http://localhost:8001/email/confirm/'

PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL = 'http://localhost:8001/password-reset/confirm/'

MERCURY_URL = 'http://127.0.0.1:8000/app/tsepamo'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'datacore', 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"


CSRF_TRUSTED_ORIGINS = ['https://127.0.0.1', 'https://localhost']
