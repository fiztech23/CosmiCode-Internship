import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generate_report():
    conn = sqlite3.connect("expenses.db")
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No expenses found!")
        return

    # Group by category
    category_sum = df.groupby("category")["amount"].sum()

    # Plot
    category_sum.plot(kind="pie", autopct='%1.1f%%')
    plt.title("Expense by Category")
    plt.ylabel("")
    plt.show()

# Example use:
# generate_report()
