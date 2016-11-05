from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from web.forms.search import SearchTripsForm
from web.models import Trip
from mb_forms.views import form_view, new_form_options
from django.contrib.auth.decorators import login_required

def search_trips(seats=None, name=None, departs=None):
    trips = Trip.objects.all()
    if seats:
        trips = trips.extra(select={'num_open' : 'requested_members-current_members'}).annotate()
        trips = trips.extra(where=['num_open > %d' % (seats)])
    if name:
        trips = trips.filter(name__contains=name)

    trips = trips.filter(start_dt__gte=departs).order_by('-start_dt')
    return trips

@login_required()
def search_trips_view(request):
    if request.method == 'POST':
        form = SearchTripsForm(request.POST)
        if form.is_valid():
            t = loader.get_template('search_results.html')
            c = RequestContext(request, {'search_form' : form})
            return HttpResponse(t.render(c))
        else:
            return form_view(request, new_form_options('Search Trips', 'Search existing trips.', form))
    else:
        return form_view(request, new_form_options('Search Trips', 'Search existing trips.', SearchTripsForm(initial={'seats': 1})))



