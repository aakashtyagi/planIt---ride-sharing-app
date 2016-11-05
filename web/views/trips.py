from web.models import Trip
from web.forms.trips.join import JoinTripForm, JoinTripApprovalForm
from mb_forms.views import form_view, new_form_options
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib import messages
from web.forms.trips.edit import EditTripForm, EditTripArriveForm, EditTripStartForm, EditTripReturnAddressForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from web import utils

def trip_edit_general_form(trip):
    nti = dict()
    nti['name'] = trip.name
    nti['descr'] = trip.descr
    nti['members'] = trip.current_members
    nti['members_requested'] = trip.requested_members
    nt = EditTripForm( initial=nti )
    return nt

def trip_edit_departure_form(trip):
    dti = dict()
    dti['start_dt'] = trip.start_dt.date()
    dti['start_tm'] = trip.start_dt.strftime("%H:%M")
    dti['start_address_name'] = trip.start_loc.name
    dti['start_address_1'] = trip.start_loc.address_1
    dti['start_address_2'] = trip.start_loc.address_2
    dti['start_address_city'] = trip.start_loc.address_city
    dti['start_address_state'] = trip.start_loc.address_state
    dti['start_address_postal'] = trip.start_loc.address_postal
    dt = EditTripStartForm( initial=dti )
    return dt

def trip_edit_arrival_form(trip):
    ati = dict()
    ati['arrive_dt'] = trip.arrive_dt.date()
    ati['arrive_tm'] = trip.arrive_dt.strftime("%H:%M")
    ati['arrive_address_name'] = trip.arrive_loc.name
    ati['arrive_address_1'] = trip.arrive_loc.address_1
    ati['arrive_address_2'] = trip.arrive_loc.address_2
    ati['arrive_address_city'] = trip.arrive_loc.address_city
    ati['arrive_address_state'] = trip.arrive_loc.address_state
    ati['arrive_address_postal'] = trip.arrive_loc.address_postal
    at = EditTripArriveForm( initial=ati )
    return at

def trip_edit_return_form(trip):
    rti = dict()
    rti['return_dt'] = trip.return_dt.date()
    rti['return_tm'] = trip.return_dt.strftime("%H:%M")
    rti['return_address_name'] = trip.return_loc.name
    rti['return_address_1'] = trip.return_loc.address_1
    rti['return_address_2'] = trip.return_loc.address_2
    rti['return_address_city'] = trip.return_loc.address_city
    rti['return_address_state'] = trip.return_loc.address_state
    rti['return_address_postal'] = trip.return_loc.address_postal

    rt = EditTripReturnAddressForm( initial=rti )
    return rt

def trip_edit_sanity(request):
    if request.method != "POST":
        return False

    if request.POST.get('id', None) is None:
        return False

    trip_id = request.POST['id']
    t = Trip.objects.filter(id=trip_id).first()
    if t.created_by_id != request.user.id:
        return False

    return True


@login_required()
def trip_edit_general_view(request):
    if trip_edit_sanity(request) is False:
        return HttpResponseRedirect(reverse('home'))

    trip_id = request.POST['id']
    t = Trip.objects.filter(id=trip_id).first()
    t.name = request.POST['name']
    t.descr = request.POST['descr']
    t.requested_members = request.POST['members_requested']
    t.save()
    return HttpResponseRedirect( reverse('trip_edit') + "?id=" + trip_id )

@login_required()
def trip_edit_departure_view(request):
    if trip_edit_sanity(request) is False:
        return HttpResponseRedirect(reverse('home'))
    trip_id = request.POST['id']
    t = Trip.objects.filter(id=trip_id).first()
    t.start_dt = "%s %s" % ( request.POST['start_dt'], request.POST['start_tm']  )
    t.start_loc.name = request.POST['start_address_name']
    t.start_loc.address_1 = request.POST['start_address_1']
    t.start_loc.address_2 = request.POST['start_address_2']
    t.start_loc.address_city = request.POST['start_address_city']
    t.start_loc.address_state = request.POST['start_address_state']
    t.start_loc.address_postal = request.POST['start_address_postal']
    t.start_loc.save()
    t.save()
    return HttpResponseRedirect( reverse('trip_edit') + "?id=" + trip_id )

