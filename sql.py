import sqlite3


class Sql:
    def __init__(self):
        self.connection = sqlite3.connect('paynet.db')
        self.cursor = self.connection.cursor()

    def create_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
               id integer PRIMARY KEY,
               username varchar(50),
               link varchar(50),
               friends integer,
               ish_sum integer,
               yech_sum integer,
               qol_sum integer,
               tel varchar(13),
               click varchar(16),
               )''')
        return self.connection.commit()
    
    def user(self, user):
        self.cursor.execute('''INSERT INTO users(id, username, link, tg_name) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            user)
        return self.connection.commit()

    def user_update_tel(self, user):
        self.cursor.execute(f'''UPDATE users SET tel = {user[1]}  WHERE id = {user[0]}''')
        return self.connection.commit()

    def user_update_click(self, user):
        self.cursor.execute(f'''UPDATE users SET click = {user[1]}  WHERE id = {user[0]}''')
        return self.connection.commit()

    def add_friend(self, user):
        c = self.cursor.execute(f'''SELECT friends FROM users WHERE id = {user[0]}''')
        c = c + 1
        ish_sum = self.cursor.execute(f'''SELECT ish_sum FROM users WHERE id = {user[0]}''')
        ish_sum = ish_sum + user[1]
        qol_sum = self.cursor.execute(f'''SELECT qol_sum FROM users WHERE id = {user[0]}''')
        qol_sum = qol_sum + user[1]
        self.cursor.execute(
            f'''UPDATE users SET friends = {c}, ish_sum = {ish_sum}, qol_sum = {qol_sum}  WHERE id = {user[0]}''')

        return self.connection.commit()

    def user_update(self, user):
        c = self.cursor.execute(f'''SELECT ish_sum FROM users WHERE id = {user[0]}''')
        c = c - user[1]
        yech_sum = self.cursor.execute(f'''SELECT yech_sum FROM users WHERE id = {user[0]}''')
        yech_sum = yech_sum + user[1]
        self.cursor.execute(
            f'''UPDATE users SET qol_sum = {c}, yech_sum = {yech_sum}  WHERE id = {user[0]}''')
        return self.connection.commit()

    def user_count(self):
        users_count = self.cursor.execute(f'''SELECT COUNT(id) FROM users WHERE id = {user[0]}''')
        return users_count
