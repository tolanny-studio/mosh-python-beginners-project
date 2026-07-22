from guesser import GuessNumber
from termcolor import cprint

def main():

    game = GuessNumber()
    cprint("\nWELCOME TO NUMBER GUESSING GAME 🔢 ","light_green",attrs=["bold"])
    cprint(f"\nLowest Attempt : {game.lowest_attempts()} ","green","on_light_green")
    game.play()


if __name__ == "__main__":
    main()
