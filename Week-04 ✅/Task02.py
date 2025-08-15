# Week-04/Task02.py
# Task 2: Write a program to perform matrix multiplication for two
# given matrices.
print("=== TASK #2 OUTPUT ===")

A = [[2, 4, 5],
     [3, 2, 1]]

B = [[2, 4], 
     [4, 6],
     [5, 6]]
result = [[0]*len(B[0]) for x in range(len(A))]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
for row in result:
    print(row)