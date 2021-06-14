from django.forms import ModelForm, widgets
from django import forms
from credit.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['userKey', 'amount', 'email', 'buyer', 'name']
        widgets = {
            'userKey' : forms.HiddenInput(),
            'name' : forms.HiddenInput()
        }

