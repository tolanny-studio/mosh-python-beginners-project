import os

from termcolor import cprint, colored

BREAK_WORD = "SAVE"
DIVIDER = "-" * 50


def should_save(word):
    return word.upper() == BREAK_WORD


def get_input():
    words = []
    print()
    print("Enter your text.\nType SAVE on a new line to finish.")
    print()
    while True:
        word = input().strip()
        if should_save(word):
            break
        words.append(word + "\n")
    return words


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read()
    except OSError as e:
        print(f"Error : {e}")


def edit_file():
    file_name = input("Enter file name to open or create: ").strip()
    try:
        if os.path.exists(file_name):
            print(DIVIDER)
            cprint(read_file(file_name), "red")
            print(DIVIDER)
        with open(file_name, "a") as file:
            file.writelines(get_input())
        print(DIVIDER)
        cprint(read_file(file_name), "green")
        print(DIVIDER)
    except OSError as e:
        print(f"Error : {e}")


def main():
    edit_file()


if __name__ == "__main__":
    main()
