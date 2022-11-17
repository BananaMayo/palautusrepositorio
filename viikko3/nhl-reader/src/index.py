import requests
from player import Player
def sort(player):
    return player.assists + player.goals

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'])
    
        players.append(player)

    sorted_players = sorted(players, reverse=True, key=sort)
    print("Pelaajat:")

    for player in sorted_players:
        if(player.get_kansallisuus()=="FIN"):
            print(player)

if __name__ == "__main__":
    main()


""" from player import Player

def main():
    pass

if __name__ == "__main__":
    main() """