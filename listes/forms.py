from django.apps import apps
from django import forms
from django.forms import ModelForm
from django.db.models import IntegerField, Model
from django_mysql.models import ListTextField
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


class AjouterEtudiant(ModelForm):
    numEtudiant = forms.CharField(label="Numero Etudiant", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nom = forms.CharField(label="nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(label="prenom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="email", max_length=150,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))

    niveau_choix = [
        ('L1', 'L1'),
        ('L2', 'L2'),
        ('L3', 'L3'),
        ('M1', 'M1'),
        ('M2', 'M2'),
    ]

    niveaux = forms.CharField(label="niveau", widget=forms.Select(choices=niveau_choix))
    ajac = forms.BooleanField(required=False)

    filliere = forms.ModelChoiceField(label="filliere",queryset=Filiere.objects.all())
    filliere2 = forms.ModelChoiceField(label="filliere double licence", queryset=Filiere.objects.all(), required=False)

    class Meta:
        model = Etudiant
        fields = ('numEtudiant', 'nom', 'prenom', 'email', 'niveaux', 'filliere')


class ModifierEtudiant(ModelForm):
    numEtudiant = forms.CharField(label="Numero Etudiant", max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    nom = forms.CharField(label="nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(label="prenom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="email", max_length=150,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))

    niveau_choix = [
        ('L1', 'L1'),
        ('L2', 'L2'),
        ('L3', 'L3'),
        ('M1', 'M1'),
        ('M2', 'M2'),
    ]

    niveau_choix2 = [
        ('Nan', ' '),
        ('L1', 'L1'),
        ('L2', 'L2'),
        ('L3', 'L3'),
        ('M1', 'M1'),
        ('M2', 'M2'),
    ]

    niveaux = forms.CharField(label="niveau", widget=forms.Select(choices=niveau_choix))
    ajac = forms.BooleanField(required=False)

    filliere = forms.ModelChoiceField(label="filliere", queryset=Filiere.objects.all())
    filliere2 = forms.ModelChoiceField(label="filliere double licence", queryset=Filiere.objects.all(), required=False)

    class Meta:
        model = Etudiant
        fields = ('nom', 'prenom', 'email', 'niveaux', 'filliere')


class AjouterProfesseur(ModelForm):
    nom = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(label="Prénom", max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="Email", max_length=150,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))

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

    TYPES = [('CM', 'CM'),
                 ('TD', 'TD')]
    niveau=[ ('L1','L1'),
             ('L2','L2'),
             ('L3','L3'),
             ('M1','M1'),
             ('M2','M2'),
            ]

    nb= [tuple([x, x]) for x in range(1, 4)]
    nomCours =forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type= forms.ChoiceField(choices=TYPES, widget=forms.RadioSelect(attrs={'class': "custom-radio-list"}))
    nb_filliere = forms.IntegerField(label="Filière(s)", widget=forms.Select(choices=nb))
    nom_filliere1=forms.ModelChoiceField(label='Filiere n°1',queryset=Filiere.objects.all())
    nom_filliere2=forms.ModelChoiceField(label="Filiere n°2",queryset=Filiere.objects.all(),required=False)
    nom_filliere3=forms.ModelChoiceField(label="Filiere n°3",queryset=Filiere.objects.all(),required=False)
    nb_prof=forms.IntegerField(label="Professeur(s)", widget=forms.Select(choices=nb))
    nom_prof1=forms.ModelChoiceField(label='Professeur n°1', queryset=Professeur.objects.all())
    nom_prof2=forms.ModelChoiceField(label='Professeur n°2', queryset=Professeur.objects.all(),required=False)
    nom_prof3=forms.ModelChoiceField(label='Professeur n°3', queryset=Professeur.objects.all(),required=False)
    Niveau=forms.ChoiceField(label="Niveau",choices=niveau)
    date_debut=forms.DateField(initial=datetime.date.today)
    date_fin=forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Cours
        fields = ('nom', 'niveaux', 'types','debut','fin')

class ModifierCours(forms.Form):

    TYPES = [('CM', 'CM'),
                 ('TD', 'TD')]
    niveau=[ ('L1','L1'),
             ('L2','L2'),
             ('L3','L3'),
             ('M1','M1'),
             ('M2','M2'),
            ]

    nb= [tuple([x, x]) for x in range(1, 4)]
    nomCours = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type= forms.ChoiceField(choices=TYPES, widget=forms.RadioSelect(attrs={'class': "custom-radio-list"}))
    #nb_filliere = forms.IntegerField(label="Fillière(s)", widget=forms.Select(choices=nb))
    nom_filliere1=forms.ModelChoiceField(label='Filiere n°1',queryset=Filiere.objects.all())
    nom_filliere2=forms.ModelChoiceField(label="Filiere n°2",queryset=Filiere.objects.all(),required=False)
    nom_filliere3=forms.ModelChoiceField(label="Filiere n°3",queryset=Filiere.objects.all(),required=False)
    #nb_prof=forms.IntegerField(label="", widget=forms.Select(choices=nb))

    nom_prof1=forms.ModelChoiceField(label='Professeur n°1', queryset=Professeur.objects.all())
    nom_prof2=forms.ModelChoiceField(label='Professeur n°2', queryset=Professeur.objects.all(),required=False)
    nom_prof3=forms.ModelChoiceField(label='Professeur n°3', queryset=Professeur.objects.all(),required=False)
    Niveau=forms.ChoiceField(label="Niveau",choices=niveau)
    date_debut=forms.DateField(initial=datetime.date.today)
    date_fin=forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Cours
        fields = ('nom', 'niveaux', 'types','debut','fin')


class SwitchForm(forms.Form):
    choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
    )

