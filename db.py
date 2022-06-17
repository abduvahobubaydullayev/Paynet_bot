import sqlite3


def create_student(a):
    base = sqlite3.connect('MiniMarket.db')
    cur = base.cursor()

    base.execute('CREATE TABLE IF NOT EXISTS {}(nomi, kilosi, sifati, narxi)'.format('meva'))
    base.commit()

    base.executemany('INSERT INTO meva VALUES(?, ?, ?, ?)', a)
    base.commit()
