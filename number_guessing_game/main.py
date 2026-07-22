from guesser import GuessNumber


def main():

    game = GuessNumber()
    print("\nWelcome to number guessing game 🔢 ")
    print(f"\nLowest Attempt : {game.lowest_attempts()}")
    game.play()


if __name__ == "__main__":
    main()
