
# print all odd values between 1 and 20
for i in range(21):
    # for every iteration, the i variable holds a number from 0...
    if i % 2 != 0:
        # checks if the number when divided by two has no remainder
        # checks for even numbers
        # prints every even number between o and 20
        print("i = ", i)

# taking input from user and storing in a variable
this_f = input("Enter float number: ")
# typecasting the value stored in the variable to float
this_f = float(this_f)
# printing the typecasting value using string.format
# 3.f specifies the precision/decimal places, format() accepts the variable as an argument
print("Float rounded: {:.3f}".format(this_f))
