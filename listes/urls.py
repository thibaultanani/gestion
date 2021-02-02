from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .forms import  ConnexionForm

urlpatterns = [

    url(r'^index/', views.index, name='index'),
    url(r'^', views.connexion, name='connexion')
]