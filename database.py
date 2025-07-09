import sqlite3

connection = sqlite3.connect("data.db")


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT)"
        )


# entries = []


def add_entry(entry_content, entry_date):
    # entries.append({"content": entry_content, "date": entry_date})
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?,?);", (entry_content, entry_date)
        )
        # do it like above instead of f strings to avaoid injection attacks


def get_entries():
    # return entries
    cursor = connection.cursor()
    cursor.execute{"SELECT * FROM entries"}
    return cursor.fetchall()
