from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
    username  = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    
    
    
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()