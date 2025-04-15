import sqlite3

def init_db():
    conn = sqlite3.connect("mbta.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            place TEXT NOT NULL,
            station TEXT NOT NULL,
            accessible TEXT NOT NULL,
            latitude REAL,
            longitude REAL
        )
    """)

    conn.commit()
    conn.close()