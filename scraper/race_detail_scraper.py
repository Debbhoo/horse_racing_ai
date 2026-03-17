import os
import sqlite3
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup


print("STARTING SELENIUM SCRAPER")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "database", "racing.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("SELECT race_date FROM race")
races = cursor.fetchall()


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


for race in races:

    race_date = race[0]

    day, month,year =race_date.split("/")
    race_date = f"{year}/{month}/{day}"

    print("Checking race date:", race_date)

    url = f"https://racing.hkjc.com/racing/information/English/Racing/ResultsAll.aspx?RaceDate=2026/03/15"
    driver.switch_to.default_content()
    driver.get(url)

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

horses = driver.find_elements(By.CSS_SELECTOR, ".horsetable tbody tr")

for horse in horses:
    cols = horse.find_elements(By.TAG_NAME, "td")

    if len(cols) > 5:
        horse_name = cols[3].text
        jockey = cols[4].text
        trainer = cols[5].text
        draw = cols[2].text

        print(horse_name, jockey, trainer, draw)

    try:
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
    except:
        print("Page did not load tables yet")

    iframes = driver.find_elements("tag name", "iframe")
    print("IFRAMES FOUND:", len(iframes))

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    tables = soup.select("table.f_fs13")

    print("Tables found:", len(tables))

    tables = driver.find_elements(By.TAG_NAME, "table")

    print("Tables found:", len(tables))

    for table in tables:
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")

            if len(cols) >= 10:
                horse_name = cols[3].text
                jockey = cols[4].text
                trainer = cols[5].text
                draw = cols[2].text

                print(horse_name, jockey, trainer, draw)

    for i, table in enumerate(tables):
        print("TABLE", i)


driver.quit()
conn.close()
print("SCRAPER FINISHED")