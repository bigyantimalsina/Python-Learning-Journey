# -----------------------------
# Set in Python
# -----------------------------

# A set is an unordered collection of unique elements.
# - No duplicate values
# - Unordered (no index like lists)
# - We can do mathematical set operations: union, intersection, etc.

# -----------------------------
# Creating a Set
# -----------------------------

# Syntax:
my_set = {1, 2, 3}
print(my_set)

# Or from a list (to remove duplicates):
nums = [1, 2, 2, 3, 4, 4]
unique = set(nums)
print(unique)  # Output: {1, 2, 3, 4}

# -----------------------------
# Set Methods
# -----------------------------

# add(x): Adds x to the set
s = {1, 2}
s.add(3)
print(s)  # {1, 2, 3}

# remove(x): Removes x from the set, gives error if x not present
s.remove(1)
print(s)  # {2, 3}

# discard(x): Removes x if present, no error if not present
s.discard(10)  # No error
print(s)

# pop(): Removes a random item
colors = {"red", "green", "blue"}
colors.pop()
print(colors)  # One color will be removed randomly

# clear(): Removes all items
colors.clear()
print(colors)  # set()

# -----------------------------
# Set Operations
# -----------------------------

a = {1, 2, 3}
b = {2, 3, 4}

# Union: All elements from both sets
print(a | b)  # {1, 2, 3, 4}

# Intersection: Common elements
print(a & b)  # {2, 3}

# Difference: Elements in a but not in b
print(a - b)  # {1}

# Symmetric Difference: Not common in both
print(a ^ b)  # {1, 4}

# -----------------------------
# Looping Through a Set
# -----------------------------

fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)

# -----------------------------
# Example: Remove Duplicates
# -----------------------------

names = ["John", "Alice", "Bob", "Alice", "John"]
unique_names = set(names)
print(unique_names)  # {'John', 'Alice', 'Bob'}

# To print them in sorted order:
print(sorted(unique_names))  # ['Alice', 'Bob', 'John']

