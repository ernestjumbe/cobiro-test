"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from django.conf.global_settings import *
#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from cobiro.settings.secrets import *


import cobiro as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

#sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/Copenhagen'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
)

DATE_FORMAT = 'd B Y'

DATETIME_FORMAT = 'd B Y H:M'


# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third paty apps

    'rest_framework',

    # Project apps

    'stores',
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

ROOT_URLCONF = 'cobiro.urls'

WSGI_APPLICATION = 'cobiro.wsgi.application'

LOGIN_URL = '/login/'

LOGOUT_URL = '/logout/'

LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'


#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#==============================================================================
# Static Files
#==============================================================================

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
)

#==============================================================================
# Miscellaneous project settings
#==============================================================================
DATA_SOURCE = 'json_file'

DATA_SOURCE_FILE = os.path.join(BASE_DIR, 'english_shops' + "." + 'json')
#==============================================================================
# Third party app settings
#==============================================================================
