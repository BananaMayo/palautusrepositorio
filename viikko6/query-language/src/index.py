from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, All, HasAtLeast, PlaysIn, HasFewerThan, Not, Or
from matchers import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
    query
        .oneOf(
        query.plays_in("PHI")
            .has_at_least(10, "assists")
            .has_fewer_than(5, "goals")
            .build(),
        query.plays_in("EDM")
            .has_at_least(50, "points")
            .build()
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)

    #pelaajien määrä
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))



if __name__ == "__main__":
    main()
