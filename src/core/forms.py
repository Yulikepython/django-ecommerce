from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ("S", "Strip"),
    ("P", "PayPal"),

)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={"placehoder": "1234 Main St", "id": "street_address"}))
    apartment_address = forms.CharField(required=False)
    country = CountryField(blank_label="(select country)")
    zip_code = forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_CHOICES)

