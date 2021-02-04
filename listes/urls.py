from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .forms import  ConnexionForm

urlpatterns = [
    url(r'^accueil_admin/', views.accueil_admin, name='accueil_admin'),
    url(r'^admin_cours/', views.admin_cours, name='admin_cours'),
    url(r'^admin_etudiant/', views.admin_etudiant, name='admin_etudiant'),
    url(r'^admin_professeur/(?P<user_id>[0-9]+)/', views.admin_professeur, name='admin_professeur'),
    url(r'^gestion_professeur/(?P<user_id>[0-9]+)/', views.gestion_professeur, name='gestion_professeur'),
    url(r'^', views.connexion, name='connexion')
]
