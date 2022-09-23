class PlayerViews:
    def create_player_form():
        name = input("Nom : ")
        first_name = input("Prénom : ")
        date_of_birth = input("Date de naissance : ")
        sex = input("Genre ? : ")
        ranking = input("Classement du joueur : ")
        print()

        return {
            "name": name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "sex": sex,
            "ranking": ranking
        }

    def display_player_from_db(players):
        print()
        player_number = 1
        for player in players:
            print(f"{player_number} : {player}")
            player_number += 1
        print()

        return input("Saisissez votre choix (0 pour revenir en arrière) : ")

    def display_infos_player(player):
        print()
        print(f"Nom : {player.name}")
        print(f"Prénom : {player.first_name}")
        print(f"Date de naissance : {player.date_of_birth}")
        print(f"Genre : {player.sex}")
        print(f"Classement : {player.ranking}")
        print()
        print("1. Retour à la liste des joueurs")
        print(f"2. Modifier le classement de {player}")
        print("3. Revenir en arrière")
        print()
        return input("Saisissez votre choix : ")

    def display_update_rank():
        print()
        return input("Veuillez saisir le nouveau classement du joueur : ")
