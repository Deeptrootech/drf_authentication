import os

from .base import * # noqa


DEBUG = env.bool("DJANGO_DEBUG")
ALLOWED_HOSTS = ['*']
DEV = DEBUG

INSTALLED_APPS += ('debug_toolbar',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cookie_cutter_db',
        'USER': 'cokie_cutter',
        'PASSWORD': 'admin@321',
        'HOST': 'localhost',
        'PORT': '',
    }
}

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

SECRET_KEY = 'devel'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 2

AUTH_PASSWORD_VALIDATORS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
