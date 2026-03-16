import sqlite3

DB_PATH = "database/racing.db"

print("STARTING HORSE PERFORMANCE ANALYSIS")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT horses.horse, COUNT(*) as races
FROM race_results
JOIN horses ON race_results.horse_id = horses.id
GROUP BY horses.horse
ORDER BY races DESC
LIMIT 10
""")

results = cursor.fetchall()

print("\nTOP 10 MOST ACTIVE HORSES\n")

for horse in results:
    print(f"Horse: {horse[0]} | Races: {horse[1]}")

conn.close()

print("\nDONE")