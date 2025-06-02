# ===============================
# 🔁 LOOPS IN PYTHON
# ===============================

# -----------------------------------------------
# 🔹 FOR LOOP – Used when the number of iterations is known(When we know where to stop the loop)
# Syntax: for variable in sequence:
#         code block
# -----------------------------------------------

# Loop using range(start, end, step)
print("📌 For loop with range(1, 6):")
for i in range(1, 6): 
    print(i)

print("\n📌 Loop through a string:")
for char in "Bigyan":
    print(char)


# -----------------------------------------------
# 🔹 WHILE LOOP – Used when the number of iterations is unknown (When we don't know where to stop the loop)
# Syntax: while condition:
#        code block
# -----------------------------------------------

print("\n📌 While loop with a condition:")
age = int(input("Enter your age: "))

while age > 13 and age < 19:
    print("You are a Teenager")
    break  # added to avoid infinite loop


# -----------------------------------------------
# 🔹 Validating input with while loop
# -----------------------------------------------

print("\n📌 Keep asking until user enters a positive number:")
while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        break
    else:
        print("Try again.")


# -----------------------------------------------
# 🔹 Loop Control Statements
# - break: exits the loop
# - continue: skips to next iteration
# - pass: does nothing (placeholder)
# -----------------------------------------------

print("\n📌 Password check example using while loop:")
password = ""
while password != "Code123":
    password = input("Enter the password: ")
print("✅ Access granted!")


# -----------------------------------------------
# 🔹 NESTED LOOPS – A loop inside another loop
# -----------------------------------------------

print("\n📌 Nested for loops example:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
