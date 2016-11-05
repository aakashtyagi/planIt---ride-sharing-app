from django.shortcuts import render
from django.views import generic
from django.http import response
from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse

def set_last_activity(session, dt):
    session_key = getattr(settings, 'SESSION_LAST_UPDATED_KEY', 'mbwww_last_updated')
    session[session_key] = dt.strftime('%Y-%m-%dT%H:%M:%S.%f')


def get_last_activity(session):
    """
    Get the last activity datetime string from the session and return the
    python datetime object.
    """
    try:
        session_key = getattr(settings, 'SESSION_LAST_UPDATED_KEY', 'mbwww_last_updated')
        return datetime.strptime(session[session_key], '%Y-%m-%dT%H:%M:%S.%f')
    except AttributeError:
        #################################################################
        # * this is an odd bug in python
        # bug report: http://bugs.python.org/issue7980
        # bug explained here:
        # http://code-trick.com/python-bug-attribute-error-_strptime/
        # * sometimes, in multithreaded enviroments, we get AttributeError
        #     in this case, we just return datetime.now(),
        #     so that we are not logged out
        #   "./session_security/middleware.py", in update_last_activity
        #     last_activity = get_last_activity(request.session)
        #   "./session_security/utils.py", in get_last_activity
        #     '%Y-%m-%dT%H:%M:%S.%f')
        #   AttributeError: _strptime
        #
        #################################################################

        return datetime.now()

class LastActivityView(generic.View):

    def __get__(self, request, *args, **kwargs):
        if '_session_security' not in request.session:
            return response.HttpResponse('logout')

        last_activity = get_last_activity(request.sessoin)
        idle_time = (datetime.now() - last_activity).seconds
        return response.HttpResponse(idle_time)




def timeout_view(request):
    return response.HttpResponseRedirect(reverse('login'))


