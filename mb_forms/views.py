from django.forms import Form
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.conf import settings
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from mb_forms.forms import Form
from django.core.urlresolvers import reverse
from django.contrib.formtools.preview import FormPreview

def new_form_options(title='', subtitle='', form=Form()):
    options = dict()
    options['page_title'] = title
    options['page_subtitle'] = subtitle
    options['page_submit'] = 'Continue'
    options['page_cancel'] = 'Back'
    options['page_form'] = form
    return options

def form_view(request, options=new_form_options()):
    default_form_name = getattr(settings, 'FORM_VIEW_TEMPLATE', 'forms/mb_form_view.html')
    form_name = options.get('template', default_form_name)
    if form_name is None:
        form_name = default_form_name
    t = loader.get_template(form_name)
    c = RequestContext(request, options)
    return HttpResponse(t.render(c))

class PreviewFormView(FormPreview):
    preview_template = 'forms/preview_form_preview.html'
    form_template = 'forms/preview_form.html'

    def done(self, request, cleaned_data):
        return HttpResponseRedirect(reverse('home'))

class FormView(FormView):
    title = 'Form'
    subtitle = 'Please complete the form below'
    success_url_revered = False

    def get_success_url(self, request):
        if self.success_url and self.success_url_revered == False:
            return reverse(self.success_url)
        if self.success_url and self.success_url_revered == True:
            return self.success_url
        elif request.GET.get('next', None):
            return request.GET['next']
        else:
            return reverse('home')

    def get_initial(self, request):
        return super(FormView, self).get_initial()

    def get_form(self, form_class, request):
        return form_class(**self.get_form_kwargs(request))

    def get_form_kwargs(self, request):
        kwargs = {
            'initial': self.get_initial(request),
            'prefix': self.get_prefix(),
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_form_class(self):
        if self.form_class is None:
            self.form_class = Form
        return self.form_class

    def render_form_options(self, form, request):
        form_options = new_form_options(self.title, self.subtitle, form)
        form_options['template'] = self.template_name
        return form_view(request, options=self.get_template_options(request, form_options))

    def get_template_options(self, request, options):
        return options

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class, request)
        return self.render_form_options(form, request)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class, request)
        if form.is_valid():
            if self.process_data(form.cleaned_data, request, form):
                return self.form_valid(form, request)
            else:
                return self.form_invalid(form, request)
        else:
            return self.form_invalid(form, request)

    def process_data(self, data, request, form):
        return False

    def form_valid(self, form, request):
        return HttpResponseRedirect(self.get_success_url(request))

    def form_invalid(self, form, request):
        return self.render_form_options(form, request)


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class SecureFormView(FormView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SecureFormView, self).dispatch(*args, **kwargs)
