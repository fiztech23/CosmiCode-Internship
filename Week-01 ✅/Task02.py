# Week-01/Task02.py
# Task 2: Create a program to perform advanced arithmetic
# operations (power, modulo) using functions.
print ("=== TASK #2 OUTPUT ===")

num = int(input("Enter your number: "))
def math_operation(n):
    power = n ** 2
    module = n % 2 
    return power, module 
power_result, module_result = math_operation(num)  
print(f"The power of {num} is: {power_result}")
print(f'The module of {num} is: {module_result}')