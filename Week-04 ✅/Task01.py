# Week-04/Task01.py
# Task 1: Implement a binary search algorithm to find the position
# of a target value within a sorted list.
print ("=== TASK #1 OUTPUT ===")

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 90
def binary(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
           left = mid + 1 
        else:
            right = mid - 1  
    return -1
print(f"Target {target} found at index: {binary(arr, target)}")