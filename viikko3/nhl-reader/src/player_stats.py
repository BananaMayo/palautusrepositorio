from player_reader import PlayerReader

def sort(player):
    return player.points

class PlayerStats:
    def __init__(self, playerReader:PlayerReader):
        self.players = playerReader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        players = []
        sorted_players = sorted(self.players, reverse=True, key=sort)
        for player in sorted_players:
            if(player.get_kansallisuus()==nationality):
                players.append(player)
        return players

