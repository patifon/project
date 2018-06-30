from django import forms
from .models import UserRegisterGroup



class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegisterGroup
        exclude=[""]
from django.forms import ModelForm



