from django.db import models
from django.db.models.functions import Concat
from django.forms import ModelChoiceField
from django_mysql.models import ListCharField
from django.utils import timezone

# Create your models here.
import datetime
from django.contrib.auth.models import User


class Admnistrateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    poste = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.poste


class Niveau(models.TextChoices):
    L1 = 'L1'
    L2 = 'L2'
    L3 = 'L3'
    M1 = 'M1'
    M2 = 'M2'


class Type(models.TextChoices):
    CM = 'CM'
    TD = 'TD'


class Ufr(models.Model):
    nom = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.nom


class Departement(models.Model):
    nom = models.CharField(max_length=100, default=None)
    ufr = models.ForeignKey(Ufr, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nom


class Filiere(models.Model):
    nom = models.CharField(max_length=100, default=None)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nom


class Cours(models.Model):
    nom = models.CharField(max_length=100, default=None)
    filieres = models.ManyToManyField(Filiere, default=None)
    niveaux = models.CharField(
            max_length=100,
            choices=Niveau.choices,
            default=Niveau.L1,
        )

    types = models.CharField(
        max_length=100,
        choices=Type.choices,
        default=Type.CM,
    )
    debut = models.DateField(default=None)
    fin = models.DateField(default=None)
    def __str__(self):
        return self.nom


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
    cours = models.ManyToManyField(Cours)

    #def __str__(self):
     #return self.titre
    def __str__(self):
      return self.user.get_full_name()


class Etudiant(models.Model):
    numEtudiant = models.CharField(max_length=8, default=None)
    nom = models.CharField(max_length=100, default=None)
    prenom = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=100,default=None)
    filieres = models.ManyToManyField(Filiere, default=None)
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
    cours = models.ManyToManyField(Cours)


class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, User):
        return User.get_full_name()


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class Cursus(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, default=None)
    debut = models.DateField(default=None)
    fin = models.DateField(default=None)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, default=None)
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
    etablissement = models.CharField(max_length=100, default=None)