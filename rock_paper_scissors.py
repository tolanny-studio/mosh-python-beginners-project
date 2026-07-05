import random

# Game rules:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock


def game_continues():
    """Prompt the player to decide whether to play another round."""
    while True:
        continue_game = input("Do you wish to continue (y/n): ").lower()

        # Keep prompting until a valid response is entered.
        if continue_game not in ("yes", "y", "no", "n"):
            print("Invalid input")
            continue

        # Return True to continue, False to quit.
        return continue_game in ("yes", "y")


# Map shorthand inputs to their full names.
choices = {
    "r": "rock",
    "p": "paper",
    "s": "scissors",
}

# Define which choice defeats which.
# Example: wins["r"] == "s" means Rock beats Scissors.
wins = {
    "r": "s",
    "s": "p",
    "p": "r",
}


def display_choices(choice, computer_choice):
    """Display the player's and computer's choices."""
    print(f"You chose {choices[choice]}")
    print(f"The computer chose {choices[computer_choice]}")


# Main game loop.
while True:

    # Randomly select the computer's choice.
    computer_choice = random.choice(tuple(choices))

    # Get the player's choice.
    choice = input("Rock, paper, or scissors? (r/p/s): ").lower()

    # Reject invalid input and restart the round.
    if choice not in choices:
        print("Invalid input")
        continue

    # Determine the outcome of the round.
    if choice == computer_choice:
        print(f"You both chose {choices[choice]}. It's a tie")

    elif wins[choice] == computer_choice:
        display_choices(choice, computer_choice)
        print("You won!")

    else:
        display_choices(choice, computer_choice)
        print("The computer won!")

    # Ask whether the player wants another round.
    if not game_continues():
        break