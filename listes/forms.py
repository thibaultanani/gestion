from django.apps import apps
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext as _
from .models import *
from django.contrib.auth.models import User


class ConnexionForm(ModelForm):
    class Meta:
        model = User
        fields = ('email','password')