@login_required()
def trip_edit_arrival_view(request):
    if trip_edit_sanity(request) is False:
        return HttpResponseRedirect(reverse('home'))

    trip_id = request.POST['id']
    t = Trip.objects.filter(id=trip_id).first()
    t.arrive_dt = "%s %s" % ( request.POST['arrive_dt'], request.POST['arrive_tm']  )
    t.arrive_loc.name = request.POST['arrive_address_name']
    t.arrive_loc.address_1 = request.POST['arrive_address_1']
    t.arrive_loc.address_2 = request.POST['arrive_address_2']
    t.arrive_loc.address_city = request.POST['arrive_address_city']
    t.arrive_loc.address_state = request.POST['arrive_address_state']
    t.arrive_loc.address_postal = request.POST['arrive_address_postal']
    t.arrive_loc.save()
    t.save()
    return HttpResponseRedirect( reverse('trip_edit') + "?id=" + trip_id )

@login_required()
def trip_edit_return_view(request):
    if trip_edit_sanity(request) is False:
        return HttpResponseRedirect(reverse('home'))

    trip_id = request.POST['id']
    t = Trip.objects.filter(id=trip_id).first()
    t.return_dt = "%s %s" % ( request.POST['return_dt'], request.POST['return_tm']  )
    t.return_loc.name = request.POST['return_address_name']
    t.return_loc.address_1 = request.POST['return_address_1']
    t.return_loc.address_2 = request.POST['return_address_2']
    t.return_loc.address_city = request.POST['return_address_city']
    t.return_loc.address_state = request.POST['return_address_state']
    t.return_loc.address_postal = request.POST['return_address_postal']
    t.return_loc.save()
    t.save()
    return HttpResponseRedirect( reverse('trip_edit') + "?id=" + trip_id )

@login_required()
def trip_edit_view(request):
    trip_id = request.GET.get('id', None)
    if trip_id is None:
        return HttpResponseRedirect(reverse('home'))
    trip = Trip.objects.filter(id=trip_id).first()
    nt = trip_edit_general_form(trip)
    dt = trip_edit_departure_form(trip)
    at = trip_edit_arrival_form(trip)
    rt = trip_edit_return_form(trip)
    t = loader.get_template('trip_edit.html')
    c = RequestContext(request, {'trip' : trip, 'ntf': nt, 'atf' : at, 'dtf' : dt, 'rtf' : rt})
    return HttpResponse(t.render(c))

@login_required()
def join_trip_view(request):
    trip_id = request.GET.get('id', None)
    if trip_id is None:
        return HttpResponseRedirect(reverse('home'))
    if request.method == "GET":
        trip = Trip.objects.filter(id=trip_id).first()
        if len(trip.party.filter(user_id=request.user.id)):
            messages.add_message(request, messages.INFO, 'You have already requested access to join this trip.')
            return HttpResponseRedirect(reverse('join_trip_requested') + "?id=" + trip_id)

        t = loader.get_template('trip_join.html')
        c = RequestContext(request, {'trip' : trip, 'form' : JoinTripForm( initial={'trip_id' : trip.id})})
        return HttpResponse(t.render(c))
    elif request.method == "POST":
        trip = Trip.objects.filter(id=trip_id).first()
        form = JoinTripForm(request.POST)
        if form.is_valid():
            party = trip.add_to_party(request.user)
            party.gas = form.cleaned_data['trip_gas']
            party.car = form.cleaned_data['trip_car']
            party.save()
            return HttpResponseRedirect(reverse('join_trip_request') + "?id=" + trip_id)
        else:
            t = loader.get_template('trip_join.html')
            c = RequestContext(request, {'trip' : trip, 'form' : form})
            return HttpResponse(t.render(c))

