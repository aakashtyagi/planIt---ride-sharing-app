import os
from web import utils
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from mb_forms.views import form_view, new_form_options
from mb_forms.views import SecureFormView
from web.models import Trip, Location
from web.forms.trips.new import NewTripForm, NewTripStartForm, NewTripArriveForm, NewTripReturnForm, NewTripReturnAddressForm
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from datetime import datetime
from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def new_trip_return_home_condition(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('3') or {}
    value =  cleaned_data.get('return_home', True)
    return not value


class PlanTripWizard(SessionWizardView):
    form_list = [NewTripForm, NewTripStartForm, NewTripArriveForm, NewTripReturnForm, NewTripReturnAddressForm]
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PlanTripWizard, self).dispatch(request, *args, **kwargs)


    def get_form_initial(self, step):
        if int(step)==1:
            return { 'start_dt': datetime.now().date(), 'start_tm' : datetime.now().time().strftime("%H:%M") }
        elif int(step)==2:
            return { 'arrive_dt': datetime.now().date(), 'arrive_tm' : datetime.now().time().strftime("%H:%M") }
        elif int(step)==3:
            return { 'return_dt': datetime.now().date(), 'return_tm' : datetime.now().time().strftime("%H:%M") }
        return {}

    def done(self, form_list, **kwargs):
        # for f in form_list:
        #     print f.cleaned_data
        
        default_dt = datetime.utcfromtimestamp(0)
        data = form_list[0].cleaned_data
        nt = Trip()
        nt.created_by = self.request.user
        self.request.session['new_trip_id'] = str(nt.id)
        nt.name = data['name']
        nt.descr = data['descr']
        nt.current_members = data['members']
        nt.requested_members = data['members_requested']

        data = form_list[1].cleaned_data
        nt.start_dt = "%s %s" % (data.get('start_dt', default_dt.date()), data.get('start_tm', default_dt.time()))
        # nt.start_dt = "%s %s" % (data.get('start_dt', None), data.get('start_tm', None))
        # nt.start_dt = data.get('start_dt')
        # nt.start_dt = "%s %s" % (data.get('start_dt', start_dt.date()), data.get('start_tm', start_dt.strftime("%H:%M")))
        # nt.start_dt = "%s %s" % (data['start_dt'], data['start_tm'])
        # print "time is:" data['start_dt']
        # print "time is:" data.get('start_dt', default_dt.date())
        st = Location()
        st.name = data.get('start_address_name', None)
        st.address_1 = data.get('start_address_1', None)
        st.address_2 = data.get('start_address_2', None)
        st.address_city = data.get('start_address_city', None)
        st.address_state = data.get('start_address_state', None)
        st.address_postal = data.get('start_address_postal', None)
        st.save()
        nt.start_loc = st

        data = form_list[2].cleaned_data
        nt.arrive_dt = "%s %s" % (data.get('arrive_dt', default_dt.date()), data.get('arrive_tm', default_dt.time()))
        ar = Location()
        ar.name = data.get('arrive_address_name', None)
        ar.address_1 = data.get('arrive_address_1', None)
        ar.address_2 = data.get('arrive_address_2', None)
        ar.address_city = data.get('arrive_address_city', None)
        ar.address_state = data.get('arrive_address_state', None)
        ar.address_postal = data.get('arrive_address_postal', None)
        ar.save()
        nt.arrive_loc = ar

        data = form_list[3].cleaned_data
        nt.return_dt = "%s %s" % (data.get('return_dt', default_dt.date()), data.get('return_tm', default_dt.time()))
        nt.return_home = data.get('return_home', True)
        gas = data.get('trip_gas')
        car = data.get('trip_car')


        if nt.return_home:
            nt.return_loc = st
        else:
            data = form_list[4].cleaned_data
            rt = Location()
            rt.name = data.get('return_address_name', None)
            rt.address_1 = data.get('return_address_1', None)
            rt.address_2 = data.get('return_address_2', None)
            rt.address_city = data.get('return_address_city', None)
            rt.address_state = data.get('return_address_state', None)
            rt.address_postal = data.get('return_address_postal', None)
            rt.save()
            nt.return_loc = rt

        nt.open = False
        nt.save()
        # nt.add_to_party(self.request.user, True)
        nt.add_gas_car(self.request.user, gas, car, True)

        return HttpResponseRedirect( "%s?id=%s" % (reverse('plan_trip_summary'), str(nt.id)))

    def get_template_names(self):
        return "wizard_form.html";

plan_trip_view = PlanTripWizard.as_view(condition_dict={'4': new_trip_return_home_condition})

def plan_trip_summary_view(request):
    if request.method == "GET":
        id = request.GET.get('id', None)
        if id is None:
            return HttpResponseRedirect(reverse('home'))
        nt = Trip.objects.filter(id=id).first()
        t = loader.get_template('new_trip_summary.html')
        c = RequestContext(request, {'trip' : nt})
        return HttpResponse(t.render(c))
    else:
        id = request.GET.get('id', None)
        if id is None:
            return HttpResponseRedirect(reverse('home'))
        nt = Trip.objects.filter(id=id).first()
        if nt.created_by == request.user:
            nt.open = True
            nt.save()
            utils.send_new_trip_created_email(request, nt, request.user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('home'))

