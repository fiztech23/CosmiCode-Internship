# Week-06/Task02.py
# Task 2: Implement exception handling in a program that
# performs complex mathematical calculations, ensuring it handles
# various potential errors.
print ("=== TASK #2 OUTPUT ===")

def complex_calculation(x, y, op):
   if op == "+":
      return x + y
   elif op == "-":
       return x - y
   elif op=="*":
       return x * y
   elif op=="/":
       return x / y   
   else :
       raise ValueError("Operation Failed!")
try:
    x = int(input("Enter first number: ")) 
    y = int(input("Enter second number: ")) 
    op = input("Choose +, -, * or /: ")
    result = complex_calculation(x, y, op)
    print(f"Result of {x} {op} {y} = {result}")
except ZeroDivisionError:
    print("❌ Error: Division by zero is not allowed.")
except ValueError:
    print("❌ Error: Invalid numeric value.")
except Exception as e: 
    print("❌ Unexpected Error:", e)
else:
    print("✅ Calculation successful! Result:", result)
finally:
    print("🔹 Program finished!")



