from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.flatpages import views as flatviews

urlpatterns = patterns('',
	url(r'^getting-around/', 'web.views.misc.getting_around', name="getting-around"),
	url(r'^privacy-policy/', 'web.views.misc.privacy_policy', name="privacy-policy"),
	url(r'^terms-of-use/', 'web.views.misc.terms_of_use', name="terms-of-use"),
	url(r'^safety-tips/', 'web.views.misc.safety_tips', name="safety-tips"),
    url(r'^facebook.html$', 'web.views.misc.facebook_view', name='link_facebook'),
    url(r'^twitter.html$', 'web.views.misc.twitter_view', name='link_twitter'),
    url(r'^pinterest.html$', 'web.views.misc.pinterest_view', name='link_pinterest'),
    url(r'^about-us/', 'web.views.misc.about_us_view', name='about_us'),
    url(r'^trip-ideas/', 'web.views.misc.trip_suggestion', name='trip-ideas'),
    # url(r'^trip-ideas/(?P<anystring>\w+)/$', 'web.views.misc.trip_places', name='trip-places'),
    url(r'^ideas/(?P<anystring>.+)/$', 'web.views.misc.trip_places', name='trip-places'),
    # url(r'^free-tickets/', 'web.views.misc.free_tickets', name='free_tickets'),
)