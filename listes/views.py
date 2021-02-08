from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import *


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
                    if Admnistrateur.objects.filter(user_id=user_object.pk).exists():
                        return render(request, 'listes/accueil_admin.html', {'user_object': user_object})
                    if Professeur.objects.filter(user_id=user_object.pk).exists():
                        return render(request, 'listes/accueil_professeur.html', {'user_object': user_object})
            except:
                render(request, 'listes/login.html', {'form': form})
    else:
        form = ConnexionForm()
    return render(request, 'listes/login.html', {'form': form})


def deconnexion(request):
    logout(request)
    return render(request,'listes/login.html')


@login_required(login_url="/connexion")
def accueil_admin(request, user_object):
    user = get_object_or_404(User, id=user_object.id)
    print(user.first_name)
    return render(request, 'listes/accueil_admin.html', {'user', user})


@login_required(login_url="/connexion")
def accueil_professeur(request, user_object):
    user = get_object_or_404(User, id=user_object.id)
    print(user.first_name)
    return render(request, 'listes/accueil_professeur.html', {'user', user})


def prof_liste_etudiant(request):
    return render(request, 'listes/prof_liste_etudiant.html')


def prof_cursus_etudiant(request):
    return render(request, 'listes/prof_cursus_etudiant.html')


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


def modif_mdp(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = ModifierMdp(request.POST)
        if form.is_valid():
            old_mdp = request.POST.get('password', False)
            new_mdp = request.POST.get('new_password1', False)
            new_mdp2 = request.POST.get('new_password2', False)
            if new_mdp == new_mdp2:
                try:
                    user_mdp = User.objects.get(id=user_id)
                    if check_password(old_mdp, user_mdp.password):
                        user_mdp.set_password(new_mdp)
                        user_mdp.save()
                        return render(request, 'listes/accueil_professeur.html', {'user': user})
                    else:
                        print("echec-1")
                        messages.error(request, 'L\'ancien mot de passe ne correspond pas')
                        return render(request, 'listes/modif_mdp.html', {'user': user, 'form': form})
                except:
                    render(request, 'listes/login.html', {'form': form})
                    return render(request, 'listes/modif_mdp.html', {'user': user, 'form': form})
            else:
                print("echec0")
                messages.error(request, 'Les deux mot de passe saisies sont différents, veuillez réesayer')
                return render(request, 'listes/modif_mdp.html', {'user': user, 'form': form})
        else:
            print("echec1")
            messages.error(request, 'Erreur lors de la modification du mot de passe, réesayer plus tard')
        return render(request, 'listes/modif_mdp.html', {'user': user, 'form': form})
    else:
        print("echec2")
        form = ModifierMdp()
    return render(request, 'listes/modif_mdp.html', {'user': user, 'form': form})


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
            password=make_password('test1234')

            utilisateur = User(first_name=prenom, last_name=nom, email=email,
                               username=email, password=password)
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


def admin_creer_etudiant(request):
    if request.method == "POST":
        form = AjouterEtudiant(request.POST)
        if form.is_valid():
            numEtu = request.POST.get('numEtudiant', False)
            nom = request.POST.get('nom', False)
            prenom = request.POST.get('prenom', False)
            email = request.POST.get('email', False)
            niveaux = [request.POST.get('niveaux', False), request.POST.get('niveaux2', False)]

            etudiant = Etudiant(numEtudiant=numEtu, nom=nom, prenom=prenom, email=email, niveaux=niveaux)
            etudiant.save()

            print('#####')
            print(etudiant)
            print('#####')
            messages.success(request, 'Un nouvelle étudiant a été créé')
            return render(request, 'listes/admin_etudiant.html')
        else:
            print("echec")
            messages.error(request, 'Erreur lors de l\'ajout, réesayer plus tard')
        return render(request, 'listes/admin_creer_etudiant.html', {'form': form})
    else:
        print("echec2")
        form = AjouterEtudiant()
    return render(request, 'listes/admin_creer_etudiant.html', {'form': form})


def admin_etudiant(request):
    return render(request, 'listes/admin_etudiant.html')


def admin_modifier_etudiant(request):
    return render(request, 'listes/admin_modifier_etudiant.html')


def admin_cursus_etudiant(request):
    return render(request, 'listes/admin_cursus_etudiant.html')


def admin_switch_cours_etudiant(request):
    return render(request, 'listes/admin_switch_cours_etudiant.html')