size = input("Enter size of pizaa [S/M/L]: ")
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print("Small pizza price is 100")
elif size == 'M' or size == 'm':
    bill += 200
    print("Medium pizza size is 200")
else:
    bill += 300
    print("Large pizza price is 300")

add_pepe = input("Do you want peppperoni (Y/N): ")
if add_pepe == 'Y' or add_pepe == 'y':
    if size == 'S' or size == 's':
        bill += 30
    else:
        bill += 50

extra_cheese = input("Do you want extra cheese? (Y/N)")
if extra_cheese == 'Y' or add_pepe == 'y':
    bill += 20

print(f"Your final bill is {bill}")
