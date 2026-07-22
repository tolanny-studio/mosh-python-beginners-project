import random
import logging
from pathlib import Path
from termcolor import cprint

LOWEST_ATTEMPT_FILE = Path(__file__).parent / "lowest-attempt.txt"

logger = logging.getLogger(__name__)


class GuessNumber:
    def __init__(self):
        self.__highest_number = 100
        self.__lowest_number = 1
        self.__random_number = random.randint(
            self.__lowest_number, self.__highest_number
        )
        self.__attempt = 0
        self.__lowest_attempt = self.get_lowest_attempt()

    def get_lowest_attempt(self):
        try:
            lowest_attempt = int(LOWEST_ATTEMPT_FILE.read_text())
        except FileNotFoundError:
            logger.warning("File does not exist")
            LOWEST_ATTEMPT_FILE.write_text("0")
            return 0
        except ValueError as e:
            logger.error("Invalid number %s", e)
            return 0
        except:
            logger.error("Invalid number")
            return 0
        else:
            return lowest_attempt

    def get_number(self):
        return int(input("\nGuess a number between 1 and 100: "))

    def lowest_attempts(self):
        return self.__lowest_attempt

    def update_attempt(self):
        self.__attempt += 1

    def print_attempts(self):
        cprint(
            f"\nAttempt(s): {self.__attempt} || Lowest Attempt(s): {self.lowest_attempts()}",
            "green",
            "on_light_green",
        )

    def reset_game(self):
        self.__attempt = 0
        self.__highest_number = 100
        self.__lowest_number = 1
        self.__random_number = random.randint(
            self.__lowest_number, self.__highest_number
        )

    def retry_game(self):
        while True:
            retry = input("\nDo you wish to retry ?").lower()
            if retry not in ("y", "n"):
                cprint("Invalid Input ⛔ Enter y or n")
                continue
            self.reset_game()
            return retry == "y"

    def play(self):
        while True:
            while True:
                try:
                    guess = self.get_number()
                except ValueError:
                    print("\nPlease enter a valid number!")
                    continue

                if guess > self.__highest_number or guess < self.__lowest_number:
                    cprint(
                        f"\nWrong number ⛔ Please enter a number between {self.__lowest_number} and {self.__highest_number}!",
                        attrs=["italic"],
                    )
                    continue
                elif guess == self.__random_number:
                    print("\nYou guessed right!")
                    self.update_attempt()
                    if self.__attempt < self.__lowest_attempt:
                        self.__lowest_attempt = self.__attempt
                        LOWEST_ATTEMPT_FILE.write_text(str(self.__lowest_attempt))
                        print(f"🎉 New Record!Lowest attempts: {self.__lowest_attempt}")
                    self.print_attempts()
                    break
                elif guess > self.__random_number:
                    self.update_attempt()
                    self.print_attempts()
                    cprint("\nToo high ⚡")

                else:
                    self.update_attempt()
                    self.print_attempts()
                    cprint("\nToo low ⬇️ ")

            if not self.retry_game():
                break
