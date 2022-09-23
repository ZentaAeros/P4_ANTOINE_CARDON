class TournamentViews:
    def create_tournament_form():
        name = input("Entrez le nom du tournoi : ")
        place = input("Indiquez le lieu du tournoi : ")
        description = input("Ajoutez une description : ")

        return {"name": name, "place": place, "description": description}

    def state_of_tournaments_to_report():
        print()
        print("1. Afficher les tournois terminés")
        print("2. Afficher les tournois en cours")
        print()
        return input("Saisissez votre choix (0 pour revenir en arrière) : ")

    def display_players_from_tournament(list_of_players):
        print()
        print()
        player_number = 1
        for player in list_of_players:
            print(f"{player_number} : {player}")
            player_number += 1

    def display_infos_tournaments(tournaments):
        print()
        print(f"Nom : {tournaments.name}")
        print(f"Lieu : {tournaments.place}")
        print(f"Description : {tournaments.description}")
        print()
        print(f"Date de début : {tournaments.datetime_start}")
        print(f"Date de fin : {tournaments.datetime_end}")
        print()
        print("1. Afficher tous les joueurs du tournoi")
        print("2. Afficher tous les tours du tournoi")
        print("3. Retour à la liste des tournois")
        print()

        return input("Saisissez votre choix (0 pour revenir en arrière) : ")

    def display_list_of_tournaments(list_of_tournaments):
        tournament_number = 1
        for tournaments in list_of_tournaments:
            print(f"{tournament_number} : {tournaments}")
            tournament_number += 1
        print()
        return input("Saisissez votre choix (0 pour revenir en arrière) : ")

    def display_tournaments_from_db(tournaments):
        number_tournament = 1
        for tournament in tournaments:
            print(f"{number_tournament} : {tournament}")
            number_tournament += 1
        print()

        return input("Saisissez votre choix (0 pour revenir en arrière) : ")

    def display_tournament(tournament):
        print(f"Début du tounoi {tournament.name} à {tournament.datetime_start}")
        print(f"Lieu du tournoi : {tournament.place}")
        print(f"Description du tournoi : {tournament.description}")
        print()

    def add_or_load_player_menu():
        print("1. Ajouter un nouveau joueur")
        print("2. Charger un joueur")
        print()

        return input("Saisissez votre choix : ")

    def display_get_results_from_user(player1, player2):
        print()
        print("Qui est le vainqueur de la partie : ")
        print(f"1. {player1}")
        print(f"2. {player2}")
        print("3. Les joueurs sont à égalités")
        print()

        return input("Saisissez votre choix : ")

    def display_pairs(pair_of_players):
        for pair in pair_of_players:
            print(f"{pair.player1} vs {pair.player2}")

    def display_ranking_by_number_of_points(resultats):
        player_number = 1
        for resultat in resultats:
            print(f"{player_number} : {resultat} ({resultat.number_of_points} points)")
            player_number += 1
        print()
