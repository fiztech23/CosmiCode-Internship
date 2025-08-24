# Week-05/Task04.py
# Task 4: Write a program to implement operator overloading for
# complex number arithmetic.
print ("=== TASK #4 OUTPUT ===")

class Complex_Number:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex_Number(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex_Number(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex_Number(real, imag)
    
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real*other.real + self.imag*other.imag) / denom
        imag = (self.imag*other.real - self.real*other.imag) / denom
        return Complex_Number(real, imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

z1 = Complex_Number(4, 2)
z2 = Complex_Number(5, 6)

print("Addition: ", z1 + z2)
print("Subtraction: ", z1 - z2)
print("Multiplication: ", z1 * z2)
print("Division: ", z1 / z2)
    
    

