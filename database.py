import sqlite3

# Connect to the database file
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# View tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# Example: Read all rows from a table
cursor.execute("SELECT * FROM tasks;")
print(cursor.fetchall())

conn.close()
