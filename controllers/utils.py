from models.round import Match
from views.tournament import TournamentViews
from controllers.player import PlayerController


def search_in_list(tosearch, liste):
    return tosearch in liste


def create_pairs_first_round(list_of_players):
    pair_of_players = []
    # Trie les joueurs selon leur classement
    list_of_players = sort_players_by_ranking(list_of_players)
    # Division du groupe : Moitié supérieure
    moitie_superieure = list_of_players[0:4]
    # Division du groupe : Moitié inférieure
    moitie_inferieure = list_of_players[4:8]

    # Jumelage des joueurs
    for moitie_sup, moitie_inf in zip(moitie_superieure, moitie_inferieure):
        # Ajout de l'ID dans la liste des parties jouées des joueurs
        moitie_inf.played_with.append(moitie_sup.id)
        moitie_sup.played_with.append(moitie_inf.id)

        pair = Match(moitie_sup, moitie_inf)
        pair_of_players.append(pair)

    return pair_of_players


def create_pairs_next_rounds(list_of_players):
    # Trie les joueurs selon leur classement
    pair_of_players = []
    players_not_assigned = 0
    list_of_players = sort_players_by_number_of_points(list_of_players)
    next_player = 1
    players_assigned = []
    # Tant que tous les joueurs ne sont pas assignés
    while players_not_assigned < len(list_of_players):
        # Si le joueur n'est pas dans la liste des joueurs assignés
        if not search_in_list(list_of_players[players_not_assigned].id, players_assigned):
            while next_player < 8:
                if search_in_list(list_of_players[next_player].id, players_assigned):
                    next_player += 1
                elif search_in_list(
                        list_of_players[players_not_assigned].id, list_of_players[next_player].played_with):
                    next_player += 1
                else:
                    # Les joueurs assignés
                    players_assigned.append(list_of_players[next_player].id)
                    players_assigned.append(list_of_players[players_not_assigned].id)
                    pair = Match(list_of_players[next_player], list_of_players[players_not_assigned])

                    # Ajout de l'ID dans la liste des parties jouées
                    list_of_players[next_player].played_with.append(list_of_players[players_not_assigned].id)
                    list_of_players[players_not_assigned].played_with.append(list_of_players[next_player].id)

                    # Ajout de la pair de joueur dans le tableau
                    pair_of_players.append(pair)
                    next_player = 0
                    break
        players_not_assigned += 1

    return pair_of_players


def sort_players_by_ranking(players_sorting):
    return sorted(players_sorting, key=lambda player: player.ranking)


def sort_players_by_number_of_points(players_sorting):
    return sorted(players_sorting, key=lambda player: (player.number_of_points, player.ranking), reverse=True)


def sort_players_by_name(players_sorting):
    return sorted(players_sorting, key=lambda player: player.first_name)


def results_of_matchs(pair_of_players):
    list_of_players = []
    list_of_matchs = []
    pair_number = 0
    while pair_number < len(pair_of_players):
        user_entry = TournamentViews.display_get_results_from_user(
            pair_of_players[pair_number].player1, pair_of_players[pair_number].player2
        )
        match user_entry:
            case "1":
                update_points = PlayerController.add_points_to_player(
                    pair_of_players[pair_number].player1, pair_of_players[pair_number].player2
                )
                list_of_players.extend([update_points['winner'], update_points['loser']])
                list_of_matchs.append(update_points['match'])
                pair_number += 1
            case "2":
                update_points = PlayerController.add_points_to_player(
                    pair_of_players[pair_number].player2, pair_of_players[pair_number].player1
                )
                list_of_players.extend([update_points['winner'], update_points['loser']])
                list_of_matchs.append(update_points['match'])
                pair_number += 1
            case "3":
                update_points = PlayerController.add_points_to_player(
                    pair_of_players[pair_number].player1, pair_of_players[pair_number].player2, "y"
                )
                list_of_players.extend([update_points['winner'], update_points['loser']])
                list_of_matchs.append(update_points['match'])
                pair_number += 1
            case _:
                continue

    return list_of_players, list_of_matchs
