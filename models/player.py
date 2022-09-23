from database.database import Database


class Player:
    def __init__(self, id, name, first_name, date_of_birth, sex, ranking, number_of_points, played_with):
        self.id = id
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking
        self.number_of_points = number_of_points
        self.played_with = played_with

    def save_player(self):
        Database.save_player(self)

    def update_ranking(self, ranking):
        Database.update_ranking_player(self.id, ranking)

    def __str__(self):
        return f"{self.first_name} {self.name}"
