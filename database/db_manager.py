import sqlite3
import os

print("CREATING DATABASE...")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "racing.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# races table
cursor.execute("""
CREATE TABLE IF NOT EXISTS race(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    race_date TEXT
)
""")

# horse table
cursor.execute("""
CREATE TABLE IF NOT EXISTS horses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    horse_name TEXT
)
""")


# jockeys table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jockeys(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jocky_name TEXT
)
""")

# race results table
cursor.execute("""
CREATE TABLE IF NOT EXISTS race_results(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    race_id INTEGER,
    horse_id INTEGER,
    jockey_id INTEGER,
    position INTEGER,
    odds REAL
)
""")

conn.commit()

print("DATABASE READY")

conn.close()