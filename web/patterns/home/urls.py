from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^$', lambda x: HttpResponseRedirect(reverse('home_view')), name='home'),
    url(r'^index.html$', 'web.views.home.home_view', name='home_view'),
)