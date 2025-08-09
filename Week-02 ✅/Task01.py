# Week-02/Task01.py
# Task 1: Write a program to check if a number is prime, and also
# list all prime numbers up to that number.
print ("=== TASK #1 OUTPUT ===")

num = int(input("Enter a number: "))
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
print("Prime numbers up to", num, "are:" )
for n in range(2, num+1):  
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        print(n, end=' ')


