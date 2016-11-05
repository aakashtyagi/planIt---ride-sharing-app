from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

api_patterns = patterns('web.api',
    url(r'^test$', 'misc.test_api'),
    url(r'^search$', 'search.search_api'),
    url(r'^profile/trips', 'trips.user_trip_api', name='profile_trip_api'),
)

from mb_api.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(api_patterns, suffix_required=True, allowed=['json', 'api', 'xml'])
