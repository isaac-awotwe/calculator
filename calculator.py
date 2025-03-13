# Define function for the arithmetic operations - add, subtract, multipky, and divide

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

# add these four functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

print(operations["*"](4, 8))