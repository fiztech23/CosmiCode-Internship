# Week-02/Task02.py
# Task 2: Create a program that generates the first 30 Fibonacci
# numbers using both iterative and recursive approaches.
print("=== TASK #2 OUTPUT ===")

print("Using recursive function:")
def recursion_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return (recursion_fibonacci (n-1) + recursion_fibonacci(n-2))
for i in range(31):
    print( recursion_fibonacci(i), end=' ')

print("\n\nUsing iterative function:")
def iterative_fibonacci(x):
    a = 0
    b = 1
    for i in range(x):
        print(a, end=' ')
        next_num = a + b 
        a = b
        b = next_num
iterative_fibonacci (31)

