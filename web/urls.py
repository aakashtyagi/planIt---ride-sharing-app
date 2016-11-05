from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
from mb_errorpages.urls import *

urlpatterns = patterns('',
    url(r'^contactus/', include('mb_contactus.urls')),
    url(r'^sessions/', include('mb_session.urls')),
    url(r'^', include('web.patterns.accounts.urls')),
    url(r'^', include('web.patterns.home.urls')),
    url(r'^', include('web.patterns.misc.urls')),
    url(r'^api/', include('web.patterns.api.urls')),
    url(r'^trips/', include('web.patterns.search.urls')),
    url(r'^trips/', include('web.patterns.trips.urls')),
    url(r'^site/admin/', include(admin.site.urls)),
    url(r'^signup/', 'web.views.accounts.facebook_login', name="signup"),
    url(r'^facebook_javascript_login_sucess/$', 'web.views.accounts.facebook_javascript_login_sucess'),
    url(r'^facebook_email/', 'web.views.accounts._render_user'),
)



