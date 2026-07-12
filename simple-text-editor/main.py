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
