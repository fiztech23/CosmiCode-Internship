# Week-05/Task02.py
# Task 2: Implement a class hierarchy to represent geometric
# shapes (e.g., Circle, Rectangle, Triangle) with methods to
# calculate area and perimeter.
print ("=== TASK #2 OUTPUT ===")

import math
class Geometric_shapes:
    def __init__(self):
        pass

    def circle(self):
        print("== Finding the Area and Perimeter of Circle ==")
        a = int(input("Enter radius: "))
        calculate_area = math.pi* (a**2)
        calculate_perimeter = 2 * math.pi * a
        print(f"The area of circle is {calculate_area}")
        print(f"The perimeter of circle is {calculate_perimeter}")
        
    def rectangle(self):
        print("== Finding the Area and Perimeter of Rectangle ==")
        a = int(input("Enter length: "))
        b = int(input("Enter width: "))
        calculate_area2 = a * b
        calculate_perimeter2 = 2 * (a+b)
        print(f"The area of rectangle is {calculate_area2}")
        print(f"The perimeter of rectangle is {calculate_perimeter2}")

    def triangle(self):
        print("== Finding the Area and Perimeter of Triangle ==")
        a = int(input("Enter number (base): "))
        b = int(input("Enter number (height): "))
        c = int(input("Enter number (third side): "))
        calculate_area3 = 1/2 * a * b
        calculate_perimeter3 = a+b+c
        print(f"The area of triangle is {calculate_area3}")
        print(f"The perimeter of triangle is {calculate_perimeter3}")

shapes = Geometric_shapes()
shapes.circle()
shapes.rectangle()
shapes.triangle()