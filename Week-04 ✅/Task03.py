# Week-04/Task03.py
# Task 3: Create a program to solve the Tower of Hanoi problem
# recursively
print("=== TASK #3 OUTPUT ===")

def move (a, b):
    print("Move", a , "to", b)
def towerOfHonoi (n, A, B, C):
    if n == 1:
        move(A, C)
    else:
        towerOfHonoi(n-1, A, C, B)
        move(A, C)
        towerOfHonoi(n-1, B, A, C)
n = int(input("Enter the number of disks: "))
towerOfHonoi(n, "A", "B", "C")

#took help from Anjali Sharma Youtube Channel and chatgpt for better understanding 
#Tower of hanoi in Python 