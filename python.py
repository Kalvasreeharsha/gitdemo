# add_sub_mul_div.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero error"
    return a / b

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {sub(a, b)}")
    print(f"Multiplication: {mul(a, b)}")
    print(f"Division: {div(a, b)}")
