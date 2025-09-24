import sqlite3

def add_expense(date, category, amount, description):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
              (date, category, amount, description))
    conn.commit()
    conn.close()
    print("✅ Expense added successfully!")

# Example use:
# add_expense("2025-09-20", "Food", 500, "Lunch with friends")
