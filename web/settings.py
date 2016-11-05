from mb_settings.settings import *
from django.core.urlresolvers import reverse_lazy

LOGIN_URL = reverse_lazy('auth_login')
TIME_ZONE = 'America/Chicago'
USE_TZ = False

# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL='help@yallplanit.com'
# CONTACT_US_EMAIL='help@yallplanit.com'
# EMAIL_HOST='box1090.bluehost.com'
# EMAIL_PORT=993
# EMAIL_HOST_USER='help@yallplanit.com'
# EMAIL_HOST_PASSWORD='Androiduser.10'
# EMAIL_USE_TLS=True
# DEFAULT_FROM_EMAIL='help@yallplanit.com'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'teen14aakash@gmail.com'
EMAIL_HOST_PASSWORD = '10blackbox'
DEFAULT_FROM_EMAIL='aakash.tyagi@yallplanit.com'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#DEBUG=False
#TEMPLATE_DEBUG = False
ALLOWED_HOSTS=['box1090.bluehost.com']


INSTALLED_APPS += (
    'mb_contactus',
    'mb_session',
    'mb_forms',
    'mb_grids',
    'mb_tables',
    'mb_menu',
    'mb_api',
    'mb_errorpages',
    'web',
)

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'planit_web',
    'USER': 'root',
    'OPTIONS': {'init_command': 'SET storage_engine=INNODB;'},
}


MIDDLEWARE_CLASSES += (
    'mb_session.middleware.MacrobitsMiddlewareSession',
    'audit_log.middleware.UserLoggingMiddleware',
)

MBAPI_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'mb_api.permissions.IsAuthenticated'
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'mb_api.renderers.JSONRenderer',
        'mb_api.renderers.BrowsableAPIRenderer',
        'mb_api.renderers.XMLRenderer',
    )
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    # "allauth.account.auth_backends.AuthenticationBackend"
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    # "allauth.account.context_processors.account",
    # "allauth.socialaccount.context_processors.socialaccount",
)

# LOGIN_REDIRECT_URL = '/'
# SOCIALACCOUNT_QUERY_EMAIL = True
# SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'SCOPE': ['email', 'public_profile', 'user_friends'],
#         'METHOD': 'js_sdk'  # instead of 'oauth2'
#     }
# }

SITE_ID = 2

# Facebook related Settings
FACEBOOK_APP_ID = '922994814454175'
FACEBOOK_SECRET_KEY = 'fc5fb8b2923039c3700d10f120fc8203'
NUMVERIFY_KEY = '8c59fa4e7344742a7d565b6f0af60bb9'