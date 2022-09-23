from controllers.utils import (
    sort_players_by_name, sort_players_by_number_of_points, sort_players_by_ranking
)
from database.deserialize import Deserialize
from views.menus import Menus
from views.player import PlayerViews
from views.tournament import TournamentViews
from controllers.player import PlayerController


def report_all_players_from_db():
    user_entry = True
    players_from_db = Deserialize.players()
    while user_entry:
        user_entry = Menus.sort_players_by_name_or_ranking()

        match user_entry:
            case "0":
                return 0
            case "1":
                players = sort_players_by_name(players_from_db)
                report_all_players_from_db_old(players)
            case "2":
                players = sort_players_by_ranking(players_from_db)
                report_all_players_from_db_old(players)
            case _:
                continue


def report_all_players_from_db_old(list_of_players_sorted):
    user_entry = True
    while user_entry:
        user_entry = PlayerViews.display_player_from_db(list_of_players_sorted)
        match user_entry:
            case "0":
                return 'main_menu'
            case _:
                user_entry = int(user_entry) - 1
                if user_entry >= len(list_of_players_sorted):
                    continue
                else:
                    get_info_player(list_of_players_sorted[user_entry])


def get_info_player(player):
    user_entry = 0
    while user_entry != "1" or user_entry != "2":
        user_entry = PlayerViews.display_infos_player(player)
        match user_entry:
            case "1":
                report_all_players_from_db()
            case "2":
                PlayerController.update_ranking_of_player(player)
            case "3":
                break
            case _:
                continue


def report_all_tournaments_from_db(state):
    tournaments = Deserialize.tournament(state)
    user_entry = True
    while user_entry:
        user_entry = TournamentViews.display_tournaments_from_db(tournaments)
        match user_entry:
            case "0":
                return 'main_menu'
            case _:
                user_entry = int(user_entry) - 1
                if user_entry >= len(tournaments):
                    continue
                else:
                    get_infos_tournament(tournaments[user_entry])


def report_players_from_tournament(list_of_players):
    user_entry = 0
    while user_entry != "0" or user_entry != "1":
        user_entry = Menus.sort_players_by_name_or_ranking()
        match user_entry:
            case "0":
                return 0
            case "1":
                players = sort_players_by_name(list_of_players)
                TournamentViews.display_players_from_tournament(players)
            case "2":
                players = sort_players_by_number_of_points(list_of_players)
                TournamentViews.display_players_from_tournament(players)
            case _:
                continue


def get_infos_tournament(tournament):
    user_entry = 0
    while user_entry != "0" or user_entry != "1":
        user_entry = TournamentViews.display_infos_tournaments(tournament)
        match user_entry:
            case "0":
                return 0
            case "1":
                report_players_from_tournament(tournament.players)
            case "2":
                Deserialize.round_of_tournament(tournament.id_tournament)
            case "3":
                user_entry_choose_state_of_tournament()
            case _:
                continue


def report_rounds_from_tournament():
    pass


def user_entry_choose_state_of_tournament():
    user_entry = "0"
    while user_entry:
        user_entry = TournamentViews.state_of_tournaments_to_report()
        match user_entry:
            case "0":
                break
            case "1":
                report_all_tournaments_from_db("done")
            case "2":
                report_all_tournaments_from_db("doing")
