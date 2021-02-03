from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email', False)
            password = request.POST.get('password', False)
            try:
                username = User.objects.get(email=email.lower()).username
                user_object = User.objects.get(email=email.lower())

                print(username)
                user = authenticate(username=username, password=password)

                if user is not None and user.is_active:
                    login(request, user)
                    return render(request, 'listes/accueil_admin.html', {'user_object': user_object})
            except:
                render(request, 'listes/login.html', {'form': form})
    else:
        form = ConnexionForm()
    return render(request, 'listes/login.html', {'form': form})


@login_required(login_url="/connexion")
def accueil_admin(request, user_object):
    user = get_object_or_404(User, id=user_object.id)
    print(user.first_name)
    return render(request, 'listes/accueil_admin.html', {'user', user})


def admin_cours(request):
    return render(request, 'listes/admin_cours.html')


def admin_professeur(request):
    return render(request, 'listes/admin_professeur.html')


def admin_etudiant(request):
    return render(request, 'listes/admin_etudiant.html')

