from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email', False)
            password = request.POST.get('password', False)
            try:
                username = User.objects.get(email=email.lower()).username
                user_object = User.objects.get(email=email.lower())

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

def admin_liste_cours(request):
    return render(request, 'listes/admin_informations_cours.html')

def admin_creer_cours(request):
    return render(request, 'listes/admin_creer_cours.html')

def admin_modifier_cours(request):
    return render(request, 'listes/admin_modifier_cours.html')

def admin_gestion_professeur(request, user_id):
    user = get_object_or_404(User, id=user_id)
    print("HELLO")
    return render(request, 'listes/admin_gestion_professeur.html', {'user': user})

def admin_modifier_professeur(request):
    return render(request, 'listes/admin_modifier_professeur.html')

def admin_creer_professeur(request, user_id):
    user = get_object_or_404(User, id=user_id)
    print(user.first_name)
    if request.method == "POST":
        form = AjouterProfesseur(request.POST)
        if form.is_valid():
            prenom = request.POST.get('prenom', False)
            nom = request.POST.get('nom', False)
            email = request.POST.get('email', False)
            titre = request.POST.get('titre', False)

            utilisateur = User(first_name=prenom, last_name=nom, email=email,
                               username=email, password='test1234')
            utilisateur.is_active = True
            utilisateur.save()

            professeur = Professeur(user=utilisateur, titre=titre)
            # prof.active = 1
            professeur.save()

            print('#####')
            print(user)
            print(professeur)
            print('#####')
            messages.success(request, 'Un nouveau professeur a été créé')
        else:
            print("echec")
            messages.error(request, 'Erreur lors de l\'ajout, réesayer plus tard')
        return render(request, 'listes/admin_creer_professeur.html', {'user': user, 'form': form})
    else:
        print("echec2")
        form = AjouterProfesseur()
    return render(request, 'listes/admin_creer_professeur.html', {'user': user, 'form': form})

def admin_etudiant(request):
    return render(request, 'listes/admin_etudiant.html')

def admin_creer_etudiant(request):
    return render(request, 'listes/admin_creer_etudiant.html')

def admin_modifier_etudiant(request):
    return render(request, 'listes/admin_modifier_etudiant.html')

def admin_cursus_etudiant(request):
    return render(request, 'listes/admin_cursus_etudiant.html')

def admin_switch_cours_etudiant(request):
    return render(request, 'listes/admin_switch_cours_etudiant.html')