from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^search.html$', 'web.views.search.search_trips_view', name='search_trips'),
)