import random
import string


def get_word_list():
    word_list = []
    with open("word.txt", "r") as file:
        for line in file:
            word_list.append(line.strip())
    return word_list


WORD_LIST = get_word_list()


def select_random_word():
    return random.choice(WORD_LIST)


def get_guess_letter(blanks):
    while True:
        guess = input("\nEnter a letter🔤: ").lower()
        if len(guess) != 1:
            print("\nEnter a single letter")
            print(blanks)
            continue
        if guess not in string.ascii_lowercase:
            print("\nEnter an alphabet only")
            print(blanks)
            continue
        return guess


def retry_game():
    while True:
        retry = input("\nDo you wish to retry 🔄️: ").lower()
        if retry not in ("y", "n"):
            print("\nInvalid input ❌")
            continue
        return retry == "y"


def play_game():
    lives = 6
    random_word = select_random_word()
    blanks = "_" * len(random_word)
    print(blanks)
    list_blanks = list(blanks)
    guesses = set()

    while True:
        guess = get_guess_letter(blanks)
        if guess in guesses:
            print(f"Letter {guess} already guessed")
            continue
        if guess in random_word:
            print("Good guess. Keep it up")
            print(f"\nLives: {lives}")
            guesses.add(guess)
            for index, char in enumerate(random_word):
                if char == guess:
                    list_blanks[index] = guess
        else:
            print("\nWrong guess ❌ Retry")
            lives -= 1
            guesses.add(guess)
            print(f"\nLives: {lives}")

        blanks = "".join(list_blanks)
        print(blanks)

        if lives == 0:
            print("\nGame Over ⛔")
            break
        if "_" not in blanks:
            print("\nKudos 👊 You made it.")
            break


def main():
    while True:
        play_game

        if not retry_game():
            print("Thanks for playing")
            break


if __name__ == "__main__":
    main()
