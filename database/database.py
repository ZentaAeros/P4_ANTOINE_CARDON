from tinydb import TinyDB, Query, where
from database.serialize import Serialize

DB = TinyDB("database/database.json")
PLAYERS = DB.table('players')
TOURNAMENT = DB.table('tournament')

class Database:
    # Serialize Player
    def save_player(player):
        PLAYERS.insert(Serialize.player(player))

    def update_ranking_player(id_player, ranking):
        request = Query()
        PLAYERS.update({'ranking': ranking}, request.id == id_player)

    def save_tournament(tournament, players, rounds, state):
        TOURNAMENT.insert(Serialize.tournament(tournament, players, rounds, state))

    def remove_tournament(id_tournament):
        TOURNAMENT.remove(where('id_tournament') == id_tournament)