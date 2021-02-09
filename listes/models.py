from django.db import models
from django.db.models.functions import Concat
from django.forms import ModelChoiceField
from django_mysql.models import ListCharField
from django.utils import timezone
import datetime
from django.contrib.auth.models import User




class Admnistrateur(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    poste = models.CharField(max_length=100)

    def __str__(self):
        return self.poste


class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
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

    titre = models.CharField(max_length=100, choices=titre_choix, default=AUCUN)

    def __str__(self):
        return self.titre


class Ufr(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Departement(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Filiere(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Niveau(models.TextChoices):
    L1 = 'L1'
    L2 = 'L2'
    L3 = 'L3'
    M1 = 'M1'
    M2 = 'M2'


class Etudiant(models.Model):
    numEtudiant = models.CharField(max_length=8)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    niveaux = ListCharField(
        base_field=models.CharField(
            max_length=10,
            choices=Niveau.choices,
            default=Niveau.L1,
        ),
        size=2,
        max_length=(2 * 11),
        default=None
    )


class Type(models.TextChoices):
    CM = 'CM'
    TD = 'TD'


class Cours(models.Model):
    nom = models.CharField(max_length=100)
    niveaux = ListCharField(
        base_field=models.CharField(
            max_length=10,
            choices=Niveau.choices,
            default=Niveau.L1,
        ),
        size=2,
        max_length=(2 * 11)
    )
    types = models.CharField(
        max_length=100,
        choices=Type.choices,
        default=Type.CM,
    )
    debut = models.IntegerField(datetime.date.today().year)
    fin = models.IntegerField(datetime.date.today().year + 1)

class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, User):
         return User.get_full_name()

