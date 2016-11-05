from django.http.response import HttpResponse
from django.template import RequestContext, loader
from web.models import Trip


def home_view(request):
    if request.user.is_authenticated():
        trips = Trip.objects.all().order_by('-created')[:5]
        t = loader.get_template('home.html')
        c = RequestContext(request, {'trips' : trips})
        return HttpResponse(t.render(c))
    else:
        t = loader.get_template('home_public.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))





