import time
import random
while True:
    your_turn = input("Enter a choice (rock, paper, scissors):")
    rps_choices = [ "rock" , "paper" ,"scissors"]
    computer_choice = random.choice(rps_choices)
    print("rock")
    time.sleep(2)
    print("paper")
    time.sleep(2)
    print("scissors")
    time.sleep(2)
    print("SHOOT!")
    print(f"\n You chose {your_turn}, Bot chose {computer_choice}.\n")

    if your_turn == computer_choice:
        print("Both chose the same! {computer_choice}. REDO \n")

    elif your_turn == "rock":
        if computer_choice == "paper":
            print("Paper cover rock. You kinda lost...")
            time.sleep(1)
            print("...")
        elif computer_choice == "scissors":
            print("Rock beats Scissors... YOU WON GREAT JOB!")
    elif your_turn == "scissors":
        if computer_choice == "rock":
            print("The rock smashes the scissors. You kinda lost...")
            time.sleep(1)
            print("...")
        elif computer_choice == "paper":
            print("You cut the paper YOU WON!")
    elif your_turn == "paper":
        if computer_choice == "scissors":
            print("Scissors cuts the rock. You kinda lost...")
            time.sleep(1)
            print("...")
        elif computer_choice == "rock":
            print("Paper cover rock. YOU WON GREAT JOB!")

    print("Thanks for playing rock paper scissors with BOT")