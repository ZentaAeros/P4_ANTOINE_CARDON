from views.player import PlayerViews
from views.tournament import TournamentViews
from database.deserialize import Deserialize
from database.serialize import Serialize
from models.tournament import Tournament
from models.player import Player
from views.menus import Menus
from controllers.reports import (
    report_all_players_from_db,
    user_entry_choose_state_of_tournament
)
from controllers.utils import (
    create_pairs_first_round,
    create_pairs_next_rounds,
    sort_players_by_number_of_points,
    results_of_matchs
)
from controllers.player import PlayerController
from time import strftime
import sys


class TournamentController:
    def __init__(self):
        self.list_of_players = []
        self.pair_of_players = []
        self.list_of_matchs = []
        self.list_of_players_from_db = []
        self.list_of_tournaments_from_db = []
        self.list_of_rounds = []

    def add_tournament(self):
        # Récupération des informations de la vue
        tournament_form = TournamentViews.create_tournament_form()
        id_tournament = Deserialize.id_tournament()
        datetime_start_tournament = strftime('%d-%m-%Y %H:%M:%S')
        self.tournament = Tournament(
            str(id_tournament),
            datetime_start_tournament,
            tournament_form["name"],
            tournament_form["place"],
            tournament_form["description"],
            self.add_players_on_tournament(),
        )

        id_tournament += 1
        Serialize.id_tournament(id_tournament)

    def add_players_on_tournament(self):
        player_number = 1
        new_player = []
        self.list_of_players = []
        self.list_of_players_from_db = []
        self.list_of_players_from_db = Deserialize.players()
        while player_number <= 8:
            print(f"Joueur n° {player_number}")
            user_entry = TournamentViews.add_or_load_player_menu()
            match user_entry:
                case "1":
                    # Récupération des informations du nouveau joueur depuis la vue
                    id_player = Deserialize.id_player()
                    player_form = PlayerViews.create_player_form()
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
                    new_player.append(player)
                    self.list_of_players.append(player)
                    player_number += 1

                    player.save_player()
                case "2":
                    entry = PlayerViews.display_player_from_db(self.list_of_players_from_db)
                    if entry == "0":
                        continue
                    else:
                        entry = int(entry) - 1
                        self.list_of_players.append(
                            Player(
                                self.list_of_players_from_db[entry].id,
                                self.list_of_players_from_db[entry].name,
                                self.list_of_players_from_db[entry].first_name,
                                self.list_of_players_from_db[entry].date_of_birth,
                                self.list_of_players_from_db[entry].sex,
                                self.list_of_players_from_db[entry].ranking,
                                self.list_of_players_from_db[entry].number_of_points,
                                self.list_of_players_from_db[entry].played_with,
                            )
                        )

                        self.list_of_players_from_db.pop(entry)
                        player_number += 1
                case _:
                    continue

    def save_tournament(self):
        rounds = self.list_of_rounds
        players = self.list_of_players
        self.tournament.save_tournament(players, rounds, "doing")
        print("Le tournoi a bien été sauvegardé")

        start_application()

    def load_tournament(self):
        tournaments = Deserialize.tournament("doing")
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
                        tournament_loading = Deserialize.tournament_loading(tournaments[user_entry].id_tournament)
                        self.tournament = tournament_loading['tournament']
                        self.list_of_players = tournament_loading['tournament'].players
                        self.list_of_rounds = tournament_loading['list_of_rounds']
                        self.start_tournament("load")

    def start_tournament(self, state="new"):
        if state == "new":
            TournamentViews.display_tournament(self.tournament)
            print(f"Tour n°{self.tournament.round_number}")
            datetime_start_round = strftime('%d-%m-%Y %H:%M:%S')
            self.pair_of_players = create_pairs_first_round(self.list_of_players)
            TournamentViews.display_pairs(self.pair_of_players)
            list_of_matchs = results_of_matchs(self.pair_of_players)
            self.save_round(list_of_matchs, datetime_start_round)

            self.menu_between_rounds()

            self.tournament.round_number += 1

            while self.tournament.round_number != self.tournament.number_of_rounds:
                print()
                print(f"Tour n°{self.tournament.round_number}")
                self.next_round()

                self.menu_between_rounds()

                self.tournament.round_number += 1

            print(f"Tour n°{self.tournament.round_number}")
            self.end_round()
            rounds = self.list_of_rounds
            players = self.list_of_players
            self.tournament.datetime_end = strftime('%d-%m-%Y %H:%M:%S')
            self.tournament.save_tournament(players, rounds, "done")

        else:
            TournamentViews.display_tournament(self.tournament)
            self.tournament.round_number += 1
            while self.tournament.round_number != self.tournament.number_of_rounds:
                print()
                print(f"Tour n°{self.tournament.round_number}")
                self.next_round()

                self.menu_between_rounds()

                self.tournament.round_number += 1

            print(f"Tour n°{self.tournament.round_number}")
            self.end_round()
            rounds = self.list_of_rounds
            players = self.list_of_players
            self.tournament.datetime_end = strftime('%d-%m-%Y %H:%M:%S')
            self.tournament.delete_tournament_on_db()
            self.tournament.save_tournament(players, rounds, "done")

    def next_round(self):
        datetime_start_round = strftime('%d-%m-%Y %H:%M:%S')
        self.pair_of_players = create_pairs_next_rounds(self.list_of_players)
        TournamentViews.display_pairs(self.pair_of_players)
        list_of_matchs = results_of_matchs(self.pair_of_players)
        self.save_round(list_of_matchs, datetime_start_round)

    def end_round(self):
        self.next_round()

        print("Le tournoi s'est terminé avec les résultats suivants : ")
        self.list_of_players = sort_players_by_number_of_points(self.list_of_players)
        TournamentViews.display_ranking_by_number_of_points(self.list_of_players)

    def save_round(self, list_of_matchs, datetime_start):
        datetime_end = strftime('%d-%m-%Y %H:%M:%S')
        round = {
            'datetime_start': datetime_start,
            'datetime_end': datetime_end,
            'round': self.tournament.round_number,
            'matchs': list_of_matchs[1]
        }

        self.list_of_rounds.append(round)

    def menu_between_rounds(self):
        user_entry = "0"
        while user_entry:
            user_entry = Menus.between_rounds()

            match user_entry:
                case "1":
                    break
                case "2":
                    self.save_tournament()


def start_application():
    entry = 0
    tournament = TournamentController()
    while entry != "6":
        entry = Menus.main_menu()

        match entry:
            case "1":
                tournament.add_tournament()
                tournament.start_tournament()

            case "2":
                PlayerController.add_player()

            case "3":
                report_all_players_from_db()

            case "4":
                user_entry_choose_state_of_tournament()

            case "5":
                tournament.load_tournament()

    sys.exit()
