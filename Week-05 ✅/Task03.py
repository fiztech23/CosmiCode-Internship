# Week-05/Task03.py
# Task 3: Create a program to demonstrate the concept of
# inheritance by creating a base class for a vehicle and derived
# classes for car and bike.
print ("=== TASK #3 OUTPUT ===")

class Vehicle:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def beast1(self):
        print(f"Model: {self.model}\nBrand: {self.brand}\nCH-R is a Game-changer, One of my favourite cars. 💟\nIt's a beast!! 🔥")
    
    def beast2(self):
        print(f"Model: {self.model}\nBrand: {self.brand}\nIt's a cool one.\nSuper fast!! 🔥")
    
class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

car = Car("Toyota", "CH-R", "2023")
bike = Bike("Honda", "125", "2025")

car.beast1()
bike.beast2()
