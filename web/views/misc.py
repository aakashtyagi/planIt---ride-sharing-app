from django.views.generic import TemplateView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from web.models import TripCategory, TripPlaces
from django.shortcuts import render, render_to_response

def about_us_view(request):
    return render(request, 'about_us.html', {})

def facebook_view(request):
    return HttpResponseRedirect('https://www.facebook.com/yallplanit')

def twitter_view(request):
    return HttpResponseRedirect('https://twitter.com/yallplanit')

def pinterest_view(request):
    return HttpResponseRedirect('https://www.pinterest.com/yallplanit')

def privacy_policy(request):
    return render(request, 'privacy-policy.html', {})

def terms_of_use(request):
    return render(request, 'terms-of-use.html', {})

def safety_tips(request):
    return render(request, 'safety-tips.html', {})

def getting_around(request):
    return render(request, 'getting-around.html', {})

def trip_suggestion(request):
	context = RequestContext(request)
	category = TripCategory.objects.all()
	context_dict = {'categories' : category}
	return render_to_response('trip-ideas.html', context_dict, context)

def trip_places(request, anystring=None):
	if anystring:
		context = RequestContext(request)
		places = TripPlaces.objects.filter(category__url_name = anystring)
		category = TripCategory.objects.get(url_name = anystring)
		context_dict = {'places' : places, 'category' : category}
		return render_to_response('trip-places.html', context_dict, context)

	else:
		return HttpResponse("Nothing to show here")


# def free_tickets(request):
#     return render(request, 'free-tickets.html', {})