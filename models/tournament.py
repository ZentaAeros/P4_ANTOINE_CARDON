from database.database import Database


class Tournament:
    def __init__(
        self,
        id_tournament,
        datetime_start,
        name,
        place,
        description,
        players,
        number_of_rounds=4,
        round_number=1,
        datetime_end=""
    ):
        self.id_tournament = id_tournament
        self.datetime_start = datetime_start
        self.name = name
        self.place = place
        self.description = description
        self.players = players
        self.number_of_rounds = number_of_rounds
        self.round_number = round_number
        self.datetime_end = datetime_end

    def save_tournament(self, players, rounds, state):
        Database.save_tournament(self, players, rounds, state)

    def delete_tournament_on_db(self):
        Database.remove_tournament(self.id_tournament)

    def __str__(self):
        return f"{self.name}"
