from pathlib import Path
import os
from decouple import  config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SK")

DEBUG = config('DEBUG',default=False, cast=bool)

ALLOWED_HOSTS = [
    config("HOST",default='127.0.0.1'),
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'rest_framework',
    "corsheaders",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    config("GATEWAY"),
    
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if not DEBUG:
    DATABASES={
        'default':{
            'ENGINE':'django.db.backends.postgresql',
            'NAME':config('POSTGRES_DB'),
            'USER':config('POSTGRES_USER'),
            'PASSWORD':config('POSTGRES_PASSWORD'),
            'HOST':config('POSTGRES_DB'),
            'PORT':int(config('POSTGRES_PORT')),
        }
    }


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL='users.User'

from datetime import timedelta

from uuid import uuid4

AUTH_JWT={
    'AT_KEY':'AT',
    'RT_KEY':'RT',
    'UIDT_KEY':'UIDT',
    'SHORT_LIFETIME':timedelta(seconds=(int(config("SLT")) or 86400)),#in seconds
    'LONG_LIFETIME':timedelta(days=(int(config("LLT")) or 90)),#in days
    'DEFAULT_SECRET':config("JWT_SECRET",default=uuid4().hex)
}

REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY': 'ERROR',

}


