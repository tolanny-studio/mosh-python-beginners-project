import random


class DiceGame:
    
    def validate_input(self, prompt):
        """Validate a yes/no prompt and return a boolean result."""
        while True:
            _roll = input(prompt).strip().lower()
            if _roll not in ("y", "n"):
                print("\nInvalid input⛔ Input should be y or n")
                continue
            if _roll == "n":
                return False
            return _roll == "y"

    def ask_to_roll(self):
        return self.validate_input("\nRoll the dice? (y/n): ")

    def replay_game(self):
        return self.validate_input("\nDo you wish to replay? (y/n): ")

    def show_dice(self, die1, die2):
        print(f"\n{die1},{die2}")

    def play_game(self):
        while True:
            if not self.ask_to_roll():
                break
            random_number_1 = random.randint(1, 6)
            random_number_2 = random.randint(1, 6)
            self.show_dice(random_number_1, random_number_2)
            if not self.replay_game():
                break
