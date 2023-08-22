import sqlite3


class Db:
    def __init__(self, name):
        self.name = name
        self.con = sqlite3.connect(self.name)
        self.cur = self.con.cursor()
        self.res = None

    def close(self):
        self.con.commit()
        self.con.close()

    def create_table(self, create: str):
        self.cur.execute(create)

    def insert(self, insert_query: str):
        self.cur.execute(insert_query)

    def select(self, sel):
        self.cur.execute(sel)
        self.res = self.cur.fetchall()
        for i in self.res:
            print(i)
            print("--------------------------")


db = Db("db.db")
db.create_table("CREATE TABLE movie (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, score REAL)")

db.insert("""
    INSERT INTO movie VALUES
        (1, 'Interstellar', 2014, 8.7),
        (2, 'The Others', 2001, 7.6)
""")

db.select("SELECT * FROM movie")

db.close()



def test_insert_data():
    test_db = Db("test.db")
    test_db.create_table("CREATE TABLE movie (id INTEGER PRIMARY KEY, title TEXT)")
    test_db.insert("""
        INSERT INTO movie VALUES
            (1, 'testing')
    """)
    test_db.select("SELECT * FROM movie")
    test_db.close()
    assert test_db.res[0][1] == 'testing'