from guesser import GuessNumber
from termcolor import cprint


def main():
    """Run the Number Guessing Game."""

    # Create a new game instance.
    game = GuessNumber()

    # Display the welcome message and current record.
    cprint("\nWELCOME TO NUMBER GUESSING GAME 🔢 ", "light_green", attrs=["bold"])
    cprint(
        f"\nLowest Attempt : {game.lowest_attempts()} ",
        "green",
        "on_light_green",
    )

    # Start the game loop.
    game.play()


if __name__ == "__main__":
    main()