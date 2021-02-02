from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
import datetime
from django.utils import timezone

class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')

   def __str__(self):
       return self.question_text

   def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING,)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

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


