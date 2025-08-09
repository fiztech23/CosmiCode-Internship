# Week-02/Task04.py
# Task 4: Implement a program to find all the prime factors of a
# given number.
print("=== TASK #4 OUTPUT ===")

num = int(input("Enter a number to find the prime factor: "))
i = 2 
while num > 1:
    if num % i == 0:
        print(i, end=' ')
        num = num // i 
    else:
        i += 1 
print("\nAll prime factors found!")