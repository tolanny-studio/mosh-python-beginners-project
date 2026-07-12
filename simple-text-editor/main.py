import os

from termcolor import cprint

# Sentinel value that tells the program the user has finished entering text.
BREAK_WORD = "SAVE"

# Divider used to separate sections of the program output.
DIVIDER = "-" * 50


def should_save(word):
    """Return True if the user entered the save command."""
    return word.upper() == BREAK_WORD


def get_input():
    """Collect lines of text from the user until the save command is entered."""
    words = []

    print()
    print("Enter your text.\nType SAVE on a new line to finish.")
    print()

    while True:
        word = input().strip()

        if should_save(word):
            break

        # Preserve each line by appending a newline character.
        words.append(word + "\n")

    return words


def read_file(file_name):
    """Read and return the contents of a file."""
    try:
        with open(file_name, "r") as file:
            return file.read()
    except OSError as e:
        print(f"Error: {e}")
        return ""


def edit_file():
    """Display an existing file's contents and append new user input to it."""
    file_name = input("Enter file name to open or create: ").strip()

    try:
        # Show the current contents if the file already exists.
        if os.path.exists(file_name):
            print(DIVIDER)
            cprint(read_file(file_name), "red")
            print(DIVIDER)

        # Append the user's input to the file.
        with open(file_name, "a") as file:
            file.writelines(get_input())

        # Display the updated file contents.
        print(DIVIDER)
        cprint(read_file(file_name), "green")
        print(DIVIDER)

    except OSError as e:
        print(f"Error: {e}")


def main():
    """Run the file editor application."""
    edit_file()


if __name__ == "__main__":
    main()