import mb_forms.fields as f
import mb_forms.widgets as w
from mb_forms.forms import Form

class JoinTripForm(Form):
    trip_id = f.CharField(max_length=100, widget=w.HiddenInput())
    trip_car = f.BooleanField(required=False, label='Car', help_text='Do you have a car that could be used for this trip? You must have a valid driver license and insurance.')
    trip_gas = f.BooleanField(required=False, label='Gas', help_text='Can you help pay for gas?')

class JoinTripApprovalForm(Form):
    trip_id = f.CharField(max_length=100, widget=w.HiddenInput())
    user_id = f.CharField(max_length=100, widget=w.HiddenInput())
    user_approved = f.BooleanField(required=False, label='Approve User', help_text='Would you like to approve this user to join your trip?')
