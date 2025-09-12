# Week-06/Task01.py
# Task 1: Write a program to demonstrate the use of decorators to
# measure the execution time of functions.
print ("=== TASK #1 OUTPUT ===")

import time 
def execute(func):
    def timings(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time: ", end - start, "seconds")
        return result
    return timings

@execute
def execution_time():
    print("Hello, My name is Teddy!🧸")
    total = 0
    for i in range(1, 1000000):
        total += i 
    return total
execution_time()