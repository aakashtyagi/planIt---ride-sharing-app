from datetime import timedelta
from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from views import get_last_activity, set_last_activity
from datetime import datetime




class MacrobitsMiddlewareSession():

    def is_passive_request(self, request):
        return request.path in settings.SESSION_PASSIVE_URLS

    def process_request(self, request):
        """ Update last activity time or logout. """
        if not request.user.is_authenticated():
            return

        now = datetime.now()
        self.update_last_activity(request, now)

        delta = now - get_last_activity(request.session)
        max_idle = getattr(settings, 'SESSION_EXPIRE_AFTER', 600)
        if delta >= timedelta(seconds=max_idle):
            logout(request)
            return HttpResponseRedirect(reverse('session_timeout'))
        else:
            set_last_activity(request.session, now)

    def update_last_activity(self, request, now):
        """
        If ``request.GET['idleFor']`` is set, check if it refers to a more
        recent activity than ``request.session['_session_security']`` and
        update it in this case.
        """

        session_key = getattr(settings, 'SESSION_LAST_UPDATED_KEY', 'mbwww_last_updated')
        if session_key not in request.session:
            set_last_activity(request.session, now)

        last_activity = get_last_activity(request.session)
        server_idle_for = (now - last_activity).seconds

        if (request.path == reverse('session_security_ping') and 'idleFor' in request.GET):
            # Gracefully ignore non-integer values
            try:
                client_idle_for = int(request.GET['idleFor'])
            except ValueError:
                return

            # Disallow negative values, causes problems with delta calculation
            if client_idle_for < 0:
                client_idle_for = 0

            if client_idle_for < server_idle_for:
                # Client has more recent activity than we have in the session
                last_activity = now - timedelta(seconds=client_idle_for)

                # Update the session
                set_last_activity(request.session, last_activity)