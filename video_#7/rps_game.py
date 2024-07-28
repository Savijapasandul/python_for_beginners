import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It is a tie."
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "You win."
    else: 
        return "Computer wins."

def play_game():
    player = input("Enter rock, paper, or scissors: ").lower()
    print("You choose: " + player)
    computer = get_computer_choice()
    print(f"Computer chose: {computer}")
    print(determine_winner(player, computer))

play_game()