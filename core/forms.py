from django import forms
from core.models import CreditCard

class CreditCardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Card Holder Name'}))
    number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Card Number'}))
    month = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Expiry Month'}))
    year = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Expiry Year'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'placeholder': 'CVV'}))
    
    class Meta:
        model = CreditCard
        fields = ['name', 'number', 'month', 'year', 'cvv', 'card_type']
        