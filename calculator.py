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

# print(operations["*"](4, 8))

def print_operations():
    for key in operations:
        print(key)


continue_calculator = True
continue_with_result = 'n'

while continue_calculator == True:
    first_number = float(input("What's the first number?:  "))
    print_operations()
    operation = input("Pick an operation:"  )
    next_number = float(input("What's the next number?:  "))
    result = operations[operation](first_number,next_number)
    print(f"{first_number} {operation} {next_number} =  {result}")
    continue_with_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ").lower()
    if continue_with_result == "n":
        print("\n" * 100)
    while continue_with_result == 'y':
        first_number = result
        print_operations()
        operation = input("Pick an operation:"  )
        next_number = float(input("What's the next number?:  "))
        result = operations[operation](first_number,next_number)
        print(f"{first_number} {operation} {next_number} =  {result}")
        continue_with_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ").lower()
        if continue_with_result == "n":
            print("\n"*100)

