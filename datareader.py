import sqlite3

def read_all():
    con = sqlite3.connect('tickers.db')
    cur = con.cursor()

    for row in cur.execute('SELECT * FROM tickers ORDER BY symbol'):
        print(row)

    con.close()

read_all()