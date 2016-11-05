from django.contrib.auth.forms import AuthenticationForm
from mb_forms.views import FormView
from mb_views.views import *
from django.contrib.auth.models import User
from web import utils
from django.contrib.auth import login, logout, authenticate
from web.forms.user import NewAccountForm, ProfileEditStatusForm, EmailSignUpForm
from web.models import ActiveEdu, Trip
from mb_forms.views import SecureFormView
from web.forms.user import ProfileForm
from web.utils import send_profile_updated_email, new_account_created_email
from pyfb import Pyfb
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from web.settings import FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY
from web.models import UserProfile
import requests, json
from web.settings import NUMVERIFY_KEY


def UserModel():
    try:
        from django.contrib.auth import get_user_model
        return get_user_model()
    except ImportError:
        from django.contrib.auth.models import User
        return User

class LoginView(FormView):
    title = 'Account Login'
    subtitle = 'Please complete the form below to login to your account.'
    form_class = AuthenticationForm
    template_name = 'login_form.html'

    def process_data(self, data, request, form):
        # print "fuck you"        
        login(request, form.get_user())
        return True

class LogoutView(FormView):
    title = 'Are you sure you want to log out?'
    success_url = 'home'
    template_name = 'logout.html'

    def process_data(self, data, request, form):
        logout(request)
        return True

