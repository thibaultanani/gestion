from django.db import models
from django_mysql.models import ListCharField


# Create your models here.
import datetime
from django.utils import timezone

class Utilisateur(models.Model):
   mdp = models.CharField(max_length=100)
   nom = models.CharField(max_length=100)
   prenom = models.CharField(max_length=100)
   email = models.EmailField(max_length=100)

   class Meta:
       abstract = True

class Admnistrateur(Utilisateur):
   poste = models.CharField(max_length=100)


   def __str__(self):
       return self.poste


class Titre(models.TextChoices):
    doctorant= 'Doctorant',
    maitre_de_conferences = 'Maître de conférences',
    prof_des_universites = 'Professeur des universités',
    tuteur = 'Tuteur'
class Professeur(Utilisateur):
   titre = models.CharField(max_length=100,choices=Titre.choices)
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
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
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


