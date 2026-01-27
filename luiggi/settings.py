"""Django settings"""

import os
from pathlib import Path

from django_stubs_ext import monkeypatch
from dotenv import load_dotenv

monkeypatch()

BASE_DIR = Path(__file__).resolve().parent.parent

envfile = BASE_DIR / '.env'
if envfile.exists():
  load_dotenv(envfile)

SECRET_KEY = os.environ.get(
  'DJANGO_SECRET_KEY',
  'django-insecure-ixz!t0t@3g^*a!y_s&73!8%cok2%2k&&mar24@-q3a#_8$tabj',
)

DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
  'django.contrib.contenttypes',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'categories',
  'movements',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'luiggi.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
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

WSGI_APPLICATION = 'luiggi.wsgi.application'
ASGI_APPLICATION = 'luiggi.asgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('DATABASE_NAME', 'luiggi'),
    'USER': os.environ.get('DATABASE_USERNAME', 'postgres'),
    'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres'),
    'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
    'PORT': os.environ.get('DATABASE_PORT', '5432'),
  }
}


AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
USE_I18N = True

TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_URL = 'static/'


LOGGING_LEVEL = 'INFO'

if DEBUG:
  LOGGING_LEVEL = 'INFO'

BASE_LOGGING = {
  'handlers': ['console'],
  'level': LOGGING_LEVEL,
  'propagate': False,
}

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'simple': {
      'format': '[{levelname}] {asctime} @ {name}: {message}',
      'style': '{',
    },
  },
  'handlers': {
    'console': {
      'level': LOGGING_LEVEL,
      'class': 'logging.StreamHandler',
      'formatter': 'simple',
    },
  },
  'root': BASE_LOGGING,
  'loggers': {
    'django.server': BASE_LOGGING,
    'django.db': BASE_LOGGING,
  },
}
