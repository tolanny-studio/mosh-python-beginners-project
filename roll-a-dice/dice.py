import random


class DiceGame:
    """A simple dice game that allows the user to roll two dice repeatedly."""

    def validate_input(self, prompt):
        """Prompt the user for a yes/no response and return it as a boolean."""
        while True:
            _roll = input(prompt).strip().lower()

            # Ensure the user enters either 'y' or 'n'.
            if _roll not in ("y", "n"):
                print("\nInvalid input⛔ Input should be y or n")
                continue

            return _roll == "y"

    def ask_to_roll(self):
        """Ask the user whether they want to roll the dice."""
        return self.validate_input("\nRoll the dice? (y/n): ")

    def replay_game(self):
        """Ask the user whether they want to play another round."""
        return self.validate_input("\nDo you wish to replay? (y/n): ")

    def show_dice(self, die1, die2):
        """Display the values rolled by the two dice."""
        print(f"\n{die1}, {die2}")

    def play_game(self):
        """Run the main game loop until the user chooses to quit."""
        while True:
            # End the game if the player chooses not to roll.
            if not self.ask_to_roll():
                break

            # Roll two six-sided dice.
            random_number_1 = random.randint(1, 6)
            random_number_2 = random.randint(1, 6)

            # Display the result of the roll.
            self.show_dice(random_number_1, random_number_2)

            # Ask whether the player wants another round.
            if not self.replay_game():
                break
