import random
user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice. You lose")
else:
    computer_choice = random.randint(0, 2)
    print(computer_choice)

    if computer_choice == user_choice:
        print("Its a draw")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")

