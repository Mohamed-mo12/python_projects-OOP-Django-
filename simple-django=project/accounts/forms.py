from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput,required=True,max_length=200)
    firstname = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','firstname']


