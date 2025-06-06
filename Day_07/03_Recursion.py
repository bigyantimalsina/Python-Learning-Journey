# Day 06 – Recursion

# ✨ Recursion:
# Recursion is when a function calls itself to solve smaller versions of a problem.

# Syntax Template:
# def recursive_function():
#     if base_condition:
#         return result  # Base case
#     else:
#         return recursive_function()  # Recursive case

# ✅ Example 1: Factorial using recursion
def factorial(n):
    if n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive call

print("Factorial of 5:", factorial(5))  # Output: 120


# ✅ Example 2: Fibonacci using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

print("Fibonacci of 5:", fibonacci(5))  # Output: 5
