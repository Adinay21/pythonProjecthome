import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    CREATE TABLE IF NOT EXISTS reviews (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        phone_number VARCHAR,
                        instagram_username TEXT,
                        visit_date DATA,
                        food_rating INTEGER,
                        cleanliness_rating INTEGER,
                        extra_comments TEXT
                    )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS dishes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                price INTEGER NOT NULL
                )
                """
            )
            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)
            conn.commit()


    def fetch(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as conn:
            if not params:
                params = tuple()
            result = conn.execute(query, params)
            result.row_factory = sqlite3.Row
            return result.fetchall()
            return [dict(r) for r in data]

