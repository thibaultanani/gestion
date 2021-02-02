from django.apps import apps
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext as _
from .models import *
from django.contrib.auth.models import User


class ConnexionForm(ModelForm):
    email = forms.CharField(label="email", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email',
                                                             'placeholder': 'Email'}))
    password = forms.CharField(label="password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password',
                                                                 'placeholder': 'Mot de passe'}))

    class Meta:
        model = User
        fields = ('email', 'password')
