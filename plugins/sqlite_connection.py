import sqlite3
import os
import datetime

from plugins.config import CONFIGURATION


class SqliteConnection:
    def __init__(self, filename):
        need_init = False
        if not os.path.exists(CONFIGURATION.config['Target'] + "\\{}.sqlite".format(filename)):
            open('{}.sqlite'.format(filename), 'w').close()
            need_init = True
        connection_string = '{}.sqlite'.format(filename)
        sqlite_connection = sqlite3.connect(connection_string)
        self.connection = sqlite_connection
        if need_init:
            self.init_database()

    def init_database(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE following(userid, timestamp)")
        self.commit_change()
        cursor.close()
        return

    def commit_change(self):
        self.connection.commit()
        return

    def record_row_following(self, userid):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO following VALUES('{userid}', '{timestamp}')".format(
            userid=userid,
            timestamp=datetime.datetime.now()
        ))
        self.commit_change()
        cursor.close()
        return

    def check_if_not_archived(self, userid):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM following WHERE userid = \"{}\"".format(userid))
        result = cursor.fetchone()
        cursor.close()
        return result

    def close_connection(self):
        self.connection.close()
        return
