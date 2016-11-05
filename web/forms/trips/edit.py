import mb_forms.fields as f
import mb_forms.widgets as w
from mb_forms.forms import Form
from django_localflavor_us.forms import USStateSelect

class EditTripForm(Form):
    name = f.CharField(max_length=100, widget=w.TextInput(), label='Trip Name', help_text='Example: New Years Eve Trip to New York')
    descr = f.CharField(max_length=1000, widget=w.Textarea(), label='Trip Description', help_text='')
    members_requested = f.IntegerField(label='Requested Travelers', help_text='Number of people you would like to have in your party.')

class EditTripStartForm(Form):
    start_dt = f.DateField(widget=w.DateInput(), label='Departure Date', help_text='Enter the date your trip will begin.')
    start_tm = f.TimeField(widget=w.TimeInput(), label='Departure Time', help_text='Enter the time your trip will begin.')
    start_address_name = f.CharField(required=True, max_length=50, label='Departure From', help_text='Enter the name where your trip will begin from.')
    start_address_1 = f.CharField(required=True, max_length=50, label='Departure Address', help_text='Enter the address where your trip will begin from.')
    start_address_2 = f.CharField(required=False, max_length=50, label='Departure Address Continued', help_text='Enter additional address information.')
    start_address_city = f.CharField(required=True, max_length=50, label='Departing City', help_text='Enter the city from which your trip will begin.')
    start_address_state = f.CharField(required=True, max_length=50, widget=USStateSelect(), label='Departing State', help_text='Enter the state where your trip will begin.')
    start_address_postal = f.CharField(required=True, max_length=50, label='Departing Postal Code', help_text='Enter the postal code where your trip will begin.')

class EditTripArriveForm(Form):
    arrive_dt = f.DateField(widget=w.DateInput(), label='Arrival Date', help_text='Enter the date you will arrive at your destination')
    arrive_tm = f.TimeField(widget=w.TimeInput(), label='Arrival Time', help_text='Enter the time you will arrive at your destination')
    arrive_address_name = f.CharField(required=True, max_length=50, label='Arrive To', help_text='Enter the name where your trip will arrive at.')
    arrive_address_1 = f.CharField(required=True, max_length=50, label='Arrival Address', help_text='Enter the address you will arrive at.')
    arrive_address_2 = f.CharField(required=False, max_length=50, label='Arrival Address Continued', help_text='Enter additional address information.')
    arrive_address_city = f.CharField(required=True, max_length=50, label='Arriving City', help_text='Enter the city you will arrive at.')
    arrive_address_state = f.CharField(required=True, max_length=50, widget=USStateSelect(), label='Arriving State', help_text='Enter the state you will arrive at.')
    arrive_address_postal = f.CharField(required=True, max_length=50, label='Arriving Postal Code', help_text='Enter the postal code for the arriving area.')
    #arrive_address_country = f5.ChoiceField(required=True, choices=COUNTRIES, label='', help_text='')

class EditTripReturnAddressForm(Form):
    return_dt = f.DateField(widget=w.DateInput(), label='Returning Date', help_text='Enter the date you will leave your destination.')
    return_tm = f.TimeField(widget=w.TimeInput(), label='Returning Time', help_text='Enter the time you will leave your destination')
    return_address_name = f.CharField(required=True, max_length=50, label='Returning Name', help_text='Enter the name where your trip will be returning to.')
    return_address_1 = f.CharField(required=True, max_length=50, label='Returning Address', help_text='Enter the address you will be returning to.')
    return_address_2 = f.CharField(required=False, max_length=50, label='Returning Address Continued', help_text='Enter additional address information.')
    return_address_city = f.CharField(required=True, max_length=50, label='Returning City', help_text='Enter the city you will be returning to.')
    return_address_state = f.CharField(required=True, max_length=50, widget=USStateSelect(), label='Returning State', help_text='Enter the state you will be returning to.')
    return_address_postal = f.CharField(required=True, max_length=50, label='Returning Postal Code', help_text='Enter the postal code you will be returning to.')
    #return_address_country = f5.ChoiceField(required=True, choices=COUNTRIES, label='', help_text='')