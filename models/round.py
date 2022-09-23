class Match:
    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def __str__(self):
        return f"{self.player1.__repr__()} ({self.score_player1}) vs {self.player2.__repr__()} ({self.score_player2})"


class Round:
    def __init__(self, list_of_matchs):
        self.list_of_matchs = list_of_matchs
