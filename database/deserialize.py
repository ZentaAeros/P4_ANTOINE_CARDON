from tinydb import TinyDB, where
from models.player import Player
from models.tournament import Tournament

DB = TinyDB("database/database.json")
PLAYERS = DB.table('players')
TOURNAMENT = DB.table('tournament')

class Deserialize:
    # Deserialize Players
    def players():
        players = PLAYERS.all()
        list_of_players_from_db = []

        for player in players:
            deserialized_player = Player(
                player["id"],
                player["name"],
                player["first_name"],
                player["date_of_birth"],
                player["sex"],
                player["ranking"],
                player["number_of_points"],
                player["played_with"],
            )

            list_of_players_from_db.append(deserialized_player)
        return list_of_players_from_db

    # Deserialize Tournaments
    def tournament(state=""):
        if state == "":
            tournaments = TOURNAMENT.all()
        else:
            tournaments = TOURNAMENT.search(where('state') == state)
        list_of_tournaments_from_db = []
        for tournament in tournaments:
            list_of_players = []
            datetime_start = tournament["datetime_start"]
            datetime_end = tournament["datetime_end"]
            id_tournament = tournament["id_tournament"]
            name = tournament["name"]
            place = tournament["place"],
            description = tournament["description"],
            number_of_rounds = tournament["number_of_rounds"]
            round_number = tournament["round_number"]
            for current_player in tournament["players"]:
                player = PLAYERS.search(where('id') == current_player[0]["player_id"])
                player = Player(
                    player[0]["id"],
                    player[0]["name"],
                    player[0]["first_name"],
                    player[0]["date_of_birth"],
                    player[0]["sex"],
                    player[0]["ranking"],
                    player[0]["number_of_points"],
                    player[0]["played_with"]
                )

                list_of_players.append(player)

            list_of_tournaments_from_db.append(
                Tournament(
                    id_tournament,
                    datetime_start,
                    name,
                    place,
                    description,
                    list_of_players,
                    datetime_end,
                    number_of_rounds,
                    round_number
                    )
                )

        return list_of_tournaments_from_db


    # Deserialize ROUND
    def round_of_tournament(id_tournament):
        tournament = TOURNAMENT.search(where('id_tournament') == id_tournament)
        current_round = 0
        player1 = 0
        player2 = 1
        id_player = 0
        score_player = 1
        number_of_rounds = tournament[0]['round_number']
        while current_round < number_of_rounds:
            print(f"TOUR N°{current_round+1}")
            print()
            print(f"Démarré le : {tournament[0]['list_of_rounds'][current_round]['datetime_start']}")
            print()
            for match in tournament[0]['list_of_rounds'][current_round]['matchs']:
                id_of_player1 = match[player1][id_player]
                id_of_player2 = match[player2][id_player]
                score_of_player1 = match[player1][score_player]
                score_of_player2 = match[player2][score_player]
                myplayer1 = PLAYERS.search(where('id') == id_of_player1)
                myplayer2 = PLAYERS.search(where('id') == id_of_player2)
                name_of_player1 = myplayer1[0]['first_name'] + " " + myplayer1[0]['name']
                name_of_player2 = myplayer2[0]['first_name'] + " " + myplayer2[0]['name']
                print(f"{name_of_player1} VS {name_of_player2} ({score_of_player1} - {score_of_player2})")
            print()
            print(f"Terminé le : {tournament[0]['list_of_rounds'][current_round]['datetime_end']}")
            input()
            current_round += 1


    def tournament_loading(id_tournament):
        list_of_players = []
        infos_tournament = TOURNAMENT.search(where('id_tournament') == id_tournament)
        list_of_rounds = infos_tournament[0]['list_of_rounds']
        round_number = infos_tournament[0]['round_number']
        number_of_rounds = infos_tournament[0]['number_of_rounds']

        for current_player in infos_tournament[0]['players']:
            infos_player = PLAYERS.search(where('id') == current_player[0]['player_id'])
            player = Player(
                infos_player[0]['id'],
                infos_player[0]['name'],
                infos_player[0]['first_name'],
                infos_player[0]['date_of_birth'],
                infos_player[0]['sex'],
                infos_player[0]['ranking'],
                infos_player[0]['number_of_points'],
                infos_player[0]['played_with'],
                )

            player.played_with = current_player[0]['played_with']
            list_of_players.append(player)
        tournament = Tournament(
            infos_tournament[0]['id_tournament'],
            infos_tournament[0]['datetime_start'],
            infos_tournament[0]['name'],
            infos_tournament[0]['place'],
            infos_tournament[0]['description'],
            list_of_players,
            infos_tournament[0]['number_of_rounds'],
            infos_tournament[0]['round_number'],
        )

        return {
            'tournament': tournament,
            'list_of_players': list_of_players,
            'list_of_rounds': list_of_rounds,
            'round_number': round_number,
            'number_of_rounds': number_of_rounds
        }


    def tournament_in_progress():
        tournament = TOURNAMENT.search(where('state') == "doing")
        print(tournament[1]['name'])

    # Deserialize ID player
    def id_player():
        id_player = TinyDB("database/id_player.json")
        id = id_player.all()
        for id_of_player in id:
            return id_of_player["id"]

    # Deserialize ID tournament
    def id_tournament():
        id_tournament = TinyDB("database/id_tournament.json")
        id = id_tournament.all()
        for id_of_tournament in id:
            return id_of_tournament["id"]