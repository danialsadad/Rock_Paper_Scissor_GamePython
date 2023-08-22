import time
import random
choice_list = ["r", "p", "s"]

def game():
    won = False
    lost = False
    while not won and not lost:
        you = input("Enter your choice from Rock, Paper or Scissors: ")
        you_i = you.lower()
        com_1 = random.choice(choice_list)
        com_choice = com_1.lower()
        if com_choice ==  you_i:
            print("Draw, try again!")
        elif com_choice == "r" and  you_i == "p":
            won = True
        elif com_choice == "r" and  you_i == "s":
            lost = True
        elif com_choice == "p" and  you_i == "r":
            lost = True
        elif com_choice == "p" and  you_i == "s":
            won = True
        elif com_choice == "s" and  you_i == "r":
            won = True
        elif com_choice == "s" and  you_i == "p":
            lost = True
        elif you != "s" or "p" or "r":
            print("Invalid choice, try again...")
    if won:
        print("Congrats you won, the PC chose " + com_1 + "!")
        won = False
    if lost:
        print("You lost, the PC chose " + com_1 + "!")
        lost = False

play_again = "y"
while play_again.lower() == "y":
    game()
    play_again = input("Would u like to play again? ")
if play_again.lower() != "y":
    print("Goodbye!")
    time.sleep(3)

