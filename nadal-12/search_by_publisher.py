import sqlite3


def get_games_by_publisher(publisher_name):

    with sqlite3.connect(r"db\TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Game.name, Publisher.name
            FROM Game
            JOIN GamePublisher ON Game.id = GamePublisher.gameId
            JOIN Publisher ON Publisher.id = GamePublisher.publisherId
            WHERE LOWER(Publisher.name) = LOWER(:publisher_name)
            ORDER BY Game.name
        """, {"publisher_name": publisher_name})
    
    return cursor.fetchall()