@login_required()
def join_trip_request_view(request):
    trip_id = request.GET.get('id', None)
    if trip_id is None:
        return HttpResponseRedirect(reverse('home'))
    trip = Trip.objects.filter(id=trip_id).first()
    # print "here1"
    utils.send_join_trip_requested_email(request, trip, request.user)
    # print "here2"
    # messages.add_message(request, messages.SUCCESS, 'Your request to join this trip was successfully processed')
    # messages.add_message(request, messages.WARNING, 'Please keep this date open until the trip organizer has processed your request')
    return HttpResponseRedirect(reverse('join_trip_requested') + "?id=" + trip_id)

@login_required()
def join_trip_requested_view(request):
    trip_id = request.GET.get('id', None)
    if trip_id is None:
        return HttpResponseRedirect(reverse('home'))
    trip = Trip.objects.filter(id=trip_id).first()
    t = loader.get_template('trip_join_requested.html')
    c = RequestContext(request, {'trip' : trip})
    return HttpResponse(t.render(c))

@login_required()
def trip_summary_view(request):
    trip_id = request.GET.get('id', None)
    if trip_id is None:
        return HttpResponseRedirect(reverse('home'))
    trip = Trip.objects.filter(id=trip_id).first()
    t = loader.get_template('trip_summary.html')
    c = RequestContext(request, {'trip' : trip})
    return HttpResponse(t.render(c))

@login_required()
def trip_travelers_view(request):
    trip_id = request.GET.get('id', None)
    if trip_id is None:
        return HttpResponseRedirect(reverse('home'))
    trip = Trip.objects.filter(id=trip_id).first()
    t = loader.get_template('trip_travelers.html')
    c = RequestContext(request, {'trip' : trip})
    return HttpResponse(t.render(c))


from datetime import date, timedelta

def view_trips_view(request):
    trips = Trip.objects.all().order_by('-created')
    today = date.today()
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(weeks=1)
    last_month = today - timedelta(weeks=4)
    today_trips = Trip.objects.all().filter(start_dt__gte=today,start_dt__lte=tomorrow)
    weekly_trips = Trip.objects.all().filter(start_dt__gte=today, start_dt__lte=next_week)
    recent_trips = Trip.objects.all().filter(modified__gte=last_month)

    t = loader.get_template('trips_view.html')
    i = dict()
    i['trips'] = trips
    i['recent_trips'] = recent_trips
    i['today_trips'] = today_trips
    i['weekly_trips'] = weekly_trips
#    i['']
    c = RequestContext(request, i)
    return HttpResponse(t.render(c))

@login_required()
def trip_edit_approve_view(request):
    if request.method == "POST":
        trip_id = request.POST['trip_id']
        user_id = request.POST['user_id']
        form = JoinTripApprovalForm(initial={'trip_id' : trip_id, 'user_id' : user_id})
        trip = Trip.objects.filter(id=trip_id).first()
        user = User.objects.filter(id=user_id).first()
        t = loader.get_template('trip_edit_approve.html')
        c = RequestContext(request, {'trip' : trip, 'trip_user' : user, 'trip_form' : form})
        return HttpResponse(t.render(c))
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required()
def trip_do_approve_view(request):
    if request.method == 'POST':
        f = JoinTripApprovalForm(request.POST)
        if f.is_valid():
            if f.cleaned_data['user_approved']:
                trip = Trip.objects.filter(id=f.cleaned_data['trip_id']).first()
                u = trip.party.filter(user_id=f.cleaned_data['user_id']).first()
                user_id = request.POST['user_id']
                user = User.objects.filter(id=user_id).first()
                u.accepted = True
                u.save()
                utils.send_trip_request_accepted_email(request, trip, user)
                # if trip.get_open_seats() == 0:
                #     trip.open = False;
                #     trip.save()
                return HttpResponseRedirect(reverse('trip_details') + "?id=" + f.cleaned_data['trip_id'])
            else:
                return HttpResponseRedirect(reverse('trip_details') + "?id=" + f.cleaned_data['trip_id'])
        else:
            return HttpResponseRedirect(reverse('trip_details') + "?id=" + f.cleaned_data['trip_id'])
    else:
        return HttpResponseRedirect(reverse('home'))