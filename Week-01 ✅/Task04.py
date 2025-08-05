# Week-01/Task04.py
# Task 4: Implement a program to calculate the area of complex
# shapes like a trapezoid or an ellipse.
print("=== TASK #4 OUTPUT ===")

choice = input("1. Trapezoid\n2. Ellipse\n3. Both\nEnter the shape type:")
if choice.lower() == "trapezoid" or choice == "1":
    a = float(input("Enter base 1 : "))
    b = float(input("Enter base 2 : "))
    h = float(input("Enter height : "))
    Trapezoid_result = 1/2 * (a + b) * h
    print(f"The area of the trapezoid is: {Trapezoid_result} square units")

elif choice.lower() == "ellipse" or choice == "2":
    a = float(input("Enter major number (a): "))
    b = float(input("Enter minor number (b): "))
    Ellipse_result = 3.14 * a * b
    print(f"The area of the ellipse is: {Ellipse_result} square units")

elif choice.lower() =="both" or choice == "3":
    print("You have chosen both shapes.")
    print("Finding Trapezoid: ")
    a = float(input("Enter base 1 : "))
    b = float(input("Enter base 2 : "))
    h = float(input("Enter height : "))
    Trapezoid_result = 1/2 * (a + b) * h
    print(f"The area of the trapezoid is: {Trapezoid_result} square units")
    print("Finding Ellipse: ")
    a = float(input("Enter major number (a): "))
    b = float(input("Enter minor number (b): "))
    Ellipse_result = 3.14 * a * b
    print(f"The area of the ellipse is: {Ellipse_result} square units")
else:
    print("Invalid shape entered. ")
