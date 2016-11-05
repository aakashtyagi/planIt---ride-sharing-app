import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'b0b6de0f4f12566f66f3121dad554dcf661f69d2f2fe117b331ae2a211d79d3c9e07d17b8affd5885fff8d6176804bc546caf9ce30cfa84dd1f82451115916c5'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'web.urls'
WSGI_APPLICATION = 'web.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
SITE_ID = 1
LANGUAGE_CODE = 'en-us'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 5 * 60
SESSION_COOKIE_HTTPONLY = True



INSTALLED_APPS = (
    'mb_admin',
    'django.contrib.admin',
    'mb_bootstrap',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.formtools',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'development.sqlite3'),
    }
}

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)
