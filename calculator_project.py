import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def calculator():
    num_0 = float(input("Enter first number: \n"))
    for symbol in operations_dict:
        print(symbol)

    cont_flag = True
    while cont_flag:
        op_symbol = input("Pick an operation: ")
        num_1 = float(input("Enter second number: \n"))
        calc_function = operations_dict[op_symbol]
        result = calc_function(num_0, num_1)
        print(f"{num_0} {op_symbol} {num_1} = {result}")

        continue_ = input(
            "Enter 'Y' to continue with previous output or 'n' start a new calculation or 'x' to exit").lower()
        if continue_ == 'y':
            num_0 = result
        elif continue_ == 'n':
            cont_flag = False
            clear()
            calculator()
        else:
            cont_flag = False
            print("Goodbye!")


calculator()
