from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from mb_forms.views import SecureFormView, FormView
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from mb_forms.views import *

def mb_info_message(request, message):
    messages.add_message(request, messages.INFO, message)

def mb_debug_message(request, message):
    messages.add_message(request, messages.DEBUG, message)

def mb_warning_message(request, message):
    messages.add_message(request, messages.WARNING, message)

def mb_success_message(request, message):
    messages.add_message(request, messages.SUCCESS, message)


def mb_template_view(request, template, context=dict()):
    t = loader.get_template(template)
    c = RequestContext(request, context)
    return HttpResponse(t.render(c))