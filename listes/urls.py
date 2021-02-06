from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .forms import ConnexionForm

urlpatterns = [
    url(r'^accueil_admin/', views.accueil_admin, name='accueil_admin'),
    url(r'^accueil_professeur/', views.accueil_professeur, name='accueil_professeur'),
    url(r'^prof_liste_etudiant/(?P<user_id>[0-9]+)/', views.prof_liste_etudiant, name='prof_liste_etudiant'),
    url(r'^prof_cursus_etudiant/(?P<user_id>[0-9]+)/', views.prof_cursus_etudiant, name='prof_cursus_etudiant'),
    url(r'^modif_mdp/(?P<user_id>[0-9]+)/', views.modif_mdp, name='modif_mdp'),
    url(r'^admin_cours/', views.admin_cours, name='admin_cours'),
    url(r'^admin_liste_cours/', views.admin_liste_cours, name='admin_liste_cours'),
    url(r'^admin_creer_cours/', views.admin_creer_cours, name='admin_creer_cours'),
    url(r'^admin_modifier_cours/', views.admin_modifier_cours, name='admin_modifier_cours'),
    url(r'^admin_etudiant/', views.admin_etudiant, name='admin_etudiant'),
    url(r'^admin_modifier_etudiant/', views.admin_modifier_etudiant, name='admin_modifier_etudiant'),
    url(r'^admin_creer_etudiant/', views.admin_creer_etudiant, name='admin_creer_etudiant'),
    url(r'^admin_cursus_etudiant/', views.admin_cursus_etudiant, name='admin_cursus_etudiant'),
    url(r'^admin_switch_cours_etudiant/', views.admin_switch_cours_etudiant, name='admin_switch_cours_etudiant'),
    url(r'^admin_professeur/(?P<user_id>[0-9]+)/', views.admin_professeur,
        name='admin_professeur'),
    url(r'^admin_modifier_professeur/', views.admin_modifier_professeur, name='admin_modifier_professeur'),
    url(r'^admin_creer_professeur/(?P<user_id>[0-9]+)/', views.admin_creer_professeur, name='admin_creer_professeur'),
    url(r'^', views.connexion, name='connexion'),
    url(r'^', views.deconnexion, name='deconnexion')
]
