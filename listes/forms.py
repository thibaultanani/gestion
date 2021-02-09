from django.apps import apps
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext as _
from .models import *
from django.contrib.auth.models import User
from .models import *


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


class AjouterProfesseur(ModelForm):
    nom = forms.CharField(label="nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(label="prenom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="email", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email',
                                                             'placeholder': 'Email'}))

    DOCTORANT = 'Doctorant'
    MAITRES_DE_CONFERENCES = 'Maître de conférences'
    PROF_DES_UNIVERSITES = 'Professeur des universités'
    TUTEUR = 'Tuteur'
    AUCUN = 'Aucun'

    titre_choix = (
        (DOCTORANT, 'Doctorant'),
        (MAITRES_DE_CONFERENCES, 'Maître de conférences'),
        (PROF_DES_UNIVERSITES, 'Professeur des universités'),
        (TUTEUR, 'Tuteur'),
        (AUCUN, 'Aucun'),
    )

    titre = forms.ChoiceField(choices=titre_choix)

    class Meta:
        model = Professeur
        fields = ('nom', 'prenom', 'email', 'titre')


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Choisir un fichier',
        help_text='max. 42 megabytes'
    )


class ModifierProfesseur(ModelForm):
    nom = forms.CharField(label="nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(label="prenom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="email", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email',
                                                             'placeholder': 'Email'}))

    DOCTORANT = 'Doctorant'
    MAITRES_DE_CONFERENCES = 'Maître de conférences'
    PROF_DES_UNIVERSITES = 'Professeur des universités'
    TUTEUR = 'Tuteur'
    AUCUN = 'Aucun'

    titre_choix = (
        (DOCTORANT, 'Doctorant'),
        (MAITRES_DE_CONFERENCES, 'Maître de conférences'),
        (PROF_DES_UNIVERSITES, 'Professeur des universités'),
        (TUTEUR, 'Tuteur'),
        (AUCUN, 'Aucun'),
    )

    titre = forms.ChoiceField(choices=titre_choix)

    class Meta:
        model = Professeur
        fields = ('nom', 'prenom', 'email', 'titre')


class ModifierMdp(ModelForm):
    password = forms.CharField(label="ancien mot de passe", max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="nouveau mot de passe", max_length=100,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="nouveau mot de passe", max_length=100,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('password',)



class AjouterCours(forms.Form):

    TYPES = [('type1', 'CM'),
                 ('type2', 'TD')]
    niveaux=[ ('L1','L1'),
             ('L2','L2'),
             ('L3','L3'),
             ('M1','M1'),
             ('M2','M2'),
            ]

    #nb_f = [tuple([x, x]) for x in range(1, 4)]
    nb= [tuple([x, x]) for x in range(1, 4)]
    choix = (('1', 'Choix 1'),('2', 'Choix 2'))
    model = Cours
    nomCours = forms.CharField(label=_('Nom Cours'), max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type= forms.ChoiceField(choices=TYPES, widget=forms.RadioSelect(attrs={'class': "custom-radio-list"}))
    nb_filliere = forms.IntegerField(label="Fillière(s)", widget=forms.Select(choices=nb))
    nom_filliere1=forms.ModelChoiceField(queryset=Filiere.objects.all())
    nom_filliere2=forms.ModelChoiceField(label="",queryset=Filiere.objects.all())
    nom_filliere3=forms.ModelChoiceField(label="",queryset=Filiere.objects.all())
    nb_prof=forms.IntegerField(label="", widget=forms.Select(choices=nb))
    nom_prof1=UserModelChoiceField(label="Professeur(s)",queryset=User.objects.all())
    nom_prof2=UserModelChoiceField(label="",queryset=User.objects.all(), required=False)
    nom_prof3=UserModelChoiceField(label="",queryset=User.objects.all(), required=False)
    Niveau=forms.ChoiceField(label="Niveau",choices=niveaux)
    date_debut=forms.DateField(initial=datetime.date.today)
    date_fin=forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Cours
        fields = ('nom', 'niveaux', 'types')

# class CreerCoursForm(forms.Form):
#     nom = forms.CharField(label=_('Nom'), max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
#     objectif = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
#     code = forms.CharField(label=_('Code'), max_length=10, required=False,
#                            widget=forms.TextInput(attrs={'class': 'form-control'}))
#     Type = forms.ChoiceField(label=_('Type'), max_length=100, required=True, choices=Type)
#
#     def save(self, user):
#
