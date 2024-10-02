import sqlite3


conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()
cursor.execute(
    """
  CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT, 
    email TEXT
  )
"""
)

conn.commit()


# Insert data

cursor.execute(
    """
  INSERT INTO users (name, email) 
  VALUES (?, ?)
""",
    ("John Doe", "john@email.com"),
)

conn.commit()

# Query table

cursor.execute(
    """
  SELECT * FROM users
"""
)

for row in cursor:
    print(row)