class NewAccountView(FormView):
    title = 'Create an account'
    subtitle = 'Complete the form below to create your free account'
    form_class = NewAccountForm
    template_name = 'new_account_form.html'
    success_url = 'auth_new_account_complete'

    def get_template_options(self, request, options):
        z = options.copy()
        z['edus'] = ActiveEdu.objects.all()
        return z

    def process_data(self, data, request, form):
        u = UserModel().objects.create_user(username=data['username'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
        u.email = data['email']
        u.set_password(data['password'])
        u.save()
        utils.new_account_created_email(request, u)
        u = authenticate(username=data['username'], password=data['password'])
        login(request, u)
        return True

class NewAccountCompleteView(FormView):
    title = 'Your account has been created'
    subtitle = 'You can now create and join trips'
    success_url = 'home'

    def process_data(self, data, request, form):
        return True

logout_view = LogoutView.as_view()
login_view = LoginView.as_view()
new_account_view = NewAccountView.as_view()
new_account_complete_view = NewAccountCompleteView.as_view()

#-----------------------------------This is for when you EDIT THE PROFILE---------------------
class ProfileView(SecureFormView):
    form_class = ProfileForm
    title = 'My Profile'
    subtitle = 'Edit user profile information'
    success_url = 'user_profile'

    def get_initial(self, request):
        i = dict()
        i['first_name'] = request.user.first_name
        i['last_name'] = request.user.last_name
        i['email'] = request.user.email
        i['phone_number'] = request.user.userprofile.phone_number
        print "I'm in get_initial"
        return i

    def process_data(self, data, request, form):
        request.user.first_name = data['first_name']
        request.user.last_name = data['last_name']
        request.user.email = data['email']
        # request.user.userprofile.phone_number = data['phone_number']
        #-----------------------NUMVERIFY API Code---------------------------
        user_required = UserProfile.objects.get(user=request.user)
        key = NUMVERIFY_KEY
        number = "1"+ str(data['phone_number'])
        url = "http://apilayer.net/api/validate?access_key="+key+"&number="+number
        myResponse = requests.get(url)
        if myResponse.ok:
            jData = json.loads(myResponse.content)
        else:
            myResponse.raise_for_status()
        if jData['valid'] == True:
            user_required.phone_number = data['phone_number']
            user_required.save()
        else:
            print "bad phone number"
            return my_profile_view(request) 
        #-----------------------------------------------------------------------
        #------------------PROFILE PICTURE CODE---------------------------------

        request.user.save()
        print "data saved"
        # return True
        try:
            pass
            # send_profile_updated_email(request.user)
            # print "i'm in try"
        except:
            pass
        return True
        # return HttpResponseRedirect('/')

edit_profile_view = ProfileView.as_view()


@login_required()
def my_profile_view(request):
    context = dict()
    i = dict()
    i['first_name'] = request.user.first_name
    i['last_name'] = request.user.last_name
    i['email'] = request.user.email
    try:
        phone_number = request.user.userprofile.phone_number
        i['phone_number'] = phone_number
    except:
        pass
    
    
    print "my_profile_view"
    # print request.user.last_name
    print "something"
    context['profile_form'] = ProfileForm(initial=i)
    context['profile_trips'] = Trip.objects.filter(created_by=request.user.id)
    return mb_template_view(request, template='my_profile.html', context=context)



class ProfileStatusView(SecureFormView):
    title = 'Change Status'
    subtitle = 'Change trip status'
    form_class = ProfileEditStatusForm
    success_url = 'user_profile'

    def get_initial(self, request):
        i = dict()
        trip_id = request.POST['trip_id']
        trip_status = request.POST.get('trip_question', None)
        trip = Trip.objects.filter(id=trip_id).first()

        if trip.open:
            self.title = 'Hide users from viewing this trip.'
            self.subtitle = '%s is visible to other viewers.' % trip.name

        else:
            self.title = 'Allow users to view this trip.'
            self.subtitle = '%s is not visible to other users. Select the checkbox to allow other users to view and join this trip.' % trip.name

        return i

    def process_data(self, data, request, form):
        trip_id = request.POST['trip_id']
        trip = Trip.objects.filter(id=trip_id).first()
        if trip.open:
            trip.open = False
            ## send email
        else:
            trip.open = True
            ## send email
        trip.save()
        return True

my_profile_status_view = ProfileStatusView.as_view()

# def local_signup(request):
    

#     return render(request, 'facebook_login.html', {'accountform': accountform})
def facebook_loginview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

#---------------------NEW USERPROFILE CODE ADDED HERE---------------------

            want_profile = 1
            user_profiles = UserProfile.objects.all()
            user_required = User.objects.get(username=username)
            for profile in user_profiles:
                if profile.user.username == request.user.username:
                    want_profile = 0
            if want_profile == 1:
                new_profile = UserProfile()
                new_profile.user = user_required
                try:
                    new_profile.save()
                except:
                    print "didn't save the user profile"
                    pass

            u = authenticate(username=username, password=password)
            login(request, u)
                # return True
            return HttpResponseRedirect('/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()
    return render_to_response("login_form.html", {"FACEBOOK_APP_ID": FACEBOOK_APP_ID, 'form':form}, RequestContext(request))


def facebook_login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        accountform = NewAccountForm(request.POST)
        # check whether it's valid:
        if accountform.is_valid():
            username = accountform.clean_username()
            password = accountform.clean_password_2()
            first_name = accountform.cleaned_data['first_name']
            last_name = accountform.cleaned_data['last_name']
            email = accountform.clean_email()
            u = UserModel().objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            # u.email = email
            # u.set_password(password)
            # print password
            u.save()
            # utils.new_account_created_email(request, u)
            u = authenticate(username=username, password=password)
            login(request, u)
                # return True
            return HttpResponseRedirect('/')

        # if a GET (or any other method) we'll create a blank form
    else:
        accountform = NewAccountForm()
    return render_to_response("signup.html", {"FACEBOOK_APP_ID": FACEBOOK_APP_ID, 'accountform':accountform}, RequestContext(request))

    #Login with the js sdk and backend queries with pyfb
def facebook_javascript_login_sucess(request):

    access_token = request.GET.get("access_token")
    # print "printing access token"
    facebook = Pyfb(FACEBOOK_APP_ID)
    facebook.set_access_token(access_token)

    user_id = "https://graph.facebook.com/me?access_token="+str(access_token)
    UID = requests.get(user_id)
    # print UID
    if UID.ok:
        jData = json.loads(UID.content)
        UID = jData['id']

    print str(UID) #print FACEBOOK USER ID
    url = "http://graph.facebook.com/v2.7/"+str(UID)+"/picture?redirect=false"
    print url
    myResponse = requests.get(url)
    print myResponse
    if myResponse.ok:
        jData = json.loads(myResponse.content)
        data = jData['data']
        pic_url = data['url'] #Profile Picture
        print pic_url
    else:
        myResponse.raise_for_status()
        print "error"
    photos = facebook.get_photos()
    print "These are my photos:\n"

    facebook_user = True
    users = User.objects.all()
    me = facebook.get_myself()
    fullname = me.name.split()
    first_name = str(fullname[0])
    last_name = str(fullname[1])
    fullname = first_name + last_name
    if User.objects.filter(username=fullname).exists():
        u = authenticate(username=fullname, password=fullname)
        user_profile = UserProfile.objects.get(user=)
        login(request, u)
        return HttpResponseRedirect('/')
    else:
        return _render_user(facebook, facebook_user, request)

def _render_user(facebook, facebook_user, request):
    if facebook_user == True:
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
            form = EmailSignUpForm(request.POST)
        # check whether it's valid:
            if form.is_valid():
                me = facebook.get_myself()
                fullname = me.name.split()
                first_name = str(fullname[0])
                last_name = str(fullname[1])
                fullname = first_name + last_name
                email = form.clean_email()

                u = User.objects.create_user(username=fullname, email=email, first_name=first_name, last_name=last_name,password=fullname)
                u.save()
                    # print "User is saved"
                utils.new_account_created_email(request, u)
                u = authenticate(username=fullname, password=fullname)
                if not u.is_authenticated():
                    print "User is not authenticated"
                login(request, u)
                # print "Logged in"
                return HttpResponseRedirect('/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = EmailSignUpForm()

        return render(request, 'facebook_email.html', {'form': form})


































