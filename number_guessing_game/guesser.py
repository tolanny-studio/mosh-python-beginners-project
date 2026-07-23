import logging
import random
from pathlib import Path

from termcolor import cprint

# File used to persist the lowest number of attempts.
LOWEST_ATTEMPT_FILE = Path(__file__).parent / "lowest-attempt.txt"

logger = logging.getLogger(__name__)


class GuessNumber:
    """A number guessing game that tracks the player's best score."""

    def __init__(self):
        """Initialize the game settings and load the lowest attempt record."""

        self.__highest_number = 100
        self.__lowest_number = 1
        self.__random_number = random.randint(
            self.__lowest_number,
            self.__highest_number,
        )
        self.__attempt = 0
        self.__lowest_attempt = self.get_lowest_attempt()

    def get_lowest_attempt(self):
        """
        Read the lowest attempt record from the save file.

        Returns:
            int: The saved lowest attempt, or 0 if the file does not exist
            or contains invalid data.
        """
        try:
            lowest_attempt = int(LOWEST_ATTEMPT_FILE.read_text())

        except FileNotFoundError:
            logger.warning("Lowest attempt file does not exist.")
            LOWEST_ATTEMPT_FILE.write_text("0")
            return 0

        except ValueError as e:
            logger.error("Invalid value in lowest attempt file: %s", e)
            return 0

        except Exception as e:
            logger.exception("Unexpected error while reading file: %s", e)
            return 0

        return lowest_attempt

    def get_number(self):
        """
        Prompt the player to enter a guess.

        Returns:
            int: The player's guessed number.
        """
        return int(input("\nGuess a number between 1 and 100: "))

    def lowest_attempts(self):
        """
        Return the current record.

        Returns:
            int: Lowest number of attempts needed to win.
        """
        return self.__lowest_attempt

    def update_attempt(self):
        """Increment the player's attempt counter by one."""
        self.__attempt += 1

    def print_attempts(self):
        """Display the current attempt count and the lowest recorded attempt."""
        cprint(
            f"\nAttempt(s): {self.__attempt} || "
            f"Lowest Attempt(s): {self.lowest_attempts()}",
            "green",
            "on_light_green",
        )

    def reset_game(self):
        """Reset the game state for a new round."""

        self.__attempt = 0
        self.__highest_number = 100
        self.__lowest_number = 1
        self.__random_number = random.randint(
            self.__lowest_number,
            self.__highest_number,
        )

    def retry_game(self):
        """
        Ask the player if they want to play another round.

        Returns:
            bool: True if the player wants to continue, otherwise False.
        """
        while True:
            retry = input("\nDo you wish to retry? (y/n): ").lower()

            if retry not in ("y", "n"):
                cprint("Invalid Input ⛔ Enter y or n")
                continue

            if retry == "y":
                self.reset_game()
                return True

            return False

    def play(self):
        """Run the main game loop."""

        while True:
            while True:
                try:
                    guess = self.get_number()

                except ValueError:
                    print("\nPlease enter a valid number!")
                    continue

                # Validate the player's input.
                if (
                    guess > self.__highest_number
                    or guess < self.__lowest_number
                ):
                    cprint(
                        f"\nWrong number ⛔ Please enter a number "
                        f"between {self.__lowest_number} "
                        f"and {self.__highest_number}!",
                        attrs=["italic"],
                    )
                    continue

                # Player guessed correctly.
                if guess == self.__random_number:
                    print("\nYou guessed right!")

                    self.update_attempt()

                    # Update the record if the player achieved a new best score.
                    if (
                        self.__lowest_attempt == 0
                        or self.__attempt < self.__lowest_attempt
                    ):
                        self.__lowest_attempt = self.__attempt
                        LOWEST_ATTEMPT_FILE.write_text(
                            str(self.__lowest_attempt)
                        )
                        print(
                            f"🎉 New Record! "
                            f"Lowest attempts: {self.__lowest_attempt}"
                        )

                    self.print_attempts()
                    break

                # Hint the player whether the guess was too high or too low.
                self.update_attempt()
                self.print_attempts()

                if guess > self.__random_number:
                    cprint("\nToo high ⚡")
                else:
                    cprint("\nToo low ⬇️ ")

            # Exit the game if the player chooses not to continue.
            if not self.retry_game():
                break