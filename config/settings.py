"""
Django settings for OppiaMobile project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from django.utils.translation import gettext_lazy as _

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uzekt30thl4&hw)p@c#ht=b8mn!3l080kmnuk7ez+g5l%lb*p9'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

ALLOWED_HOSTS = []
DEBUG = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.i18n',
            ],
            'debug': True,
        },
    },
]

INSTALLED_APPS = [
    'learning_rebellion',
    'crispy_forms',
    'sorl.thumbnail',
    'ckeditor',
    'blog',
    'projects',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TIME_ZONE = 'UTC'
USE_TZ = True
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, '..','static')]
STATIC_ROOT = os.path.join(ROOT_DIR, '..', 'static')
MEDIA_ROOT = os.path.join(ROOT_DIR, '..', 'media')
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

ROOT_URLCONF = 'config.urls'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'


# Email
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/'
SERVER_EMAIL = 'adming@email.org'
EMAIL_SUBJECT_PREFIX = '[SUBJECT_PREFIX]: '


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-GB'
USE_I18N = True
USE_L10N = True

LANGUAGES = ('en', _('English'))

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Database - mainly this is for the automated testing
# a proper RDBMS should be configured in your settings_secret.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Import secret_settings.py (if exists)
# > see settings_secret.py.template for reference
try:
    from config.settings_secret import *
except ImportError:
    print("settings_secret.py file could not be found.")
