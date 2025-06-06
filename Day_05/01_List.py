# Day 04 – Python Lists

# 🧠 List: Ordered and mutable (changeable) collection of items
# Lists are defined using square brackets [] and can contain mixed data types.

# Basic List

a = [1, 2, 3, 4, 5, "Bigyan", True]
print(a)
print(type(a))  # Output: <class 'list'>
print(a[0])      # Output: 1
print(a[5])      # Output: Bigyan
print(a[6])      # Output: True

# Indexing:
# Positive Index starts from 0
# Negative Index starts from -1
print(a[-5])          # Output: 3 (Negative indexing)
print(a[2])           # Output: 3 (Positive indexing)
print(a[len(a)-5])    # Output: 3 (Using len)

# Membership Test
if "Bigyan" in a:
    print("Yes")
else:
    print("No")

if "gyan" in "Bigyan":
    print("Yes")
else:
    print("No")

# Slicing: list[start:end:step]
print(a[0:5:3])      # Output: [1, 4]
print(a[0:7:2])      # Output: [1, 3, 5, True]
print(a[0:len(a)])   # Output: full list


# 🔹 List Comprehension
# A short way to create a list from any iterable

# Syntax:
# [expression for item in iterable]
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

# With condition:
# [expression_if_true if condition else expression_if_false for item in iterable]
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # Output: ['even', 'odd', 'even', 'odd', 'even']


# 🔹 List Methods
lst = [3, 3, 0, 5, 1, 8, 9, 7, 1, 5]
print(lst)

lst.append(8)           # Add item at end
print(lst)

lst.reverse()           # Reverse the list
print(lst)

print(lst.index(5))     # First index of value 5
print(lst.count(3))     # Count how many times 3 appears

lst.sort(reverse=True)  # Sort in descending order
print(lst)

lst.insert(4, 7)        # Insert 7 at index 4
print(lst)

lst.remove(7)           # Remove first occurrence of 7
print(lst)

lst.extend("naygiBB")   # Extend list with characters from string
print(lst)

lst.pop()               # Remove last element
print(lst)

lst.reverse()           # Reverse again
print(lst)

print(lst.clear())      # Remove all elements (returns None)
