from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

def send_email_template(template_name, context, subject, recipient):
    plaintext = get_template('email/%s/%s.txt' % (template_name, template_name))
    html = get_template('email/%s/%s.html' % (template_name, template_name))
    d = Context(context)
    subject, from_email, to = subject, getattr(settings, 'DEFAULT_FROM_EMAIL'), recipient
    text_content = plaintext.render(d)
    html_content = html.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_join_trip_requested_email(request, trip, user):
    c = dict()
    c['username'] = user.username
    c['trip_name'] = trip.name
    c['trip_url'] = 'www.yallplanit.com' + reverse('trip_edit') + "?id=%s" % trip.id
    send_email_template('join_trip', c, 'Request to join %s' % trip.name, trip.created_by.email)


def send_profile_updated_email(user):
    send_email_template('profile_update', dict(), 'planIt profile updated', user.email)

def send_new_trip_created_email(request, trip, user):
    c = dict()
    c['username'] = user.username
    c['trip_name'] = trip.name
    send_email_template('trip_created', c, '%s successfully created' % trip.name, trip.created_by.email)

def send_trip_request_accepted_email(request, trip, user):
    c = dict()
    c['trip_name'] = trip.name
    send_email_template('join_approval', c, '%s request accepted!' % trip.name, user.email)

def new_account_created_email(request, user):
    c = dict()
    c['username'] = user.first_name
    # print "Sending email"
    send_email_template('new_account', c, 'Welcome to planIt!', user.email)