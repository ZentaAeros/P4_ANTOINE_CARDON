# Développez un programme logiciel en Python
Bienvenue dans cette application de gestion de tournois d'échec.

## Comment executer ce script ?
* Veuillez créer un dossier à l'emplacement souhaité où sera placé le projet.
* Vous pouvez désormais clôner ce dépot dans le dossier fraîchement créé via `git clone https://github.com/ZentaAeros/P4_CARDON_ANTOINE.git`
* Vous pouvez à présent créer un environnement virtuel via : `python3 -m venv env`
* Activez l'environnement virtuel via `source env/bin/activate`
* Installez les paquets nécessaire à l'éxecution du script à l'aide du fichier *requirements.txt* via `python -m pip install -r requirements.txt`
* Vous êtes prêt à executer l'application via la commande `python3 main.py`

## Guide d'utilisation de l'application :
* Créer un tournoi
  * Vous pouvez entrer le nom du tournoi, le lieu et une description
  * Ajoutez les joueurs au tournoi
  * L'application génère les paires de joueurs
  * Entrez les résultats
  * Vous pouvez sauvegarder et quitter le tournoi et le reprendre plus tard
  * A la fin du tournoi, l'application affiche le classement final
  
* Ajouter un joueur
  * Entrez le nom, prénom, date de naissance, genre et classement du nouveau joueur pour l'enregistrer
 
* Voir tous les joueurs 
  * Affiche la liste de tous les joueurs : Par ordre alphabétique / Par classement
  * Sélectionnez l'un des numéros correspondant au joueur souhaité afin d'obtenir les informations détaillés du joueur
  * Vous pouvez modifier le classement du joueur sélectionné

* Afficher un rapport
  * Vous pouvez afficher les tournois en cours ou terminés
  * Vous pouvez Sélectionnez le numéro correspondant au tournoi souhaité
  * Vous pouvez alors afficher les joueurs du tournoi en question (par classement / par ordre alphabétique)
  * Vous pouvez afficher tous les tours du tournoi

* Charger un tournoi
  * Permet de reprendre un tournoi déjà créé et qui n'est pas terminé
  
## Comment générer un rapport FLAKE 8 :
* Depuis la racine du projet
 * Exécuter cette commande : flake8 --format=html --htmldir=flake-report
 * Un dossier nommé "flake-report" sera créé avec le rapport à l'intérieur
  
## ENJOY !
