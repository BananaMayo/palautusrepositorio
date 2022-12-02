class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def advantage_or_win(self):
        status = ["Advantage ", "Win for "]
        index = max(0,min(abs(self.player2_score - self.player1_score)-1, 1))
        if self.player1_score > self. player2_score:
            return status[index]+self.player1_name
        else:
            return status[index]+self.player2_name

    def get_score(self):
        scores = ["Love", "Fifteen", "Thirty", "Forty", "Deuce"]

        if self.player1_score == self.player2_score:
            return scores[self.player1_score]+"-All" if self.player1_score < 4 else "Deuce"

        elif self.player1_score >= 4 or self.player2_score >= 4:
           return self.advantage_or_win()

        else:
            return scores[self.player1_score]+"-"+scores[self.player2_score]
