import sqlite3

def init_db():
    con = sqlite3.connect('tickers.db')
    cur = con.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS tickers (symbol text, price real, timestamp real)''')

    con.commit()
    con.close()