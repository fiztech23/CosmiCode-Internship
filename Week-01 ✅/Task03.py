# Week-01/Task03.py
# Task 3: Write a program that takes user input for three numbers
# and prints the largest and smallest among them.
print ("=== TASK #3 OUTPUT ===")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Using built-in functions
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print("The Largest number is:", largest)
print("The Smallest number is:", smallest)
