import sqlite3

# Connect to the database (will create if it doesn't exist)
conn = sqlite3.connect("expenses.db")
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT
    )
''')

conn.commit()
conn.close()

print("✅ Database setup complete!")
