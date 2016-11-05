from mb_forms.views import form_view, new_form_options
from mb_contactus.forms import ContactUsForm
from django.conf import settings
from pydoc import locate
from mb_forms.views import FormView
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

MB_QUESTION_KEY='mb_question_id'

class ContactUsView(FormView):
    form_class = ContactUsForm
    title = 'Contact Us'
    success_url = 'contact_us_success'

    def get_form_class(self):
        cls_name = getattr(settings, 'CONTACT_US_FORM', 'mb_contactus.forms.ContactUsForm')
        cls = locate(cls_name)
        return cls

    def process_data(self, data, request, form):
        email_from = getattr(settings, 'DEFAULT_FROM_EMAIL', 'postmaster@macrobits.com')
        email_to = getattr(settings, 'CONTACT_US_EMAIL', 'postmaster@macrobits.com')

        html = "Full Name: %s\n" % data['name']
        html += "Email: %s\n" % data['email']
        html += "Question: %s" % data['question']

        send_mail('Contact Us Question', html, email_from, [email_to], fail_silently=False)
        request.session[MB_QUESTION_KEY] = data
        return True

class ContactUsSuccessView(TemplateView):
    template_name = 'mb_contactus/success.html'

    def get(self, request, *args, **kwargs):
        id = request.session.get(MB_QUESTION_KEY, None)
        if not id:
            return HttpResponseRedirect( reverse('contact_us') )
        else:
            del request.session[MB_QUESTION_KEY]
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


contactus_view = ContactUsView.as_view()
contactus_successs_view = ContactUsSuccessView.as_view()