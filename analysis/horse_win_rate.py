import sqlite3

DB_PATH = "database/racing.db"

print("CALCULATING HORSE WIN RATES")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT 
    horses.horse_name,
    COUNT(*) as total_races,
    SUM(CASE WHEN race_results.position = 1 THEN 1 ELSE 0 END) as wins
FROM race_results
JOIN horses ON race_results.horse_id = horses.id
GROUP BY horses.horse_name
HAVING total_races >= 3
ORDER BY wins DESC
LIMIT 20
""")

results = cursor.fetchall()

print("\nTOP HORSES BY WINS\n")

for horse_name, races, wins in results:

    win_rate = wins / races

    print(f"{horse_name} | Races: {races} | Wins: {wins} | WinRate: {win_rate:.2f}")

conn.close()

print("\nDONE")