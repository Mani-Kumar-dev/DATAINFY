from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    company_name = forms.CharField(max_length=100)
    work_email = forms.EmailField()
    phone_type_choices = [
        ('business', 'Business'),
        ('personal', 'Personal'),
    ]
    phone_type = forms.ChoiceField(choices=phone_type_choices)
    phone_number = forms.CharField(max_length=15)
    job_title = forms.CharField(max_length=100)
    department = forms.CharField(max_length=100)
    job_role = forms.CharField(max_length=100)
    country_choices = [
        # Add your country choices here
        ('us', 'United States'),
        ('ca', 'Canada'),
        # Add more countries as needed
    ]
    country = forms.ChoiceField(choices=country_choices)
    state_choices = [
        # Add your state choices here
        ('ca', 'California'),
        ('ny', 'New York'),
        # Add more states as needed
    ]
    state = forms.ChoiceField(choices=state_choices)
    city_choices = [
        # Add your city choices here
        ('la', 'Los Angeles'),
        ('nyc', 'New York City'),
        # Add more cities as needed
    ]
    city = forms.ChoiceField(choices=city_choices)
    zip_code = forms.CharField(max_length=10)
    address = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
