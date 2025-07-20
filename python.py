import sys

# Functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Ensure the correct number of arguments are passed
if len(sys.argv) != 4:
    print("Usage: python python.py <operation> <num1> <num2>")
    sys.exit(1)

# Read command-line arguments
try:
    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])
except ValueError:
    print("Error: num1 and num2 must be numbers.")
    sys.exit(1)

# Perform the operation based on the string value of `operation`
if operation == '1':  # Add
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == '2':  # Subtract
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == '3':  # Multiply
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == '4':  # Divide
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid operation selected. Please choose 1, 2, 3, or 4.")
