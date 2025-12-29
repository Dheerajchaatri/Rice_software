import sqlite3

def get_db():
    conn = sqlite3.connect("rice.db")
    return conn

def setup_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        variety TEXT,
        quantity REAL,
        avg_cost REAL
    )
    """)

    conn.commit()
    conn.close()

