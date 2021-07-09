from django import forms

from customer.models import Customer


class CustomerForm(forms.ModelForm):
    def __init__(self):
        super(CustomerForm, self).__init__()
        self.fields['name'].widget.attrs.update({'placeholder': 'Customer Name'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Customer Phone No.'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Customer Email'})

    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'email']
