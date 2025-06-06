# Day 07 – DocString & PEP 8

# --------------------
# 📃 DocString
# --------------------
# A docstring is a string that appears right after the definition of a function, method, class, or module.
# It is used to document what the function/class/module does.

# For Example:
def cube(n):
    '''Take the cube of number n, returns the cube of n.'''
    print(n**3)

cube(5)

# Accessing the docstring of the function
print(cube.__doc__)


# --------------------
# 📃 PEP 8
# --------------------
# PEP 8 stands for Python Enhancement Proposal 8.
# It provides guidelines and best practices on how to write Python code.
# Helps make code more readable, consistent, and easier to maintain.

# Naming conventions, spacing, line length, and structure are part of PEP 8.

# For Example:
def get_price_with_tax(price, tax_rate_percent):
    """Return the final price after applying tax rate in percent."""
    tax_rate = tax_rate_percent / 100
    final_price = price + (price * tax_rate)
    return round(final_price, 2)

print(get_price_with_tax(2000, 5))  # Output: 2100.0
