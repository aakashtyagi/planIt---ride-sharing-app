from mb_api.response import Response
from mb_api.decorators import api_view
from web.models import Trip
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

@api_view()
def search_view(request, format=None):
    count = request.GET['rowCount']
    current = request.GET['current']
    sort = request.GET.get('sort', None)
    name = request.GET.get('name', None)
    query = Trip.objects.all()
    if name:
        query = query.filter(name__icontains=name)

    p = Paginator(query, count)
    trips = p.page(current)
    res_data = list()
    for trip in trips:
        data = dict()
        data['id'] = str(trip.id)
        data['name'] = "<a href='%s'>%s</a>" % (reverse('trip_details') + "?id=" + trip.id, trip.name)
        data['start'] = trip.start_dt.date()
        data['destination'] = "%s %s %s" % (trip.arrive_loc.name, trip.arrive_loc.address_city, trip.arrive_loc.address_state)
        data['return'] = trip.return_dt.date()
        res_data.append(data)
    res = dict()
    res['current'] = int(current)
    res['rowCount'] = count
    res['rows'] = res_data
    res['total'] = p.count
    return Response(res)

search_api = search_view