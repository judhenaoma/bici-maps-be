
from pathlib import Path
from datetime import timedelta
import os
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# GDAL_LIBRARY_PATH = 'C:/OSGeo4W/bin/gdal306.dll'

# LIB_DIR = os.path.join(BASE_DIR, '..', 'lib')

# Ruta absoluta de la biblioteca GDAL
# GDAL_LIBRARY_PATH = os.path.join(LIB_DIR, 'gdal306.dll')


# GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH', '/usr/lib/libgdal.so')


# Specify the default model to authenticate users
AUTH_USER_MODEL = 'bicimaps_app.User'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#%18dev8evo+_*k(9!iz)x2zdo9c2d-sx^%%+@hyn0)tv)udpl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://bicimaps.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'bicimaps_app',
    # dependecies to add geospatial support
    'django.contrib.gis',
    'rest_framework_gis',
]

ALLOWED_HOSTS = ["localhost", "192.168.1.58"]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:5173',  # for localhost (REACT Default)
    'http://192.168.1.58:5173',  # for network 
    'https://bicimaps-dev.herokuapp.com',
    'https://effervescent-parfait-7ba86e.netlify.app',
    'https://bicimaps.netlify.app',
)


CSRF_TRUSTED_ORIGINS  = [
    'http://localhost:5173',  # for localhost (REACT Default)
    'http://192.168.1.58:5173',  # for network 
    'https://bicimaps-dev.herokuapp.com',
    'https://effervescent-parfait-7ba86e.netlify.app',
    'https://bicimaps.netlify.app',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'USER_ID_FIELD': 'email',
    'USER_ID_CLAIM': 'user_email',
    }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


ROOT_URLCONF = 'bicimaps.urls'

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

WSGI_APPLICATION = 'bicimaps.wsgi.application'

DATABASES = {
    'default': {
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'c4opKsV0FjzUCmIo12KT',
        'HOST': 'containers-us-west-16.railway.app',
        'PORT': '6407',
    }
}

DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'staticfiles/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import django_heroku
django_heroku.settings(locals())


# DATABASES['default'].update(db_from_env)


# import dj_database_url

# DATABASES['default'] = dj_database_url.config(
#     conn_max_age=600,
#     conn_health_checks=True,
# )