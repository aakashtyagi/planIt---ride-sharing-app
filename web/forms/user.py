import mb_forms.fields as f
import mb_forms.widgets as w
from mb_forms.forms import Form
from django.forms.fields import ValidationError
from web.models import ActiveEdu

def UserModel():
    try:
        from django.contrib.auth import get_user_model
        return get_user_model()
    except ImportError:
        from django.contrib.auth.models import User
        return User

class NewAccountForm(Form):
    first_name = f.CharField(max_length=30)
    last_name = f.CharField(max_length=30)
    username = f.CharField(max_length=30, error_messages={'username_taken' : 'This username is already used by another account'})
    email = f.CharField(label='Email Address', help_text="Enter your TCU email address",widget=w.EmailInput(), max_length=75, error_messages={'invalid_edu' : 'Please use your TCU email address'})
    password = f.CharField(label='Password', widget=w.PasswordInput(), max_length=30)
    password_2 = f.CharField(label='Confirm Password', widget=w.PasswordInput(), max_length=30, error_messages={'pwd_mismatch' : 'Please confirm your password'})

    def clean_email(self):
        valid_email = False
        email = self.cleaned_data['email']
        for edu in ActiveEdu.objects.all():
            if email.endswith( edu.domain ):
                valid_email = True
        if not valid_email:
            raise ValidationError(self.fields['email'].error_messages['invalid_edu'])
        return email

    def clean_password_2(self):
        pwd_1 = self.cleaned_data['password']
        pwd_2 = self.cleaned_data['password_2']
        if pwd_1 != pwd_2:
            raise ValidationError(self.fields['password_2'].error_messages['pwd_mismatch'])
        return pwd_1

    def clean_username(self):
        username = self.cleaned_data['username']
        res = UserModel().objects.all().filter(username=username)
        if len(res) != 0:
            raise ValidationError(self.fields['username'].error_messages['username_taken'])
        return username

#------------------------FORM UPDATED---------------------------
class ProfileForm(Form):
    first_name = f.CharField(max_length=100, widget=w.TextInput(), label='First Name')
    last_name = f.CharField(max_length=100, widget=w.TextInput(), label='Last Name')
    avatar = f.CharField(label='Profile Picture')
    phone_number = f.IntegerField(label='contact number', help_text='please enter your phone number here')
    email = f.CharField(max_length=100, widget=w.EmailInput(), label='Email Address', error_messages={'invalid_edu' : 'Please use an email address from one of the supported universities.'})
    def clean_email(self):
        valid_email = False
        email = self.cleaned_data['email']
        for edu in ActiveEdu.objects.all():
            if email.endswith( edu.domain ):
                valid_email = True
        if not valid_email:
            raise ValidationError(self.fields['email'].error_messages['invalid_edu'])
        return email


class ProfileEditStatusForm(Form):
    trip_id = f.CharField(widget=w.HiddenInput())
    trip_status = f.CharField(widget=w.HiddenInput())
    trip_question = f.BooleanField(label='Update Trip Status', help_text='Confirm that you would like to make this change to your trip.')

class EmailSignUpForm(Form):
    email = f.CharField(label='@tcu.edu',widget=w.EmailInput(), max_length=75, error_messages={'invalid_edu' : 'Please use your TCU email address'})
    def clean_email(self):
        valid_email = False
        email = self.cleaned_data['email']
        for edu in ActiveEdu.objects.all():
            if email.endswith( edu.domain ):
                valid_email = True
        if not valid_email:
            raise ValidationError(self.fields['email'].error_messages['invalid_edu'])
        return email