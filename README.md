
# Projet 10 du parcours python d'OC : SoftDesk 

Ce programme est une API REST framework sous django réalisé dans le cadre d'un projet d'OC


## Installation

Se diriger sur le répertoire où l'on souhaite installer l'application.

Pour installer le programme via un terminal :  

Sous Windows :  
```sh
$ git clone https://github.com/Mildophin/P10  
$ python3 -m venv env  
$ env/scripts/activate  
$ pip3 install -r requirements.txt   
```
Sous linux/Mac :      
```sh
$ git clone https://github.com/Mildophin/P10
$ python3 -m venv env    
$ source env/bin/activate    
$ pip3 install -r requirements.txt    
```

## Lancement du serveur Django##

* Se rendre dans le répertoire contenant le fichier python ' manage.py ' ( dossier P10 )
* Puis exécuter:
```python manage.py runserver```
* La page sera accessible à l'URL suivante:  http://127.0.0.1:8000/projects/

## Fonctionnement

Se référer à la documentation POSTMAN pour effectuer les tests:
https://documenter.getpostman.com/view/14877827/UVkqqZyc


## Optionnel
Créer un rapport flake8 :  

`flake8 --exclude=env,venv --format=html --htmldir=flake8_report --max-line-lengt=119`

