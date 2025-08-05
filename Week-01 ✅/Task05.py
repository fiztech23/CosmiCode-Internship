# Week-01/Task05.py
# Task 5: Create a program that converts a given time in seconds
# to hours, minutes, and seconds.
print("=== TASK #5 OUTPUT ===")

total_seconds = int(input("Enter time in seconds: "))
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
