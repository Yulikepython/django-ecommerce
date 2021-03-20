from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import BillingAddress

PAYMENT_CHOICES = (
    ("S", "Stripe"),
    ("P", "PayPal"),

)

class CheckoutForm(forms.ModelForm):
    street_address = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "1234 Main St"}))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Apartment or suite"}))
    country = CountryField(blank_label="(select country)").formfield(widget=CountrySelectWidget(attrs={
                        "class":"custom-select d-block w-100"
                        }))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_CHOICES)

    class Meta:
        model = BillingAddress
        exclude = ['user']

    def __init__(self, login_user, *args, **kwargs):
        self.login_user = login_user
        super().__init__(*args, **kwargs)
        
