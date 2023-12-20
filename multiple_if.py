height = int(input("Enter your height in feet"))
bill = 0
if height >= 3:
    print("You're eligible")
    age = int(input("Enter your age"))
    if age < 10:
        bill = 100
        print("Ticket is Ksh. 100")
    elif age <= 18:
        bill = 200
        print("Ticket is Ksh. 200")
    else:
        bill = 300
        print("Ticket is Ksh. 300")

    want_photo = input("Do you want to take photo (Y/N)")
    if want_photo == 'y' or want_photo == 'Y':
        bill = bill + 50

    print(f"Your total bill is {bill}.")

else:
    print("You can't board")
print("Goodbye!")
