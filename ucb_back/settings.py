"""
Django settings for ucb_back project.

Generated by 'django-admin startproject' using Django 1.8.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ltgi1s-$y+5_=97ki%h1gumw+68!$tt_$n*ji4$3kju&w44eu$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.18.63', 'localhost', 'adrianrojas.pythonanywhere.com' ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'Unidadorganigrama',
    'Persona',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ucb_back.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'ucb_back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


#-------------------------- HANA Connection ------------------------------------
#DATABASES = {
#    'default': {
#        'ENGINE': 'django_hana',
#        'NAME': 'ADMNALRRHH',# The schema to use. It will be created if doesn't exist
#        'USER': 'ADMNALRRHH',
#        'PASSWORD': 'Rrhh1234',
#        'HOST': '192.168.18.180',
#        'PORT': '30015',
#    }
#}


#-------------------------- SQLite Connection ------------------------------------
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


#-------------------------- MySQL Connection ------------------------------------
#DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.mysql',
#            'NAME': 'rrhh',
#            'USER': 'remoto',
#            'PASSWORD': 'Rrhh1234',
#            'HOST': '192.168.18.63',
#            'PORT': '3306',
#        }
#    }



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Rest Framework
REST_FRAMEWORK = {
   # 'DEFAULT_PERMISSION_CLASSES': (
   #     'rest_framework.permissions.IsAuthenticated',
   # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    "LANGUAGE_CODE": "es-es",
}

CORS_ORIGIN_WHITELIST = (
    '190.104.29.19'
    '0.0.0.0'
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'assets')]
