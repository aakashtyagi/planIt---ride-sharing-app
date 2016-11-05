from django.shortcuts import render
from django.template import RequestContext, loader
from django.http.response import HttpResponse

def error_500(request):
    t = loader.get_template('errorpages/mb_500.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def error_400(request):
    t = loader.get_template('errorpages/mb_400.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def error_403(request):
    t = loader.get_template('errorpages/mb_403.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def error_404(request):
    t = loader.get_template('errorpages/mb_404.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

