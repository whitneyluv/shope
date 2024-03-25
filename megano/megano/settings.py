"""
Django settings for megano project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from django.urls import reverse_lazy
from dotenv import load_dotenv, find_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog.apps.CatalogConfig',
    'auth_app.apps.AuthAppConfig',
    'profile_app.apps.ProfileAppConfig',
    'order_app.apps.OrderAppConfig',
    'cart_app.apps.CartAppConfig',
    'coreapp.apps.CoreAppConfig',
    'taggit',
    'discounts_app.apps.DiscountsAppConfig',
]

MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.cache.FetchFromCacheMiddleware",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS.append('127.0.0.1')

ROOT_URLCONF = 'megano.urls'

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
                'coreapp.utils.context_processors.quantity_products_and_total_amount_in_cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'megano.wsgi.application'


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


AUTH_USER_MODEL = 'auth_app.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = os.getenv('SERVER_EMAIL')
SERVER_ADMIN = os.getenv('SERVER_ADMIN')
TIME_OUT_BANNERS = int(os.getenv("TIME_OUT_BANNERS"))

CACHES = {
   "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
       # "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
       "LOCATION": "127.0.0.1:11211",
   }
}
CACHE_MIDDLEWARE_SECONDS = int(os.getenv("CACHE_MIDDLEWARE_SECONDS"))

CURRENCY_SYMBOL = '₽'

DEFAULT_NUM_PRODUCTS_IN_COMPARISON_LIST = 3


LOGIN_URL = reverse_lazy("auth_app:login")

WEBHOOKS_URL = os.getenv("URL_FOR_PAYMENT") + 'payment-notification/'
URL_FOR_PAYMENT = os.getenv("URL_FOR_PAYMENT")
PAYMENT_ACCOUNT_ID = os.getenv("PAYMENT_ACCOUNT_ID")
PAYMENT_SECRET_KEY = os.getenv("PAYMENT_SECRET_KEY")

