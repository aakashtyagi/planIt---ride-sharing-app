"""
Settings for REST framework are all namespaced in the MBAPI_FRAMEWORK setting.
For example your project's `settings.py` file might look like this:

MBAPI_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'mb_api.renderers.JSONRenderer',
        'mb_api.renderers.YAMLRenderer',
    )
    'DEFAULT_PARSER_CLASSES': (
        'mb_api.parsers.JSONParser',
        'mb_api.parsers.YAMLParser',
    )
}

This module provides the `api_setting` object, that is used to access
REST framework settings, checking for user settings first, then falling
back to the defaults.
"""
from __future__ import unicode_literals
from django.conf import settings
from django.utils import importlib, six
from mb_api import ISO_8601


USER_SETTINGS = getattr(settings, 'MBAPI_FRAMEWORK', None)

DEFAULTS = {
    # Base API policies
    'DEFAULT_RENDERER_CLASSES': (
        'mb_api.renderers.JSONRenderer',
        'mb_api.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'mb_api.parsers.JSONParser',
        'mb_api.parsers.FormParser',
        'mb_api.parsers.MultiPartParser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'mb_api.authentication.SessionAuthentication',
        'mb_api.authentication.BasicAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'mb_api.permissions.AllowAny',
    ),
    'DEFAULT_THROTTLE_CLASSES': (),
    'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'mb_api.negotiation.DefaultContentNegotiation',

    # Genric view behavior
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'mb_api.serializers.ModelSerializer',
    'DEFAULT_PAGINATION_SERIALIZER_CLASS': 'mb_api.pagination.PaginationSerializer',
    'DEFAULT_FILTER_BACKENDS': (),

    # Throttling
    'DEFAULT_THROTTLE_RATES': {
        'user': None,
        'anon': None,
    },
    'NUM_PROXIES': None,

    # Pagination
    'PAGINATE_BY': None,
    'PAGINATE_BY_PARAM': None,
    'MAX_PAGINATE_BY': None,

    # Filtering
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',

    # Authentication
    'UNAUTHENTICATED_USER': 'django.contrib.auth.models.AnonymousUser',
    'UNAUTHENTICATED_TOKEN': None,

    # View configuration
    'VIEW_NAME_FUNCTION': 'mb_api.views.get_view_name',
    'VIEW_DESCRIPTION_FUNCTION': 'mb_api.views.get_view_description',

    # Exception handling
    'EXCEPTION_HANDLER': 'mb_api.views.exception_handler',

    # Testing
    'TEST_REQUEST_RENDERER_CLASSES': (
        'mb_api.renderers.MultiPartRenderer',
        'mb_api.renderers.JSONRenderer'
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'multipart',

    # Browser enhancements
    'FORM_METHOD_OVERRIDE': '_method',
    'FORM_CONTENT_OVERRIDE': '_content',
    'FORM_CONTENTTYPE_OVERRIDE': '_content_type',
    'URL_ACCEPT_OVERRIDE': 'accept',
    'URL_FORMAT_OVERRIDE': 'format',

    'FORMAT_SUFFIX_KWARG': 'format',
    'URL_FIELD_NAME': 'url',

    # Input and output formats
    'DATE_INPUT_FORMATS': (
        ISO_8601,
    ),
    'DATE_FORMAT': None,

    'DATETIME_INPUT_FORMATS': (
        ISO_8601,
    ),
    'DATETIME_FORMAT': None,

    'TIME_INPUT_FORMATS': (
        ISO_8601,
    ),
    'TIME_FORMAT': None,

    # Pending deprecation
    'FILTER_BACKEND': None,

}


# List of settings that may be in string import notation.
IMPORT_STRINGS = (
    'DEFAULT_RENDERER_CLASSES',
    'DEFAULT_PARSER_CLASSES',
    'DEFAULT_AUTHENTICATION_CLASSES',
    'DEFAULT_PERMISSION_CLASSES',
    'DEFAULT_THROTTLE_CLASSES',
    'DEFAULT_CONTENT_NEGOTIATION_CLASS',
    'DEFAULT_MODEL_SERIALIZER_CLASS',
    'DEFAULT_PAGINATION_SERIALIZER_CLASS',
    'DEFAULT_FILTER_BACKENDS',
    'EXCEPTION_HANDLER',
    'FILTER_BACKEND',
    'TEST_REQUEST_RENDERER_CLASSES',
    'UNAUTHENTICATED_USER',
    'UNAUTHENTICATED_TOKEN',
    'VIEW_NAME_FUNCTION',
    'VIEW_DESCRIPTION_FUNCTION'
)


def perform_import(val, setting_name):
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    if isinstance(val, six.string_types):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val


def import_from_string(val, setting_name):
    """
    Attempt to import a class from a string representation.
    """
    try:
        # Nod to tastypie's use of importlib.
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ImportError as e:
        msg = "Could not import '%s' for API setting '%s'. %s: %s." % (val, setting_name, e.__class__.__name__, e)
        raise ImportError(msg)


class APISettings(object):
    """
    A settings object, that allows API settings to be accessed as properties.
    For example:

        from mb_api.settings import api_settings
        print api_settings.DEFAULT_RENDERER_CLASSES

    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.
    """
    def __init__(self, user_settings=None, defaults=None, import_strings=None):
        self.user_settings = user_settings or {}
        self.defaults = defaults or {}
        self.import_strings = import_strings or ()

    def __getattr__(self, attr):
        if attr not in self.defaults.keys():
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Coerce import strings into classes
        if val and attr in self.import_strings:
            val = perform_import(val, attr)

        self.validate_setting(attr, val)

        # Cache the result
        setattr(self, attr, val)
        return val

    def validate_setting(self, attr, val):
        if attr == 'FILTER_BACKEND' and val is not None:
            # Make sure we can initialize the class
            val()

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
