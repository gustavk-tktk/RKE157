from search_by_publisher import get_games_by_publisher


def main():
    games = get_games_by_publisher("nintendo")

    for game in games:
        print(game)


if __name__ == "__main__":
    main()