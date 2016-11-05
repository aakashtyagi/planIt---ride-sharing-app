import mb_forms.fields as f
import mb_forms.widgets as w
from mb_forms.forms import Form
from django.forms.fields import ValidationError
from django_localflavor_us.forms import USStateSelect

class NewTripForm(Form):
    name = f.CharField(max_length=100, widget=w.TextInput(), label='Trip Name', help_text='Example: TCU vs Oklahoma State to Oklahoma')
    descr = f.CharField(max_length=700, widget=w.Textarea(), label='Describe Your Trip', help_text='')
    members = f.IntegerField(label='Current Travelers', help_text='Number of people currently going with you')
    members_requested = f.IntegerField(label='Requested Travelers', help_text='Additional number of people you would like to go with on your trip', error_messages={'invalid_members' : 'You must request at least one additional member to join your trip.'})

    def clean_members_requested(self):
        members = int(self.cleaned_data['members_requested'])
        if members <= 0:
            raise ValidationError(self.fields['members_requested'].error_messages['invalid_members'])
        return self.cleaned_data['members_requested']


class NewTripStartForm(Form):
    start_dt = f.DateField(widget=w.DateInput(), label='Departure Date', help_text='Date of your trip')
    start_tm = f.TimeField(widget=w.TimeInput(), label='Departure Time', help_text='Expected time of departure')
    start_address_name = f.CharField(required=True, max_length=50, label='Departing Place', help_text='Where are you leaving from?')
    start_address_1 = f.CharField(required=True, max_length=50, label='Departure Address', help_text='Address of the departure place')
    start_address_2 = f.CharField(required=False, max_length=50, label='Departure Address Continued', help_text='Additional address information')
    start_address_city = f.CharField(required=True, max_length=50, label='Departing City', help_text='Enter the city from which your trip will begin')
    start_address_state = f.CharField(required=True, max_length=50, widget=USStateSelect(), label='Departing State', help_text='Enter the state where your trip will begin')
    start_address_postal = f.CharField(required=True, max_length=50, label='Departing Postal Code', help_text='Enter the postal code where your trip will begin')
    #start_address_country = f5.ChoiceField(required=True, choices=COUNTRIES, label='Departing Country', help_text='Select the country where your trip will begin.')

class NewTripArriveForm(Form):
    arrive_dt = f.DateField(widget=w.DateInput(), label='Arrival Date', help_text='Arrival date at the destination')
    arrive_tm = f.TimeField(widget=w.TimeInput(), label='Arrival Time', help_text='Expected time of arrival')
    arrive_address_name = f.CharField(required=True, max_length=50, label='Arrive To', help_text='Where are you arriving at?')
    arrive_address_1 = f.CharField(required=True, max_length=50, label='Arrival Address', help_text='Address of the place you will arrive at')
    arrive_address_2 = f.CharField(required=False, max_length=50, label='Arrival Address Continued', help_text='Additional address information.')
    arrive_address_city = f.CharField(required=True, max_length=50, label='Arriving City', help_text='Enter the city you will arrive at')
    arrive_address_state = f.CharField(required=True, max_length=50, widget=USStateSelect(), label='Arriving State', help_text='Enter the state you will arrive at')
    arrive_address_postal = f.CharField(required=True, max_length=50, label='Arriving Postal Code', help_text='Enter the postal code for the arriving area')
    #arrive_address_country = f5.ChoiceField(required=True, choices=COUNTRIES, label='', help_text='')

class NewTripReturnForm(Form):
    return_dt = f.DateField(widget=w.DateInput(), label='Returning Date', help_text='Date you will leave your destination')
    return_tm = f.TimeField(widget=w.TimeInput(), label='Returning Time', help_text='Time you will leave your destination')
    return_home = f.BooleanField(required=False, label='Returning Home', help_text='Will you be returning to your starting location or to a different address?')
    trip_car = f.BooleanField(required=False, label='Car', help_text='Do you have a car that could be used for this trip? You must have a valid driver license and insurance.')
    trip_gas = f.BooleanField(required=False, label='Gas', help_text='Can you help pay for gas?')

class NewTripReturnAddressForm(Form):
    return_address_name = f.CharField(required=True, max_length=50, label='Returning Name', help_text='Enter the name where your trip will be returning to')
    return_address_1 = f.CharField(required=True, max_length=50, label='Returning Address', help_text='Enter the address you will be returning to')
    return_address_2 = f.CharField(required=False, max_length=50, label='Returning Address Continued', help_text='Enter additional address information')
    return_address_city = f.CharField(required=True, max_length=50, label='Returning City', help_text='Enter the city you will be returning to')
    return_address_state = f.CharField(required=True, max_length=50, widget=USStateSelect(), label='Returning State', help_text='Enter the state you will be returning to')
    return_address_postal = f.CharField(required=True, max_length=50, label='Returning Postal Code', help_text='Enter the postal code you will be returning to')
    #return_address_country = f5.ChoiceField(required=True, choices=COUNTRIES, label='', help_text='')