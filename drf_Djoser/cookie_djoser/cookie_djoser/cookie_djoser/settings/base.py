"""
Django settings for cookie_djoser project.
"""

from os.path import abspath, basename, dirname, join, normpath
from sys import path
from datetime import timedelta
from rest_framework.settings import api_settings
import environ

env = environ.Env()

# ***************** PATH CONFIGURATION *********************
BASE_DIR = dirname(dirname(__file__) + "../../../")
# Absolute filesystem path to the config directory:
CONFIG_ROOT = dirname(dirname(abspath(__file__)))
# Absolute filesystem path to the project directory:
PROJECT_ROOT = dirname(CONFIG_ROOT)

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(env_file=join(PROJECT_ROOT, '.env'))

PROJECT_NAME = basename(PROJECT_ROOT).capitalize()
PROJECT_FOLDER = basename(PROJECT_ROOT)
PROJECT_DOMAIN = "%s.com" % PROJECT_NAME.lower()

# Add our project to our pythonpath, this way we don"t need to type our project
# name in our dotted import paths:
path.append(CONFIG_ROOT)
# ***************** END PATH CONFIGURATION *********************


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Make this unique, and don"t share it with anybody.
SECRET_KEY = env('DJANGO_SECRET_KEY', default="")

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = STAGING = env.bool("DJANGO_DEBUG")
# Hosts/domain names that are valid for this site; required if DEBUG is False
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])

ADMINS = [('Deep', 'deep.pathak@trootech.com')]
MANAGERS = ADMINS
ADMIN_URL = env.str("DJANGO_ADMIN_URL", "admin")

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    # "kn_defaults.logging",

    # third party apps
    # https://djoser.readthedocs.io/en/latest/authentication_backends.html
    # here, we are using djoser JWT based stead of simple token based.
    "djoser",
    "rest_framework",
    "compressor",

    # Project Apps
    "user.apps.UsersConfig",
    "account"
]
AUTH_USER_MODEL = "user.User"
LOGIN_REDIRECT_URL = "user:redirect"
ROOT_URLCONF = "cookie_djoser.urls"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework.authentication.SessionAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10
}
# https://djoser.readthedocs.io/en/latest/settings.html
# https://dev.to/lyamaa/authenticate-with-djoser-2kf7
DJOSER = {
    "SERIALIZERS": {
        "user_create": "account.serializers.UserRegistrationSerializer",  # custom serializer
        "user": "djoser.serializers.UserSerializer",
        "current_user": "djoser.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserSerializer",
    },
    # "LOGIN_FIELD": "email",  # Default: username
    "USER_CREATE_PASSWORD_RETYPE": True,  # Default: False
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,  # Default: False
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,  # Default: False
    "SEND_CONFIRMATION_EMAIL": True,  # Default: False
    "SET_USERNAME_RETYPE": True,  # Default: False
    "SET_PASSWORD_RETYPE": True,  # Default: False
    "USERNAME_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,  # Default: False
    # "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    # "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
    #     "your redirect url",
    #     "your redirect url",
    # ],
}
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "kn_defaults.logging.middlewares.KnLogging",
]

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (normpath(join(PROJECT_ROOT, "templates")),),
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.csrf",
                "django.template.context_processors.tz",

                "django.template.context_processors.static",

            ]
        },
    },
]
# Python dotted path to the WSGI application used by Django"s runserver.
WSGI_APPLICATION = "cookie_djoser.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': env.db("DATABASE_URL", default="mysql://root:root@localhost:3306/cookie_satup_1")
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)
DATABASES["default"]["OPTIONS"] = {
    "init_command": "SET default_storage_engine=InnoDB",
    "charset": "utf8mb4",
    "use_unicode": True,
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "Asia/Calcutta"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = normpath(join(PROJECT_ROOT, "media"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = normpath(join(PROJECT_ROOT, "assets"))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don"t forget to use absolute paths, not relative paths.
    normpath(join(PROJECT_ROOT, "static")),
)

EMAIL_BACKEND = env.str("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = env.str("EMAIL_HOST", "")
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", False)
EMAIL_PORT = env.int("EMAIL_PORT", 25)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# KN_LOG_FILE_PATH = join(DJANGO_ROOT, "logs/log.log")

# from kn_defaults.logging.defaults import get_base_logging
# LOGGING = get_base_logging(logstash=False)
#
# KN_LOGGING_URL_PATTERNS = []

LOCALE_PATHS = (normpath(join(PROJECT_ROOT, "locale")),)

# Dummy gettext function
gettext = lambda s: s

LANGUAGES = [
    ("en", gettext("en")),

]

# Analytics
GOOGLE_ANALYTICS = env.str("GOOGLE_ANALYTICS", default="")

CACHE_ENGINES = {

    "dummy": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

CACHES = {
    "default": CACHE_ENGINES[env.str("CACHE", default="dummy")]
}

SENTRY_DSN = env.str("SENTRY_DSN", "")
