def func(a, b):
    c = a + b
    # print func is called to output c to standard output stream
    print(c)


# the print value cannot be used further


# the function is called for execution and arguments passed
func(3, 5)


# function with return statement
def func(a, b):
    c = a + b
    # the keyword gives the function output, which is the value in c
    return c


# the return value can be used further

# the function is called and output collected in a variable
output = func(3, 5)
# the collected output is printed to standard output stream 1
print(output)
