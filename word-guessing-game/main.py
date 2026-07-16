import random
import string

# Load the word list once when the program starts.
WORD_LIST = []


def get_word_list():
    """Read all words from the word file.

    Returns:
        list[str]: A list of words stripped of trailing whitespace.
    """
    word_list = []

    with open("./word.txt", "r") as file:
        for line in file:
            word_list.append(line.strip())

    return word_list


WORD_LIST = get_word_list()


def select_random_word():
    """Select and return a random word from the word list."""
    return random.choice(WORD_LIST)


def get_guess_letter(blanks):
    """Prompt the user for a valid letter.

    The user must enter a single lowercase alphabetic character.

    Args:
        blanks (str): The current state of the hidden word.

    Returns:
        str: A validated guessed letter.
    """
    while True:
        guess = input("\nEnter a letter 🔤: ").lower()

        if len(guess) != 1:
            print("\nEnter a single letter.")
            print(blanks)
            continue

        if guess not in string.ascii_lowercase:
            print("\nEnter an alphabet only.")
            print(blanks)
            continue

        return guess


def retry_game():
    """Ask the player whether to play another game.

    Returns:
        bool: True if the player chooses to play again, otherwise False.
    """
    while True:
        retry = input("\nDo you wish to retry 🔄️: ").lower()

        if retry not in ("y", "n"):
            print("\nInvalid input ❌")
            continue

        return retry == "y"


def play_game():
    """Run one complete game of Hangman."""
    lives = 6
    random_word = select_random_word()

    # Create the hidden version of the word.
    blanks = "_" * len(random_word)
    print(blanks)

    list_blanks = list(blanks)

    # Store all letters guessed by the player.
    guesses = set()

    while True:
        guess = get_guess_letter(blanks)

        if guess in guesses:
            print(f"Letter '{guess}' already guessed.")
            continue

        guesses.add(guess)

        if guess in random_word:
            print("Good guess. Keep it up!")
            print(f"\nLives: {lives}")

            # Reveal every occurrence of the guessed letter.
            for index, char in enumerate(random_word):
                if char == guess:
                    list_blanks[index] = guess
        else:
            print("\nWrong guess ❌ Retry")
            lives -= 1
            print(f"\nLives: {lives}")

        blanks = "".join(list_blanks)
        print(blanks)

        if "_" not in blanks:
            print("\nKudos 👊 You made it.")
            break

        if lives == 0:
            print("\nGame Over ⛔")
            break


def main():
    """Run the Hangman game until the player chooses to quit."""
    while True:
        play_game()

        if not retry_game():
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()