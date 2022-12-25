from django.forms import ModelForm
from django import forms 
from .models import Gift
from django.contrib.auth.models import User

class RegistrationForm(ModelForm):
    username = forms.TextInput()
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    class Meta:
        model = User
        fields = ['username', 'password']

class Create_gift(ModelForm):
    class Meta:
        model = Gift
        fields = ['gift_name', 'person_name']