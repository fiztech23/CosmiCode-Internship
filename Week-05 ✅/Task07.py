# Week-05/Task07.py
# Task 7: Implement a class to handle basic file operations
# (reading, writing, appending) for text files.
print("=== TASK #7 OUTPUT ===")

class File_operations:
    def __init__(self): 
        self.filename = "file_practice.txt"

    def write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)
        print("File written successfully!")

    def read(self):
        try:
            with open(self.filename, "r") as f:
                data = f.read()
            print("File content:\n", data)
        except FileNotFoundError:
            print("File not found!")

    def append(self, content):
        with open(self.filename, "a") as f:
            f.write(content)
        print("Appended successfully!")

file = File_operations()

# Write in file
file.write("'Lost time is never found again.' — Benjamin Franklin\n"
        "I still remember my favourite teacher words: 'Time is flying'\n"
        "That thought has never left my mind; life is moving so fast\nthat it feels as if he said it just yesterday, "
        "even though\nmany years have already passed. And perhaps that is why\nthe words are true.\nTime is flying. It truly is!")

# Append more data
file.append("\nLife itself is tied to time.\nEvery moment we lose is a piece of life we can never live again.")

# Read file
file.read()
