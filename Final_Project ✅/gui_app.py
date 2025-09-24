import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Add expense to DB
def add_expense():
    date = entry_date.get()
    category = entry_category.get()
    amount = entry_amount.get()
    description = entry_description.get()

    if not date or not category or not amount:
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    try:
        conn = sqlite3.connect("expenses.db")
        c = conn.cursor()
        c.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                  (date, category, float(amount), description))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Expense added successfully!")
        clear_fields()
        entry_date.focus_set()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_expenses():
    conn = sqlite3.connect("expenses.db")
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()

    top = tk.Toplevel(root)
    top.title("All Expenses")
    top.configure(bg="#F0F0F0")
    top.geometry("600x400")

    text = tk.Text(top, wrap="none", font=("Courier", 10))
    text.insert(tk.END, df.to_string(index=False))
    text.pack(expand=True, fill="both")

def generate_report():
    conn = sqlite3.connect("expenses.db")
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()

    if df.empty:
        messagebox.showinfo("Info", "No expenses found!")
        return

    category_sum = df.groupby("category")["amount"].sum()
    category_sum.plot(kind="pie", autopct='%1.1f%%', startangle=90, colors=["#ff9999","#66b3ff","#99ff99","#ffcc99"])
    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.axis('equal')
    plt.show()

def clear_fields():
    entry_date.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_description.delete(0, tk.END)

# GUI Window Setup 
root = tk.Tk()
root.title("Expense Tracker App")
root.geometry("500x350")  # Bigger window
root.configure(bg="#e6f2ff")  # Light blue background

font_label = ("Arial", 12)
font_entry = ("Arial", 11)

# Labels and Entries
tk.Label(root, text="Date (YYYY-MM-DD):", bg="#e6f2ff", font=font_label).grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_date = tk.Entry(root, font=font_entry)
entry_date.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Category:", bg="#e6f2ff", font=font_label).grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_category = tk.Entry(root, font=font_entry)
entry_category.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Amount:", bg="#e6f2ff", font=font_label).grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_amount = tk.Entry(root, font=font_entry)
entry_amount.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Description:", bg="#e6f2ff", font=font_label).grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_description = tk.Entry(root, font=font_entry)
entry_description.grid(row=3, column=1, padx=10, pady=5)

# Keyboard navigation 
def focus_next(event, next_widget):
    next_widget.focus_set()

entry_date.bind("<Return>", lambda e: focus_next(e, entry_category))
entry_category.bind("<Return>", lambda e: focus_next(e, entry_amount))
entry_amount.bind("<Return>", lambda e: focus_next(e, entry_description))
entry_description.bind("<Return>", lambda e: add_expense())

# --- Buttons ---
btn_add = tk.Button(root, text="Add Expense", bg="#4CAF50", fg="white", font=font_label, command=add_expense)
btn_add.grid(row=4, column=0, pady=20, padx=10)

btn_view = tk.Button(root, text="View Expenses", bg="#2196F3", fg="white", font=font_label, command=view_expenses)
btn_view.grid(row=4, column=1, pady=20)

btn_report = tk.Button(root, text="Generate Report", bg="#f44336", fg="white", font=font_label, command=generate_report)
btn_report.grid(row=5, column=0, columnspan=2, pady=10)

entry_date.focus_set()

root.mainloop()
