# Week-03/Task05.py
# Task 5: Write a program to find the most frequent word in a text
# file.
print("=== TASK #5 OUTPUT ===")

from collections import Counter
import string
with open("B:\\python\\Python Internship\\CosmiCode-Internship\\Week-03\\textfile1.txt", "w") as file:
    text = file.write("""Hello!!\n
My name is Fiza Sohail.\n
I'm learning python to develop my skills in AI/ML.\n
Python is an amazing language.\n
Learning python is very Fun!""")
with open("B:\\python\\Python Internship\\CosmiCode-Internship\\Week-03\\textfile1.txt", "r") as file:
    text = file.read()
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, "")
        words = text.split()
        words_count = Counter(words)
        most_frequent_word = words_count.most_common(1)[0]
print(f"The most frequent word is '{most_frequent_word[0]}' with {most_frequent_word[1]} occurrences.")