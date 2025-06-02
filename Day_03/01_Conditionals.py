# Day_03_Conditionals.py
# Python Conditionals Examples: if-else, elif, and match-case (Python 3.10+)

# Conditional Operators:
# < , > , <= , >= , == , != 

# Example 1: Voting Eligibility Check
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("\n" + "#"*40 + "\n")

# Example 2: Buying a Range Rover based on your budget
range_rover_price = 107900
money = int(input("How much money do you have? "))

if money > range_rover_price:
    print("Buy Range Rover")
elif money == range_rover_price:
    print("Buy with proper budgeting")
else:
    print("Buy by doing financing")

print("\n" + "#"*40 + "\n")

# Example 3: Using match-case 
roll_no = int(input("Enter your roll number: "))

match roll_no:
    case 1:
        print("Your roll number is 1")
    case 2:
        print("Your roll number is 2")
    case _:
        print("Your roll number is", roll_no)
