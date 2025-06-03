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


