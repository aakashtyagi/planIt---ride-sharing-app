from mb_forms.forms import Form
from mb_forms import fields as f
from mb_forms import widgets as w

class ContactUsForm(Form):
    fname = f.CharField(label='First Name:', help_text='Enter your first name', required=True)
    lname = f.CharField(label='Last Name:', help_text='Enter your last name', required=True)
    email = f.CharField(max_length=50, widget=w.EmailInput(), label='Email Address:', help_text='Enter an email address we can contact you at.', required=True)
    phone = f.CharField(max_length=20, widget=w.PhoneNumberInput(), label='Phone Number', help_text='Enter a phone number we can reach you at.')
    question = f.CharField(max_length=200, widget=w.Textarea(), label='Question:', required=True)

    












