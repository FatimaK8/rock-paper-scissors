# Rock Paper Scissors Game
# Copilot Prompt: Create a simple Rock Paper Scissors game using Pygame. Make it interactive with buttons for each choice and display the result of each round.

# Rock Paper Scissors Game
# Copilot Prompt:
# Create a simple Rock Paper Scissors game in Python.
# The game should:
# - Ask the user to type their choice (Rock, Paper, or Scissors) in the terminal.
# - The computer randomly selects its move.
# - Display both choices and the result (win, lose, or tie).
# - Repeat until the user types 'quit'.
#
# As a web version, see #file:1_web_recap.html for an HTML/JS implementation.


import random

choices = ["Rock", "Paper", "Scissors"]

import random

choices = ["Rock", "Paper", "Scissors"]

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "You lose!"

print("Welcome to Rock Paper Scissors!")
print("Type Rock, Paper, or Scissors to play. Type 'quit' to exit.")

while True:
    user_choice = input("Your choice: ").capitalize()
    if user_choice == 'Quit':
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    print(get_winner(user_choice, computer_choice))
