# Week-06/Task07.py
# Task 7: Final Project: Develop a comprehensive data analysis
# application that includes data input, processing, visualization,
# and export functionalities. This project should integrate concepts
# from all previous tasks and demonstrate a thorough
# understanding of Python programming.
print ("=== Final Project Output ===")

import csv
import matplotlib.pyplot as plt
file = r"b:\python\Online-Store-Orders.csv"
data = []
with open(file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)
for row in data:
    try:
        row["TotalPrice"] = float(row["TotalPrice"])
    except:
        row["TotalPrice"] = 0.0

    if len(row["Date"]) >= 7:
        row["Month"] = row["Date"][:7]   # YYYY-MM
    else:
        row["Month"] = "Unknown"

# Top products calculation
product_sales = {}
for row in data:
    product = row["Product"]
    product_sales[product] = round(product_sales.get(product, 0) + row["TotalPrice"], 2)

top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]

# Monthly sales
monthly_sales = {}
for row in data:
    month = row["Month"]
    monthly_sales[month] = round(monthly_sales.get(month, 0) + row["TotalPrice"], 2)

# Payment methods
payment_counts = {}
for row in data:
    method = row["PaymentMethod"]
    payment_counts[method] = payment_counts.get(method, 0) + 1
print("Top Products by Sales:", top_products)
print("Monthly Sales:", monthly_sales)
print("Payment Methods:", payment_counts)
plt.figure(figsize=(15, 5))

# Top products bar chart
plt.subplot(1, 3, 1)
plt.bar([p for p, _ in top_products], [s for _, s in top_products], color="orange")
plt.title("Top 5 Products")
plt.xticks(rotation=30)

# Monthly sales line chart
plt.subplot(1, 3, 2)
plt.plot(list(monthly_sales.keys()), list(monthly_sales.values()), marker="o", color="green")
plt.title("Monthly Sales")
plt.xticks(rotation=45)

# Payment methods pie chart
plt.subplot(1, 3, 3)
plt.pie(payment_counts.values(), labels=payment_counts.keys(), autopct="%1.1f%%")
plt.title("Payment Methods")

plt.tight_layout()
plt.show()









