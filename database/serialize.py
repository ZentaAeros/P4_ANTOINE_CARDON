from tinydb import TinyDB

class Serialize:
    def player(player):
        return {
            "id": player.id,
            "name": player.name,
            "first_name": player.first_name,
            "date_of_birth": player.date_of_birth,
            "sex": player.sex,
            "ranking": player.ranking,
            "number_of_points": player.number_of_points,
            "played_with": player.played_with,
        }

    """# Serialize Players
    def players(list_of_players):
        for player in list_of_players:
            serialize_player = {
                "id": player.id,
                "name": player.name,
                "first_name": player.first_name,
                "date_of_birth": player.date_of_birth,
                "sex": player.sex,
                "ranking": player.ranking,
                "number_of_points": player.number_of_points,
                "played_with": player.played_with,
            }

            PLAYERS.insert(serialize_player)"""

    def tournament(tournament, list_of_players, list_of_rounds, state="doing"):
        list_rounds = []
        players_on_tournament = []
        for player in list_of_players:
            current_player = [
                {
                    'player_id': player.id,
                    'played_with': player.played_with,
                    'number_of_points': player.number_of_points
                }
            ]
            players_on_tournament.append(current_player)

        for rounds in list_of_rounds:
            serialized = {
                'datetime_start': rounds['datetime_start'],
                'datetime_end': rounds['datetime_end'],
                'round': rounds['round'],
                'matchs': rounds['matchs']
            }

            list_rounds.append(serialized)

        serialize_tournament = {
            "id_tournament": tournament.id_tournament,
            "datetime_start": tournament.datetime_start,
            "name": tournament.name,
            "place": tournament.place,
            "description": tournament.description,
            "players": players_on_tournament,
            "number_of_rounds": tournament.number_of_rounds,
            "datetime_end": tournament.datetime_end,
            "round_number": tournament.round_number,
            "state": state,
            "list_of_rounds": list_rounds
            }
        return serialize_tournament
    
    # Serialize ID player
    def id_player(id_of_player):
        id_player = TinyDB("database/id_player.json")
        id_player.truncate()
        serialized_id_player = {"id": id_of_player}
        id_player.insert(serialized_id_player)

    
    # Serialize ID tournament
    def id_tournament(id_of_tournament):
        id_tournament = TinyDB("database/id_tournament.json")
        id_tournament.truncate()
        serialized_id_tournament = {"id": id_of_tournament}
        id_tournament.insert(serialized_id_tournament)