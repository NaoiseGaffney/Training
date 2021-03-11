from django import forms
from .models import Order


"""
Form for orders:
- OrderCreateForm with the fields below for the order creation. A future
feature will pre-populate these fields from the Character Profile.
"""


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
