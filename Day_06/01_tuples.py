# Day 05 – Tuples in Python

# 🧐 Tuple: An ordered, immutable (unchangeable) collection of items.
# Items are separated by commas and enclosed in parentheses ().
# Tuples can contain mixed data types: numbers, strings, lists, etc.

# 📌 When to Use Tuples
# - When you want data to be read-only
# - As dictionary keys (since tuples are hashable)
# - In functions to return multiple values

# Creating Tuples
t = (1, 2, 3)
t1 = (7, 8, 9)
t2 = 4, 5, 6         # Without parentheses (still a tuple)
t3 = (7,)            # Single element tuple (note the comma)

print(t)           # Output: (1, 2, 3)
print(type(t))     # Output: <class 'tuple'>
print(t1)
print(t2)
print(t3)
print(type(t2))

# 🔹 Single Element Tuple
t = (5)       # Not a tuple, just an int
print(type(t))  # Output: <class 'int'>

t = (5,)      # This is a tuple
print(type(t))  # Output: <class 'tuple'>

# 🔹 Accessing Tuple Elements (Indexing & Slicing)
t = (10, 20, 30, 40, 50)
print(t[0])     # 10
print(t[-1])    # 50
print(t[1:4])   # (20, 30, 40)

# 🔹 Tuple is Immutable (Cannot Be Changed)
t = (1, 2, 3)
# t[0] = 10       # ❌ Error: 'tuple' object does not support item assignment

# 🔹 Looping Through Tuple
for item in t:
    print(item)

# 🔹 Tuple with Different Data Types
mixed = (1, "Bigyan", 3.14, True)
print(mixed[1])  # Output: Bigyan

# 🔹 Tuple Methods
t = (1, 2, 2, 3, 4)
print(t.count(2))   # Output: 2
print(t.index(3))   # Output: 3

# 🔹 Tuple Packing and Unpacking
info = ("Bigyan", 20, "Nepal")  # Packing
name, age, country = info       # Unpacking
print(name)     # Bigyan
print(age)      # 20
print(country)  # Nepal

# 🔹 Nested Tuples
nested = (1, (2, 3), (4, (5, 6)))
print(nested[1])        # Output: (2, 3)
print(nested[2][1][0])  # Output: 5
