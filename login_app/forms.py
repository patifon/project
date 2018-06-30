from django import forms
from .models import AuthUsers


class AuthUserForm(forms.ModelForm):
    class Meta:
        model = AuthUsers
        exclude=[""]