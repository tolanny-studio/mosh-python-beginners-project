import re

STRENGTH_DICT = {
    0: "Very Weak",
    1: "Weak",
    2: "Medium",
    3: "Strong",
    4: "Very Strong",
    5: "Efficient",
}


def password_strength(password):

    strength = 0
    if password == "":
        strength += 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password):
        strength += 1

    return strength


def main():
    password = input("Enter a password: ")
    strength = password_strength(password)

    print(STRENGTH_DICT[strength])


if __name__ == "__main__":
    main()
