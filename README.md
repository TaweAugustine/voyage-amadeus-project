<<<<<<< HEAD
=======

>>>>>>> 4401d02415f8dd6fc69fc38f35943c84b561f3f7
# API permettant de fourninir des voyages inspirants aux utilisateurs.

1- git clone :    
 git@github.com:TaweAugustine/voyage-amadeus-project.git

 2- création d'envrironnement virtuel avec:
   "python -m venv env"  et puis faire "source env/bin/activate"

3- " pip install -r requirements.txt" permet d'installer les dépendances 

4- " python manage.py runserver " pour compiller le projet

5- Pour tester l'API il faut utiliser "POSTMAN'

Dans Postman on peut saisir ces différent endpoints pour tester le fonctionnement de l'API.

6- l'endpoint "http://127.0.0.1:8000/api/travel-inspiration/" permet d'avoir une liste de destination

Exemple: http://127.0.0.1:8000/api/travel-inspiration/?originLocationCode=PAR&destinationLocationCode=FR 


7- l'endpoint "http://127.0.0.1:8000/api/travel-inspiration/<str:pk>" permet de donner les détails spécifiques consernant une donnée ayant une clé spécifique. Donc il faut chaque fois préciser une clée qui est un string.

Exemple: http://127.0.0.1:8000/api/travel-inspiration/<"AMAN">

8- l'endpoint "http://127.0.0.1:8000/api/travel-inspiration/search/<str:keyword>/  permet de lister une liste de donnée comportant un caractère ou un groupe de caractère donné

exemple : http://127.0.0.1:8000/api/travel-inspiration/search/TE/


