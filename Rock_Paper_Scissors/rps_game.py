# Welcome to the Rock-Paper-Scissor game

import random

def getFullName(choice):
    if choice == "r":
        return "rock"
    elif choice == "s":
        return "scissor"
    else:
        return "paper"

print("Hello, welcome to Rock Paper Scissor Game!")
print("You will be prompted to chose rock, paper, or scissors. You can either type the choice, or insert first character.")

legal_choices = ["r", "p", "s"]
playing = True
score_pc = 0
score_player = 0

while playing:
    player = input("What will you chose? Rock (r), paper (p), or scissor (s)?\n")

    while player[0].lower() not in legal_choices:
        player = input("Please enter a valid choice: ")

    computer = legal_choices[random.randint(0, 2)]
    player_full = getFullName(player[0].lower())
    computer_full = getFullName(computer[0].lower())

    if player[0].lower() == "r" and computer == "p":
        print(f"You chose {player_full}, computer chose {computer_full}. Computer wins!")
        score_pc += 1
    elif player[0].lower() == "r" and computer == "s":
        print(f"You chose {player_full}, computer chose {computer_full}. Player wins!")
        score_player += 1
    elif player[0].lower() == "p" and computer == "r":
        print(f"You chose {player_full}, computer chose {computer_full}. Player wins!")
        score_player += 1
    elif player[0].lower() == "p" and computer == "s":
        print(f"You chose {player_full}, computer chose {computer_full}. Computer wins!")
        score_pc += 1
    elif player[0].lower() == "s" and computer == "p":
        print(f"You chose {player_full}, computer chose {computer_full}. Player wins!")
        score_player += 1
    elif player[0].lower() == "s" and computer == "r":
        print(f"You chose {player_full}, computer chose {computer_full}. Computer wins!")
        score_pc += 1
    else:
        print(f"You chose {player_full}, computer chose {computer_full}. It's a tie!")
    
    print(f"The score is:\nPlayer: {score_player}\nComputer: {score_pc}")
    new_game = input("If you want to continue playing, press 'Y'\n")

    if new_game.lower() != "y":
        playing = False

print("Thank you for playing the game!")