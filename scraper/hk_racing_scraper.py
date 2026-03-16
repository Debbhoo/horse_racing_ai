import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://racing.hkjc.com/racing/information/English/Racing/LocalResults.aspx"

print("CONNECTING TO HKJC...")

response = requests.get(url)

print("STATUS CODE:", response.status_code)

if response.status_code == 200:

    print("SUCCESS: CONNECTED")

    soup = BeautifulSoup(response.text, "html.parser")

    races = soup. select("select option")

    conn = sqlite3.connect("database/racing.db")
    cursor = conn.cursor()

    print("SAVING RACE DATES...")

    for race in races[:20]:

        date = race.text.strip()

        cursor.execute("""
        INSERT INTO race (race_date)
        VALUES (?)
        """, (date,))

        print("Saved:", date)

    conn.commit()
    conn.close()

    print("DONE")

else:

    print("FAILED TO CONNECT")