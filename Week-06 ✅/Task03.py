# Week-06/Task03.py
# Task 3: Create a program to read from and write to a JSON file,
# demonstrating JSON handling in Python.
print ("=== TASK #3 OUTPUT ===")

import json 
Student1 = {
    "Name": "Amna", 
    "Roll no": "100",
    "Course_name": "Python",
    "Fee_structure": "5000"
}
Student2 = {
    "Name": "Ayesha", 
    "Roll no": "101",
    "Course_name": "Python",
    "Fee_structure": "5000"     
}
Student3 = {
    "Name": "Hifsa", 
    "Roll no": "102",
    "Course_name": "Python",
    "Fee_structure": "5000"    
}  
Students = [Student1, Student2, Student3]
with open ("students.json", "w") as f:
    json.dump(Students, f, indent = 4)
with open ("students.json", "r") as f:
    data = json.load(f)

print(data)
