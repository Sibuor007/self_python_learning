import random
_friends = input("Enter the first names of each person: ")
name_split = _friends.split(" ")
print(name_split)

length = len(name_split)
choice = random.randint(0, length - 1)
pay_bill = name_split[choice]
print(f"{pay_bill} will pay the bill today!")

select = random.choice(name_split)
print(f"{select} will pay the bill.")
