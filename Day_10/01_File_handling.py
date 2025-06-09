# --------------------------------------------
# 📁 Day_10: File Handling in Python
# --------------------------------------------

# File handling allows you to create, read, write, and delete files.
# You can work with text or binary files using the built-in `open()` function.

# --------------------------------------------
# 🔹 Opening a File
# --------------------------------------------

# Syntax: open(filename, mode)
# Modes:
# 'r' - Read (default)
# 'w' - Write (creates a new file or overwrites)
# 'a' - Append
# 'x' - Create new file, error if exists
# 'b' - Binary mode (e.g., 'rb', 'wb')
# 't' - Text mode (default)

# Example: Writing to a file
f = open("example.txt", "w")
f.write("Hello, this is line one.\n")
f.write("This is line two.\n")
f.close()

# --------------------------------------------
# 🔹 Reading from a File
# --------------------------------------------

f = open("example.txt", "r")
content = f.read()
print("File content:\n", content)
f.close()

# --------------------------------------------
# 🔹 Reading Line-by-Line
# --------------------------------------------

f = open("example.txt", "r")
for line in f:
    print("Line:", line.strip())
f.close()

# --------------------------------------------
# 🔹 Using 'with' (Best Practice)
# --------------------------------------------

# Automatically closes the file
with open("example.txt", "a") as file:
    file.write("This is an added line using with statement.\n")

with open("example.txt", "r") as file:
    print(file.read())

# --------------------------------------------
# 🔹 Read Functions
# --------------------------------------------

# read()         → entire content
# readline()     → one line
# readlines()    → list of lines

with open("example.txt", "r") as f:
    print("First line only:", f.readline())

# --------------------------------------------
# 🔹 Writing Lines from a List
# --------------------------------------------

lines = ["First\n", "Second\n", "Third\n"]
with open("newfile.txt", "w") as f:
    f.writelines(lines)

# --------------------------------------------
# 🔹 Deleting a File (Optional)
# --------------------------------------------

import os

# Check if file exists before deleting
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("File does not exist.")

