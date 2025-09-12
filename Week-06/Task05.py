# Week-06/Task05.py
# Task 5: Write a program to demonstrate multithreading by
# creating and running multiple threads to perform different tasks
# simultaneously.
print ("=== TASK #5 OUTPUT ===")

import threading
import time

def numbers():
    for i in range(1, 3):
        print(f"Numbers: {i}")
        time.sleep(1)

def letters():
    for abc in "ABC":
        print(f"Letters: {abc}")
        time.sleep(1)

def symbols():
    for sym in "$@!":
        print(f"Symbols: {sym}")
        time.sleep(1)

t1 = threading.Thread(target= numbers)
t2 = threading.Thread(target= letters)
t3 = threading.Thread(target= symbols)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("Multi-Tasking Done! ✅")