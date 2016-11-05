from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

urlpatterns = patterns('web.views.accounts',

     url(r'^login/$', lambda x: HttpResponseRedirect(reverse('auth_login_view')), name='auth_login'),
     url(r'^login.html$', 'facebook_loginview', name='auth_login_view'),

     url(r'^logout/$', lambda x: HttpResponseRedirect(reverse('auth_logout_view')), name='auth_logout'),
     url(r'^logout.html$', 'logout_view', name='auth_logout_view'),

     url(r'^accounts/profile.html$', 'my_profile_view', name='user_profile'),

     # url(r'^signup/$', lambda x: HttpResponseRedirect(reverse('auth_new_account_view')), name='auth_new_account'),
     # url(r'^accounts/signup.html$', 'new_account_view', name='auth_new_account_view'),
     # url(r'^accounts/signup/complete.html$', 'new_account_complete_view', name='auth_new_account_complete'),

     url(r'^trips/update_status', 'my_profile_status_view', name='auth_profile_status'),
     url(r'^trips/update_info', 'edit_profile_view', name='auth_profile_update'),

)

