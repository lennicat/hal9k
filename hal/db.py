import sqlite3


class Database():
    def __init__(self) -> None:
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor

    def create_db(self):
        self.con.commit()

    def init(self):
        self.create_db()

    