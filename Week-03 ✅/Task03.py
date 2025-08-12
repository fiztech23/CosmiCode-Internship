# Week-03/Task03.py
# Task 3: Write a program to find the longest word in a sentence
# provided by the user, ignoring punctuation.
print("=== TASK #3 OUTPUT ===")

user_input = input("Enter a sentence: ")
import string 
cleaned_input = "" 
for char in user_input:
    if char not in string.punctuation:
        cleaned_input += char
words = cleaned_input.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word in this sentence is:", longest_word)
