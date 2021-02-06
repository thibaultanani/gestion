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

import pandas as pd


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
    return render(request, 'listes/login.html')


@login_required(login_url="/connexion")
def accueil_admin(request, user_object):
    user = get_object_or_404(User, id=user_object.id)
    print(user.first_name)
    return render(request, 'listes/accueil_admin.html', {'user': user})


@login_required(login_url="/connexion")
def accueil_professeur(request, user_id):
    user = get_object_or_404(User, id=user_id)
    print(user.first_name)
    return render(request, 'listes/accueil_professeur.html', {'user': user})


def prof_liste_etudiant(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'listes/prof_liste_etudiant.html', {'user': user})


def prof_cursus_etudiant(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'listes/prof_cursus_etudiant.html', {'user': user})


def admin_cours(request):
    return render(request, 'listes/admin_cours.html')


def admin_liste_cours(request):
    return render(request, 'listes/admin_informations_cours.html')


def admin_creer_cours(request):
    return render(request, 'listes/admin_creer_cours.html')


def admin_modifier_cours(request):
    return render(request, 'listes/admin_modifier_cours.html')


def admin_professeur(request, user_id):
    user = get_object_or_404(User, id=user_id)
    professeur_all = Professeur.objects.all().values()
    listProfesseur = []
    for i in range(len(professeur_all)):
        user_obj = User.objects.get(id=professeur_all[i]["user_id"])
        professeur_all[i]['username'] = user_obj.username
        professeur_all[i]['first_name'] = user_obj.first_name
        professeur_all[i]['last_name'] = user_obj.last_name
        professeur_all[i]['email'] = user_obj.email
        listProfesseur.append(professeur_all[i])

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            if str(newdoc.docfile.path).endswith('csv'):
                read_csv_file(newdoc.docfile)
            else:
                read_xlsx_file(newdoc.docfile)
            # Redirect to the document list after POST
            print("good")
            return redirect('listes/admin_professeur.html')
    else:
        print("echec3")
        form = DocumentForm()
    return render(request, 'listes/admin_professeur.html', {'user': user, 'form': form, "data": list(professeur_all)})


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


def read_csv_file(file):
    mon_fichier = pd.read_csv(file.path, encoding="windows-1252", sep=";")
    check_list = ['Doctorant', 'Maître de conférences', 'Professeur des universités', 'Tuteur', 'Aucun']
    print(mon_fichier)
    print("JE SUIS UN CSV")
    # TODO : ajouter un mot de passe pour les utilisateurs crées
    for index, row in mon_fichier.iterrows():
        if row["Titre"] in check_list:
            utilisateur, cree1 = User.objects.get_or_create(
                email=row["Email"],
                defaults={'first_name': row["Prenom"],
                          'last_name': row["Nom"],
                          'username': row["Email"],
                          }
            )
            print(cree1)
            professeur, cree2 = Professeur.objects.get_or_create(
                user=utilisateur,
                defaults={'titre': row["Titre"]}
            )
            print(cree2)


def read_xlsx_file(file):
    mon_fichier = pd.read_excel(file.path, engine='openpyxl')
    check_list = ['Doctorant', 'Maître de conférences', 'Professeur des universités', 'Tuteur', 'Aucun']
    print(mon_fichier)
    print("JE SUIS UN XLSX")
    # TODO : ajouter un mot de passe pour les utilisateurs crées
    for index, row in mon_fichier.iterrows():
        if row["Titre"] in check_list:
            utilisateur, cree1 = User.objects.get_or_create(
                email=row["Email"],
                defaults={'first_name': row["Prenom"],
                          'last_name': row["Nom"],
                          'username': row["Email"],
                          }
            )
            print(cree1)
            professeur, cree2 = Professeur.objects.get_or_create(
                user=utilisateur,
                defaults={'titre': row["Titre"]}
            )
            print(cree2)

