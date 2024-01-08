from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
    
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Email or password is incorrect')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect')
            if not user.is_active:
                raise forms.ValidationError('User is inactive')
                
        return super(UserLoginForm, self).clean()