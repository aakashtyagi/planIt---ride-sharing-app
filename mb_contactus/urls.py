from django.conf.urls import patterns, url
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    url(r'^$', lambda x: HttpResponseRedirect( reverse('contact_us_view') ), name='contact_us'),
    url(r'^submit.html$', 'mb_contactus.views.contactus_view', name='contact_us_view'),
    url(r'^success.html$', 'mb_contactus.views.contactus_successs_view', name='contact_us_success'),
)
