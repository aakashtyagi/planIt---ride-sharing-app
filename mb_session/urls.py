from django.conf.urls import patterns, url
from views import LastActivityView

urlpatterns = patterns('',
    url(r'^ping.html$', LastActivityView.as_view(), name='session_security_ping'),
    url(r'^timeout.html', 'mb_session.views.timeout_view', name='session_timeout'),
)
