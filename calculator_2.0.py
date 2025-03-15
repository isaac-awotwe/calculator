# import logo from art
from art import logo

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

def print_operations():
    for key in operations:
        print(key)


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    accummulate_result = True
    while accummulate_result:
        print_operations()
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        use_answer = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if use_answer == 'y':
            num1 = answer
        elif use_answer == 'n':
            print("\n" * 100)
            accummulate_result = False
            calculator()
calculator()





