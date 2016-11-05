from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^$', lambda x: HttpResponseRedirect(reverse('view_trips_view')), name='view_trips'),
    url(r'^all.html$', 'web.views.trips.view_trips_view', name='view_trips_view'),
    url(r'^details.html$', 'web.views.trips.trip_summary_view', name='trip_details'),

    url(r'^edit.html$', 'web.views.trips.trip_edit_view', name='trip_edit'),
    url(r'^edit/general$', 'web.views.trips.trip_edit_general_view', name='trip_edit_general'),
    url(r'^edit/arrival$', 'web.views.trips.trip_edit_arrival_view', name='trip_edit_arrival'),
    url(r'^edit/departure$', 'web.views.trips.trip_edit_departure_view', name='trip_edit_departure'),
    url(r'^edit/return$', 'web.views.trips.trip_edit_return_view', name='trip_edit_return'),
    url(r'^edit/approve_user.html$', 'web.views.trips.trip_edit_approve_view', name='trip_approve'),
    url(r'^edit/do_approval$', 'web.views.trips.trip_do_approve_view', name='trip_do_approve'),
    url(r'^travelers/', 'web.views.trips.trip_travelers_view', name='trip_travelers'),

    url(r'^join.html$', 'web.views.trips.join_trip_view', name='join_trip'),
    url(r'^join/request.html$', 'web.views.trips.join_trip_request_view', name='join_trip_request'),
    url(r'^join/requested.html$', 'web.views.trips.join_trip_requested_view', name='join_trip_requested'),
    url(r'^plan.html$', 'web.views.new_trip.plan_trip_view', name='plan_trip'),
    url(r'^planning/summary.html$', 'web.views.new_trip.plan_trip_summary_view', name='plan_trip_summary'),
)