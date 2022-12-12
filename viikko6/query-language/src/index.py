from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, All, HasAtLeast, PlaysIn, HasFewerThan, Not, Or
from matchers import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = query.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()




    for player in stats.matches(matcher):
        print(player)
    
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))



if __name__ == "__main__":
    main()
