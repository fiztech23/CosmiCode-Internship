# Week-04/Task04.py
# Task 4: Implement a program that uses a dictionary to count the
# frequency of each character in a string.
print("=== TASK #4 OUTPUT ===")

user_input = input("Enter a word or sentence:  ")
frequency = {}
for char in user_input:
    if char in frequency: 
        frequency[char] += 1
    else:
        frequency[char] = 1 

print("Frequency of each  character: ", frequency)
for char, count in frequency.items():
    print("Frequency for the character",char, "is", count)



