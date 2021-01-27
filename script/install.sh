#!/usr/bin/env bash

# Pour afficher les commandes dans la commande
# set -x

# Mettre la variable d'environnement PRODUCTION_SERVER à true si c'est pour le serveur de production

# Suppression des lignes pour prendre en compte les variables d'environment (.bashrc)
# même si on n'est pas en interractive/login shell
sed -i.bak -e '6,9d;' /home/vagrant/.bashrc

# Initialisation des paramètres pour le développement
if [ "$PRODUCTION_SERVER" != "true" ]; then
  # TODO: Trouver une solution pour éviter la redondance (problème .bashrc pas pris dans la portée du script)
  export DJANGO_SECRET_KEY='6cpp%r5s%u8g9+6ovqsn#6eqyqjcw4qtg-0th#gf%nnjof-)@c'
  export DJANGO_DEBUG=true

  export ADMIN_USER=admin
  export ADMIN_PWD=admin
  export ADMIN_EMAIL='admin@example.com'
  export DJANGO_DIR=/vagrant
  export DJANGO_MEDIA_ROOT=/home/vagrant/media

  export DATABASE_NAME=moulinette
  export DATABASE_USER=moulinetteuser
  export DATABASE_HOST='localhost'
  export DATABASE_PORT=''
  export DATABASE_PASSWORD=moulinette

  export BASE_URL=''
  export DOMAIN_NAME='http://localhost:8000/'

  export STATIC_JS=$DJANGO_DIR/static/moulinette

  # Pour selenium
  export FIREFOX_PATH=/opt/firefox/firefox
  export GECKODRIVER_PATH=/opt/geckodriver


  read -r -d '' ENV_VARS <<- EOM
  export PRODUCTION_SERVER=$PRODUCTION_SERVER
  export DJANGO_SECRET_KEY="$DJANGO_SECRET_KEY"
  export DJANGO_DEBUG=$DJANGO_DEBUG

  export ADMIN_USER=$ADMIN_USER
  export ADMIN_PWD=$ADMIN_PWD
  export ADMIN_EMAIL="$ADMIN_EMAIL"
  export DJANGO_DIR=$DJANGO_DIR
  export DJANGO_MEDIA_ROOT=$DJANGO_MEDIA_ROOT

  export DATABASE_NAME=$DATABASE_NAME
  export DATABASE_USER=$DATABASE_USER
  export DATABASE_HOST=$DATABASE_HOST
  export DATABASE_PORT="$DATABASE_PORT"
  export DATABASE_PASSWORD=$DATABASE_PASSWORD

  export BASE_URL=$BASE_URL
  export DOMAIN_NAME="$DOMAIN_NAME"

  export STATIC_JS=$STATIC_JS

  # Pour selenium
  export FIREFOX_PATH=$FIREFOX_PATH
  export GECKODRIVER_PATH=$GECKODRIVER_PATH

  alias run_server_dev=$DJANGO_DIR/scripts/run_server_dev.sh
  alias run_server_prod="$DJANGO_DIR/scripts/run_server_prod.sh"
  alias run_celery="celery --workdir=$DJANGO_DIR -A moulinette worker"
EOM
  echo "$ENV_VARS" >> /home/vagrant/.bashrc
  source /home/vagrant/.bashrc
fi

print_help () {
  echo "#################################################"
  echo "                     AIDE                        "
  echo "#################################################"
  echo "Se connecter à la machine virtuelle: 'vagrant ssh'"
  echo "Lancer le serveur avec la commande: 'python3.5 -u $DJANGO_DIR/manage.py runserver 0.0.0.0:8000'"
  echo "Quitter la machine virtuelle sans l'éteindre: 'exit'"
  echo "Eteindre la machine virtuelle: 'vagrant halt'"
  echo "Démarrer la machine virtuelle: 'vagrant up'"
  echo "Suprimer la machine virtuelle: 'vagrant destroy'"
  echo "Mettre à jour si des modifications ont été apportés au fichier d'installation (scripts/): 'vagrant provision'\n"

  echo "Informations admin pour la connexion"
  echo "Username = $ADMIN_USER"
  echo "Email = $ADMIN_EMAIL"
  echo "Password = $ADMIN_PWD"
}

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get -y upgrade

# Installation des dépendances python
pip3 install --upgrade pip
pip3 install -r $DJANGO_DIR/requirements.txt

# Création du dossier de log
mkdir $DJANGO_DIR/log

# Pour tester comme si on était en production (cf ./scripts/run_like_prod.sh)
apt-get -y install nginx
mkdir /var/www/cat
chown vagrant /var/www/cat

# Installation de l'outil de génération et de correction d'exercices
pip3 uninstall moulinette_tools
git clone http://MoulinetteBot2018:J1pgF42xwROO@savoircoder.fr/gogs/minions2019/moulinette-tools
mkdir moulinette-tools/moulinette_tools/bin
wget http://savoircoder.fr/gogs/attachments/60c5568c-c527-438d-be72-c692521b6cf0 -O moulinette-tools/moulinette_tools/bin/clang_ast_analysis
chmod +x moulinette-tools/moulinette_tools/bin/clang_ast_analysis
pip3 install moulinette-tools/
rm -R moulinette-tools

