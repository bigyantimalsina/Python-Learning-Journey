# Day 07 – f-string and str.format()

# 📋 String Formatting in Python

# 1️⃣ Using str.format()
# Allows insertion of values into placeholders {} inside a string.
bio = "Hey my name is {} and I am from {}."

# 2️⃣ Input from the user
country = input("Enter your country: ")
name = input("Enter your name: ")

# 3️⃣ Taking float input with formatted output using f-string
price = float(input(f"What's the price of milk in your {country}? "))
print(f"The price of milk in my {country} is {price:.2f}")  # :.2f means 2 decimal places

# 4️⃣ Output using str.format()
print(bio.format(name, country))

# 5️⃣ Output using f-string
print(f"Hey my name is {name} and I am from {country}.")
