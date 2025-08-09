# Week-02/Task05.py
# Task 5: Write a program that takes a list of numbers and finds
# the subarray with the maximum sum (Kadane's Algorithm).
print("=== TASK #5 OUTPUT ===")

arr = list(map(int, input("Enter the list of numbers: ").split()))
print("Array:", arr)
def max_subarray_sum(arr):
    current_sum = 0
    max_sum = arr[0]
    for i in range(len(arr)):
        #Kadane's Algorithm
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)
        if current_sum < 0: 
            current_sum = 0 
    return max_sum
max_subarray_sum(arr)

print("The maximum subarray sum is:", max_subarray_sum(arr))