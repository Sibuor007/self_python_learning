import os
"""
    Module that defines functions that collectively work to create a
    simple calculator
"""

def add(a, b):
    ''' a function that returns addition of two arguments
    '''
    return a + b


def subtract(a, b):
    ''' a function that returns subtraction of two arguments
    '''
    return a - b


def multiply(a, b):
    ''' a function that returns multiply of two arguments
    '''
    return a * b


def divide(a, b):
    ''' a function that returns divide of two arguments
    '''
    return a / b


# a dictionay that containes operators as keys, and description as values
operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def clear():
    ''' a function that clears the screen upon a request for new calculation
    '''
    os.system('clear' if os.name == 'posix' else 'cls')


def calculator():
    ''' a function that takes input from user, selects the operator, and prints the result
    '''
    num_0 = float(input("Enter first number: \n"))
    # a for loop to iterate through the dictionary, prints the to standard output
    for symbol in operations_dict:
        print(symbol)

    # a flag to control the while loop
    cont_flag = True
    # while loop that remains true until cont_flag becomes False
    while cont_flag:
        # input to capture operation selected by user, store in op_symbol
        op_symbol = input("Pick an operation: ")
        # takes second number from user, type casts it to float, and stores in a var
        num_1 = float(input("Enter second number: \n"))
        # uses the operand as they key to obtain dict value and store in calc_function
        calc_function = operations_dict[op_symbol]
        # the fetched value reps the functions, hence a function call
        result = calc_function(num_0, num_1)
        # prints the result of the complete operation
        print(f"{num_0} {op_symbol} {num_1} = {result}")

        # a section to get user feedback: to continue, restart, or exit
        continue_ = input(
            "Enter 'Y' to continue with previous output or 'n' start a new calculation or 'x' to exit").lower()
        # control continues with the same value to the next operation on 'continue'
        if continue_ == 'y':
            num_0 = result
        # the loop breaks on 'n', new calc, the clear() is called, and a recursive call made
        elif continue_ == 'n':
            cont_flag = False
            clear()
            calculator()
        else:
        # on 'x', the loop breaks and prints goobye!
            cont_flag = False
            print("Goodbye!")

# the main function is called to allow the program to execute the code
calculator()
