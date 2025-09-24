# 🐍 Python Internship - Final Project 

# Expense Tracker App – Track daily expenses with 
# categories and reports.

# 💰 Expense Tracker App  

A simple yet powerful **GUI-based Expense Tracker App** built with **Python, SQLite, Tkinter, Pandas, and Matplotlib**.  
This app helps users **add, view, and analyze daily expenses** with reports and charts.  


## ✨ Features
- 📝 **Add Expense** – Record expenses with date, category, amount, and description.  
- 📂 **View Expenses** – See all recorded expenses in a clean table.  
- 📊 **Generate Reports** – Visualize spending by category using pie charts.  
- 🗄 **Database Setup** – Automatically creates SQLite database (`expenses.db`).  
- 🖥 **User-Friendly GUI** – Tkinter-based interface with input validation and keyboard navigation.  


## 🛠️ Technologies Used
- **Python 3**  
- **SQLite3** – For database storage  
- **Tkinter** – GUI framework  
- **Pandas** – Data handling and reporting  
- **Matplotlib** – Charts and visualizations  


## 📂 Project Structure

Expense-Tracker-App/
- add_expense.py # Function to add an expense
- gui_app.py # Tkinter GUI application
- report.py # Generate expense reports (charts)
- setup_database.py # Database setup script
- view_expense.py # View all expenses in table form
- expenses.db # SQLite database (auto-created)
- README.md # Project documentation


## ⚙️ Setup Instructions

* Install Required Libraries
* pip install pandas matplotlib
* Setup Database
* python setup_database.py
* Run the GUI App
* python gui_app.py

▶️ Usage Guide

Add Expense: Enter date (YYYY-MM-DD), category, amount, and description → click Add Expense.

View Expenses: Click View Expenses to see all records.

Generate Report: Click Generate Report to see category-wise expense pie chart.

Example (command-line usage):

from add_expense import add_expense

add_expense("2025-09-20", "Food", 500, "Lunch with friends")

📊 Example Output

View Expenses Table

         date category  amount       description
0  2025-09-20     Food   500.0  Lunch with friends
1  2025-09-21  Travel   200.0  Bus ticket


Report (Pie Chart)

Food 🍔 – 60%

Travel 🚗 – 30%

Others – 10%

## 🙌 Personal Note

* Working on this project has been a valuable learning experience. It allowed me to combine Python programming, database management, and GUI development into one complete application. 
* While my internship gave me exposure to handling real-world tasks, this project helped me strengthen my ability to design, implement, and integrate different modules (database, GUI, and reporting).
* This journey not only improved my technical skills but also enhanced my confidence in managing projects independently and preparing for future professional challenges.