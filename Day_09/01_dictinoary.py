# -----------------------------
# Dictionary in Python
# -----------------------------

# A dictionary is an unordered collection of key-value pairs.
# - Keys are unique
# - Values can be of any type
# - Use curly braces {} or the dict() function

# -----------------------------
# Creating a Dictionary
# -----------------------------

# Syntax:
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)

# Using dict()
info = dict(name="Bob", age=30)
print(info)

# -----------------------------
# Accessing Values
# -----------------------------

# Using key
print(person["name"])  # Alice

# Using get() - returns None if key doesn't exist (no error)
print(person.get("gender"))  # None

# -----------------------------
# Adding and Updating Items
# -----------------------------

person["email"] = "alice@example.com"  # Add new key
person["age"] = 26                     # Update existing key
print(person)

# -----------------------------
# Removing Items
# -----------------------------

# pop() - removes key and returns value
email = person.pop("email")
print(email)
print(person)

# popitem() - removes and returns the last inserted pair (Python 3.7+)
last = person.popitem()
print(last)
print(person)

# del - deletes a specific key
del person["age"]
print(person)

# clear() - removes sall items
person.clear()
print(person)  # {}

# -----------------------------
# Dictionary Methods
# -----------------------------

student = {
    "name": "John",
    "age": 21,
    "grade": "A"
}

# keys()
print(student.keys())  # dict_keys(['name', 'age', 'grade'])

# values()
print(student.values())  # dict_values(['John', 21, 'A'])

# items()
print(student.items())  # dict_items([('name', 'John'), ('age', 21), ('grade', 'A')])

# update() - merge with another dictionary
extra = {"gender": "Male", "grade": "A+"}
student.update(extra)
print(student)

# -----------------------------
# Looping Through a Dictionary
# -----------------------------

# Loop through keys
for key in student:
    print(key, student[key])

# Loop through keys and values
for key, value in student.items():
    print(f"{key} → {value}")
