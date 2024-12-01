# This is a simple "Rock, Paper, Scissors" game implemented in Python.
# The player competes against the computer, which chooses randomly between "rock", "paper", or "scissors".
# The winner is determined based on the classic rules:
# - Rock beats Scissors
# - Paper beats Rock
# - Scissors beats Paper
# If both the player and the computer choose the same, it's a tie.

import random  # Import the random library to make the computer's choice random

# Function to define the game
def play():
    # Game options (Rock, Paper, Scissors)
    options = ['rock', 'paper', 'scissors']

    # Player's input
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    # Check if the player's input is valid
    if player_choice not in options:
        print("Invalid option. Please choose 'rock', 'paper', or 'scissors'.")
        return
    
    # Computer's random choice
    computer_choice = random.choice(options)
    print(f"The computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
        (player_choice == 'paper' and computer_choice == 'rock') or \
        (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")

# Run the game
play()
