import sqlite3


def query():
    """queries the db for top five rows"""
    conn = sqlite3.connect("remotehealthDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM remotehealthDB")
    print("Top 5 rows of the remotehealthDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
