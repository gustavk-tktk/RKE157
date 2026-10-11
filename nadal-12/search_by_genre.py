import sqlite3


def get_games_by_genre(genre_name):

    with sqlite3.connect(r"db\TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Game.name, Game.releaseYear, Genre.name
            FROM Game
            JOIN GenreInGame ON Game.id = GenreInGame.gameId
            JOIN Genre ON Genre.id = GenreInGame.genreId
            WHERE LOWER(Genre.name) = LOWER(:genre_name)
            ORDER BY Game.name
        """, {"genre_name": genre_name})
    
    return cursor.fetchall()