# Création des dossiers latex pour les sujets
mkdir $DJANGO_MEDIA_ROOT
mkdir $DJANGO_MEDIA_ROOT/exercices
mkdir $DJANGO_MEDIA_ROOT/exercices/tmp
mkdir $DJANGO_MEDIA_ROOT/sujets
mkdir $DJANGO_MEDIA_ROOT/sujets/tmp
mkdir $DJANGO_MEDIA_ROOT/td
mkdir $DJANGO_MEDIA_ROOT/cours
mkdir $DJANGO_MEDIA_ROOT/depoDJANGO_DIRts
mkdir $DJANGO_MEDIA_ROOT/competition
mkdir $DJANGO_MEDIA_ROOT/competition/depots
mkdir $DJANGO_MEDIA_ROOT/competition/outputs
mkdir $DJANGO_MEDIA_ROOT/code_source
mkdir $DJANGO_MEDIA_ROOT/correction
mkdir $DJANGO_MEDIA_ROOT/moocs
mkdir $DJANGO_MEDIA_ROOT/moocs/tmp

# Récupération du template LaTeX pour les sujets PDF
# TODO Add token for git serveur to read (not write) project
pip3 install git+http://MoulinetteBot2018:J1pgF42xwROO@savoircoder.fr/gogs/Moulinette2018/delbomatic --upgrade
git clone http://MoulinetteBot2018:J1pgF42xwROO@savoircoder.fr/gogs/Moulinette2018/template-delbomatic.git
mv template-delbomatic/main.tex $DJANGO_MEDIA_ROOT/sujets/main.tex
rm -R template-delbomatic

# Mise à jour des droit de DJANGO_MEDIA_ROOT
chown -R vagrant $DJANGO_MEDIA_ROOT
chgrp -R vagrant $DJANGO_MEDIA_ROOT

# Installation des dépendances javascript
npm install --prefix $STATIC_JS gentelella@1.3.0 --save
npm install --prefix $STATIC_JS jquery-sortable@0.9.13 --save
npm install --prefix $STATIC_JS autosize@4.0.0 --save
npm install --prefix $STATIC_JS magicsuggest@2.1.4 --save
npm install --prefix $STATIC_JS json-editor@0.7.28 --save
npm install --prefix $STATIC_JS datatables.net-plugins@1.10.15 --save
npm install --prefix $STATIC_JS jquery.marquee@1.3.94 --save

git clone --branch v1.3.0 https://github.com/ajaxorg/ace-builds
mv ace-builds/src-min $STATIC_JS/node_modules/ace
rm -r ace-builds

git clone --branch v2.1.13 https://github.com/fonini/ckeditor-youtube-plugin.git
mv ckeditor-youtube-plugin/youtube $STATIC_JS/node_modules/ckeditor-youtube/youtube
mv ckeditor-youtube-plugin/package.json $STATIC_JS/node_modules/ckeditor-youtube/
rm -r ckeditor-youtube-plugin

# Installation selenium
apt install -y xvfb
wget -O /opt/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
tar xf /opt/geckodriver.tar.gz --directory /opt

wget -O /opt/FirefoxSetup.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=fr"
tar xf /opt/FirefoxSetup.tar.bz2 --directory /opt

rm /opt/geckodriver.tar.gz
rm /opt/FirefoxSetup.tar.bz2

# Changement de la configuration de postgresql pour permettre d'y accéder depuis
# l'hote avec pgadmin par exemple
echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.6/main/pg_hba.conf
sudo -u postgres psql -c "ALTER SYSTEM SET listen_addresses = '*';"
sudo -u postgres psql -c "SELECT pg_reload_conf();"

service postgresql restart

# Création de l'utilisateur pour la BDD
sudo su - postgres -c psql <<EOF
CREATE DATABASE $DATABASE_NAME;
CREATE USER $DATABASE_USER WITH PASSWORD '$DATABASE_PASSWORD';

ALTER ROLE $DATABASE_USER SET client_encoding TO 'utf8';
ALTER ROLE $DATABASE_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $DATABASE_USER SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE $DATABASE_NAME TO $DATABASE_USER;
ALTER USER $DATABASE_USER CREATEDB;
EOF

# Migration de la base de données avec django
python3.5 $DJANGO_DIR/manage.py makemigrations
python3.5 $DJANGO_DIR/manage.py migrate

# Ajout des différents tests disponibles dans la BDD
python3.5 $DJANGO_DIR/manage.py shell < $DJANGO_DIR/exercice/script_bd.py

# Ajout des groupes
python3.5 $DJANGO_DIR/manage.py shell < $DJANGO_DIR/utilisateur/create_groups.py

# Création de l'admin
echo "from django.contrib.auth.models import User; \
      User.objects.filter(email='$ADMIN_EMAIL').delete(); \
      User.objects.create_superuser('$ADMIN_USER', '$ADMIN_EMAIL', '$ADMIN_PWD')" \
      |/usr/bin/python3.5 /vagrant/manage.py shell

print_help
