from django.db import models


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

