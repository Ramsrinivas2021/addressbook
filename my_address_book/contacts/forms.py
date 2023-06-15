from django import forms
from .models import Person, Address

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address']
