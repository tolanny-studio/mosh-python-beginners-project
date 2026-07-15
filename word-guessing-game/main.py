import random


def get_word_list():
    word_list = []
    with open("word.txt", "r") as file:
        for line in file:
            word_list.append(line.strip())
    return word_list


def select_random_word():
    return random.choice(get_word_list())


def get_guess_letter():
    return input("Enter a letter🔤: ").lower()


def retry_game():
    while True:
        retry = input("Do you want to retry 🔄️: ").lower()
        if retry not in ("y", "n"):
            print("Invalid input")
            continue
        return retry == "y"


def main():
    lives = 6
    random_word = select_random_word()
    blanks = ""
    for _ in random_word:
        blanks += "_"
    # print(blanks)
    list_blanks = list(blanks)
    while True:
        guess = get_guess_letter()
        for index, char in enumerate(random_word):
            if char == guess:
                print("Good guess. Keep it up")
                list_blanks[index] = guess

        print(random_word)
        blanks = "".join(list_blanks)
        print(blanks)
        lives -= 1

        if lives == 0:
            print("Game Over ⛔")
            break
        if "_" not in blanks:
            print("Kudos 👊 You made it.")
            break
    if retry_game():
      main()
      lives = 6


if __name__ == "__main__":
    main()
