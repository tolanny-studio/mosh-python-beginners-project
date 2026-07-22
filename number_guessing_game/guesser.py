import random


class GuessNumber:
    def __init__(self):
        self.__highest_number = 100
        self.__lowest_number = 1
        self.__random_number = random.randint(
            self.__lowest_number, self.__highest_number
        )

    def get_number(self):
        return int(input("Guess a number between 1 and 100: "))

    def guess_number(self):
        while True:
            try:
                guess = self.get_number()

            except ValueError:
                print("Please enter a valid number!")
                continue

            if guess > 100 or guess < 0:
                print("Number is negative!!! Retry")
                continue
            elif guess == self.__random_number:
                print("You guessed right!")
                break
            elif guess > self.__random_number:
                print("Too high")
            else:
                print("Too low")
