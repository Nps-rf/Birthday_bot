import sqlite3


class Connections(object):
    database = 'Users.db'

    @staticmethod
    def safe(func):
        def inside(*args, **kwargs):
            with sqlite3.connect(Connections.database) as connection:
                result = func(*args, connection=(connection, connection.cursor()), **kwargs)
            return result
        return inside


class Database(object):

    @Connections.safe
    def all_users(self, connection):
        connection, cursor = connection
        cursor = cursor.execute(
            '''SELECT ALL chat_id FROM Users'''
        )
        connection.commit()
        return cursor.fetchall()

    @Connections.safe
    def add_user(self, connection: tuple, chat_id: str, username: str, phone: str, full_name: str):
        connection, cursor = connection
        cursor.execute('''INSERT INTO Users (chat_id, username, phone, full_name) VALUES (?, ?, ?, ?)''',
                       (chat_id, username, phone, full_name))

        connection.commit()

    @Connections.safe
    def init(self, connection: tuple) -> None:
        """Инициализация БД, пиво, инициализация БД"""
        connection, cursor = connection
        print('Creating "Users" Table...')
        cursor.execute('''create table if not exists Users (
        id          INTEGER primary key,
        chat_id     TEXT not null,
        username  TEXT not null,
        phone TEXT not null,
        full_name TEXT not null
        )''')
        connection.commit()


if __name__ == '__main__':
    db = Database()
    db.init()
