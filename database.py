import sqlite3

connection = sqlite3.connect("data.db")


def create_table():
    """
    Creates the 'entries' table in the database if it does not already exist.
    The table contains two columns: 'content' (TEXT) and 'date' (TEXT).
    """
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT)"
        )


def add_entry(entry_content, entry_date):
    """
    Inserts a new entry into the 'entries' table.

    Args:
        entry_content (str): The content of the diary entry.
        entry_date (str): The date associated with the entry.
    """
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?,?);", (entry_content, entry_date)
        )


def get_entries():
    """
    Retrieves all entries from the 'entries' table.

    Returns:
        sqlite3.Cursor: A cursor object containing all rows from the 'entries' table.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM entries;")
    return cursor
