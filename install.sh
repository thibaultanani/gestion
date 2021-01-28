#!/usr/bin/env bash



# Installation des dépendances python
pip3 install --upgrade pip
pip3 install -r requirements.txt


# Installation des dépendances javascript
mkdir static
cd static
npm install  gentelella@1.3.0 --save
npm install  jquery-sortable@0.9.13 --save
npm install  autosize@4.0.0 --save
npm install  magicsuggest@2.1.4 --save
npm install  json-editor@0.7.28 --save
npm install  datatables.net-plugins@1.10.15 --save
npm install  jquery.marquee@1.3.94 --save

git clone --branch v1.3.0 https://github.com/ajaxorg/ace-builds


