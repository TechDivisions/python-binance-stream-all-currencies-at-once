import time
import schedule
import urllib.request, json
import datetime
import db
import sqlite3

def job():
    save_data()
    schedule.every(3).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

def save_data():
    db.init_db()

    with urllib.request.urlopen("https://api.binance.com/api/v3/ticker/price") as url:
        data = json.loads(url.read().decode())

        print(datetime.datetime.now())
        print('Amount of currencies: ' + str(len(data)))

        con = sqlite3.connect('tickers.db')
        cur = con.cursor()
        for item in data:
            cur.execute("INSERT INTO tickers VALUES (?, ?, ?)", (item['symbol'], item['price'], time.time()))
        
        con.commit()
        con.close()

job()