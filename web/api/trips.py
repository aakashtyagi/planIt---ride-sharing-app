from mb_api.views import APIView
from mb_tables.views import TableApi
from web.models import Trip
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.shortcuts import render

class UserTripApi(TableApi):

    def get_queryset(self, request):
        return Trip.objects.filter(created_by=request.user.id)

    def get_rows(self, queryset, request):
        data = list()
        for trip in queryset:
            row = dict()
            row['id'] = trip.id
            row['name'] = "<a href='%s?id=%s'>%s</a>" % (reverse('trip_details'), trip.id, trip.name)
            row['open'] = self.get_trip_status_button(trip, request)
            row['start_dt'] = trip.start_dt
            row['arrive_dt'] = trip.arrive_dt
            row['return_dt'] = trip.return_dt
            data.append(row)

        return data

    def get_trip_status_button(self, trip, request):
        html = ''
        csrf_token = csrf(request)['csrf_token']
        csrf_token = unicode(csrf_token)
        if trip.open:
            html += '<form action="%s" method="post" enctype="multipart/form-data">' % reverse('auth_profile_status')
            html += '<input type="hidden" name="csrfmiddlewaretoken" value="%s">' % csrf_token
            html += '<input type="hidden" name="trip_id" value="%s">' % trip.id
            html += '<input type="submit" name="trip_status" value="Close Trip" class="btn"/>'
            html += '</form>'
        else:
            html += '<form action="%s" method="post" enctype="multipart/form-data">' % reverse('auth_profile_status')
            html += '<input type="hidden" name="csrfmiddlewaretoken" value="%s">' % csrf_token
            html += '<input type="hidden" name="trip_id" value="%s">' % trip.id
            html += '<input type="submit" name="trip_status" value="Open Trip" class="btn"/>'
            html += '</form>'
        return html

user_trip_api = UserTripApi.as_view()