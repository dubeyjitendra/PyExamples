import sqlite3

class DB:

    def __init__(self):
        pass


    def create_db(self):
        try:
            conn = sqlite3.connect("catering.db")
        except ConnectionAbortedError:
            print("Database is not created")
        return conn

    def create_table(self):

        c = self.create_db()
        # create table in database using below way
        sql = """
                create table login(
                Id number,
                Email char(100),
                Password char(20)
                )
              """
        # run the sql query
        c.execute(sql)
        print("Successfully table created")
        c.close()

    def insert(self):

        c = self.create_db()
        # create table in database using below way
        sql = """
                Insert into login(Id,Email,Password) values(1,'XXXXXX','xxxxxx')
              """
        # run the sql query
        c.execute(sql)
        c.commit()
        print("Record saved successfully")
        c.close()


# obj =DB()
# obj.insert()
