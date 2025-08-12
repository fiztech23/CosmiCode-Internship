# Week-03/Task02.py
# Task 2: Create a program that reverses a list without using builtin
# functions and prints both the original and reversed lists.
print("=== TASK #2 OUTPUT ===")

l1 = [10, 20, 30, 40, 50]
reverse_l1 = []
for i in range(len(l1) -1, -1, -1):
    reverse_l1.append(l1[i])

print("Original list:", l1)
print("Reversed list:", reverse_l1)