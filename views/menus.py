class Menus:
    def main_menu():
        print()
        print("1. Créer un tournoi")
        print("2. Ajouter un joueur")
        print("3. Voir tous les joueurs")
        print("4. Afficher un rapport")
        print("5. Charger un tournoi")
        print("6. Quitter l'application")
        print()

        response = input("Saisissez votre choix : ")

        return response

    def between_rounds():
        print("*********************************")
        print("** 1. Démarrer le tour suivant **")
        print("** 2. Sauvegarder le tournoi   **")
        print("*********************************")
        print()

        return input("Saisissez votre choix : ")

    def sort_players_by_name_or_ranking():
        print()
        print()
        print("Afficher les joueurs :")
        print()
        print("1. Par ordre alphabétique")
        print("2. Par classement")
        print()
        return input("Saisissez votre choix (0 pour revenir en arrière) : ")
