# Week-02/Task03.py
# Task 2: Write a function to calculate the greatest common divisor
# (GCD) and least common multiple (LCM) of two numbers.
print("=== TASK #3 OUTPUT ===")

def lcm_and_gcd(a, b ):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def lcm(x, y):
        return ( x*y ) // gcd(x, y)
    
    gcd_result = gcd(a, b)
    lcm_result = lcm(a, b)
    return gcd_result, lcm_result 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gdc_val, lcm_val = lcm_and_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gdc_val}")
print(f"The LCM of {num1} and {num2} is: {lcm_val}")