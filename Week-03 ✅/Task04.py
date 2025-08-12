# Week-03/Task04.py
# Task 4: Implement a program to check if a string is a palindrome,
# ignoring spaces and case sensitivity.
print("=== TASK #4 OUTPUT ===")

user = input("Enter a word or sentence: ")
user = user.replace(" ", "").lower()  
if user == user[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")