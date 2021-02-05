#!/usr/bin/env bash



# Installation des dépendances python

pip3 install -r requirements.txt



# Installation des dépendances javascript
cd ..
mkdir media
cd static
npm install
cd node_modules
git clone --branch v1.3.0 https://github.com/ajaxorg/ace-builds
git clone https://github.com/ColorlibHQ/AdminLTE.git

