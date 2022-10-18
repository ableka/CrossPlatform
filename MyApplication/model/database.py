import sqlite3


class DataBase:

    def __init__(self):
        self.database = "C:/Users/alexa/PycharmProjects/CrossPlatform/MyApplication/model/users.db"
        self.connection = sqlite3.connect(self.database)

    def new_user(self, username, password):
        cursor = self.connection.cursor()
        sql = """INSERT INTO USERS (Username, Password) VALUES(?,?)"""
        cursor.execute(sql, (username, password))
        self.connection.commit()

    def delete_duplicates(self):
        print("I'm here")
        cursor = self.connection.cursor()
        sql = """ DELETE FROM USERS WHERE ROWID NOT IN
            (SELECT MAX(ROWID) FROM USERS GROUP BY Username)"""
        cursor.execute(sql)
        self.connection.commit()
        self.delete_nulls()

    def delete_nulls(self):
        print("I'm here")
        cursor = self.connection.cursor()
        sql = """ DELETE FROM USERS WHERE Password = '' or Username = '' """
        cursor.execute(sql)
        self.connection.commit()
