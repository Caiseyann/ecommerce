from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib .auth.models import User
from django import forms
from django.forms.utils import ValidationError
from .models import *

# New profile form
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
