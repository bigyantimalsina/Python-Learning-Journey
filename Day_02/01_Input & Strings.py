# Day 3 – Python Fundamentals: Input and String Handling

# -------------------------
# 1. Input Function Examples
# -------------------------

# Get user input as string
name = input("Enter your name: ")
print("Your name is:", name)

# Get input and convert to integer
symbol_no = int(input("Enter your symbol number: "))
print("Your symbol number is:", symbol_no)

# -------------------------
# 2. String Basics & Concatenation
# -------------------------

# Strings can be defined using '', "", or """ """
# Strings are immutable (cannot be changed after creation)
name = "Bigyan"
number = "1" + "2" + "3"  # Concatenation (not addition)
print("Name:", name)
print("Concatenated number (string):", number)

# -------------------------
# 3. String Slicing
# -------------------------

my_name = "Bigyan Timalsina"

print("Slice [0:6]:", my_name[0:6])           # From index 0 to 5
print("Slice [0:9:3]:", my_name[0:9:3])       # Step slicing
print("Last character (negative index):", my_name[-1]) 
print("Length of my_name:", len(my_name))

# -------------------------
# 4. String Methods
# -------------------------

first_name = "Bigyan !!"

print("\nString Methods:")
print("Uppercase:", first_name.upper())
print("Lowercase:", first_name.lower())
print("Right strip '!':", first_name.rstrip("!"))
print("Replace 'Bigyan' with 'Science':", first_name.replace("Bigyan", "Science"))
print("Split by space:", first_name.split(" "))

last_name = "timalsina,timalsina"
print("Capitalize:", last_name.capitalize())
print("Center (50 width):", first_name.center(50))
print("Count 'timalsina':", last_name.count("timalsina"))
print("Ends with '!!':", first_name.endswith("!!"))

bio = "My name is Bigyan Timalsina"
print("Find 'Bigyan':", bio.find("Bigyan"))

# -------------------------
# 5. String Validation Methods
# -------------------------

print("\nValidation Methods:")
number = "12345"
num = "Bigyan123"

print("Is 'name' all alphabetic?:", name.isalpha())
print("Is 'number' all digits?:", number.isdigit())
print("Is 'num' alphanumeric?:", num.isalnum())
print("Is 'my_name' just spaces?:", my_name.isspace())
print("Swapcase of 'my_name':", my_name.swapcase())
