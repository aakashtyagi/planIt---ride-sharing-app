import mb_forms.fields as f
import mb_forms.widgets as w
from mb_forms.forms import Form

class SearchTripsForm(Form):
    name = f.CharField(required=True, max_length=50, label='Trip Name', help_text='Search for trips names containing this.')
    #seats = f.IntegerField(required=False, label='Remaining Open Seats', help_text='Trips with at least this number of remaining seats.')
    #depart = f.DateField(required=True, label='Departure Date', help_text='Trips departing after this date.')
