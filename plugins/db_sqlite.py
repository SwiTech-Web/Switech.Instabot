from plugins.sqlite_connection import SqliteConnection


def record_all_rows(filename, following):
    sqlite_connection = SqliteConnection(filename)
    for pseudo in following:
        print(pseudo)
        sqlite_connection.record_row_following(pseudo)
