# Day 04 – Functions

# 🧠 Function: A block of reusable code that runs only when it is called.
# Syntax:
# def function_name(parameters):
#     """Optional docstring"""
#     # code block
#     return value (optional)

# ✅ Void Function: A function that does not return any value.
def greet():
    print("Good morning!")

greet()  # Function call


# ✅ Built-in Functions: Functions provided by Python
# Examples: print(), len(), type(), input()
print(len("Bigyan"))   # Outputs: 6
print(type(5))         # Outputs: <class 'int'>


# ✅ User-defined Function: Function created by user
def greet_user(name):
    print("Hello", name + "!")

greet_user("Bigyan")


# Another Example:
def average():
    print("The average is:", (a + b) / 2)

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
average()

# ✅Lambda Functions (Anonymous Functions):Short, unnamed functions usually used for simple operations.

# Syntax: lambda arguments: expression
#For Example:
square = lambda x: x * x
print(square(6))  # Output: 36

add = lambda a, b: a + b
print(add(4, 7))  # Output: 11


# ✅ Function Arguments

# 1️⃣ Default Arguments
# If no value is passed, default is used
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # Output: Hello, Guest!
greet("Bigyan")   # Output: Hello, Bigyan!


# 2️⃣ Multiple Parameters with Default Arguments
def user_info(name, country="Nepal"):
    print(f"{name} is from {country}")

user_info("Bigyan")          # Output: Bigyan is from Nepal
user_info("Ajex", "USA")     # Output: Ajex is from USA


# 3️⃣ Keyword Arguments
# Order doesn't matter when using keyword arguments
def student_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student_info(age=20, name="Bigyan")  # Output: Name: Bigyan, Age: 20

# 4️⃣ Variable-length Arguments (*args)
# Used when we're not sure how many arguments will be passed to your function.
# It collects multiple positional arguments into a tuple.
#Syntax
#def function_name(*args):
    # for value in args:
    #     print(value)
#For Example:
def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Total:", total)

add_numbers(1, 2, 3)            # Total: 6
add_numbers(10, 20, 30, 40)     # Total: 100


# 5️⃣ Keyword Variable-length Arguments (**kwargs)
# Used to handle unknown number of keyword arguments.
# It collects them into a dictionary.

# Syntax
# def function_name(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# For Example:
def print_info(**info):
    for key, value in info.items():   #.items() → loop over key-value pairs (most common with kwargs)
        print(f"{key}: {value}")

print_info(name="Bigyan", age=20, country="Nepal")


