from views.player import PlayerViews
from models.player import Player
from database.deserialize import Deserialize
from database.serialize import Serialize


class PlayerController:
    def add_player():
        # Récupération des informations du nouveau joueur depuis la vue
        list_player = []
        player_form = PlayerViews.create_player_form()
        id_player = Deserialize.id_player()
        player = Player(
            str(id_player),
            player_form["name"],
            player_form["first_name"],
            player_form["date_of_birth"],
            player_form["sex"],
            int(player_form["ranking"]),
            0,
            [str(id_player)],
        )
        id_player += 1
        Serialize.id_player(id_player)
        list_player.append(player)
        player.save_player()

    def update_ranking_of_player(player):
        user_entry = PlayerViews.display_update_rank()
        user_entry = int(user_entry)
        player.update_ranking(user_entry)

    def add_points_to_player(winner, loser, equality="n"):
        if equality == "n":
            winner.number_of_points += 1
            match = [[winner.id, "1"], [loser.id, "0"]]
        else:
            winner.number_of_points += 1
            loser.number_of_points += 1
            match = [[winner.id, "1"], [loser.id, "1"]]
        return {'winner': winner, 'loser': loser, 'match': match}
