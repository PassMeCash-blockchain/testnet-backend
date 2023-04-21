from pathlib import Path
from core.env import load_env
from corsheaders.defaults import default_headers
import os
from pathlib import Path
from datetime import timedelta

load_env()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv("debug_status")))

ALLOWED_HOSTS = os.getenv("allowed_hosts").split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # installed apps
    'endpoints.apps.EndpointsConfig',

    # installed dependecies
    'rest_framework',
    'corsheaders',

    'djagger',
    'drf_yasg',

]

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
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ------------------------------------------------------------------------------------
# CORS
# ------------------------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = os.getenv("cors_allowed_hosts").split(",")

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = list(default_headers)

# ------------------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------------------
CKEY = os.getenv("connection-key")

DJAGGER_DOCUMENT = {
    "version": "1.0.0",
    "title": "PassMeCash API Documentation",
    "description": """This is PassMeCash Internal API Documentation""",
    "license_name": "MIT",
    "contact_email": "api@passme.cash",
    "tags": [
        {"name": "Account", "description": "API for account Creation and Authentication "},
    ],
    "x-tagGroups": [
        {"name": "USER MANAGEMENT", "tags": ['Account']}
    ],
    "servers": [
        {
            "url": "https://example.com",
            "description": "MainNet API Server"
        },
        {
            "url": "https://example.com",
            "description": "TestNet API Server"
        },
    ]
}
    # "app_names": ['Account', 'otp'],