import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while(True):
    user_input = input("Select Rock/Paper/Scissors or Q to quit: ").lower()

    # if input is q break out of loop
    if user_input == "q":
        break

    # if input is not rock paper or scissors restart iteration
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)

    computer_input = options[random_number]
    print("Computer picked: " + computer_input)

    if user_input == options[0] and computer_input == options[2]:
        print("You win!")
        user_wins += 1

    elif user_input == options[1] and computer_input == options[0]:
        print("You win!")
        user_wins += 1
    
    elif user_input == options[2] and computer_input == options[1]:
        print("You win!")
        user_wins += 1

    elif user_input == computer_input:
        print("Tie!")
    
    else:
        print("Computer wins!")
        computer_wins += 1

print("User: " + str(user_wins) + "      Computer: " + str(computer_wins))