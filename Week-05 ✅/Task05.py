# Week-05/Task05.py
# Task 5: Implement a program that demonstrates polymorphism
# by creating a base class and derived classes with overridden
# methods.
print ("=== TASK #5 OUTPUT ===")

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2
  
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2 
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

shapes = [Circle(5), Square(2), Triangle(8, 10)]

for shape in shapes:
    print(shape.area())

