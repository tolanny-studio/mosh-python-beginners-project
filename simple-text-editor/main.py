BREAK_WORD = "SAVE"


def get_input():
    words = []
    print()
    print("Enter your text.\nType SAVE on a new line to finish.")
    print()
    while True:
        word = input().strip()
        if word == BREAK_WORD:
            break
        words.append(word + "\n")
    return words


def write_file():
    file_name = input("Enter file name to open or create: ").strip()
    try:
        with open(file_name, "w") as file:
            file.writelines(get_input())
    except OSError:
        print(f"{file_name} not present")