import string
import random
import secrets


def password_generator(
    password_length, include_upper_case, include_special_character, include_number
):
    password = ""
    if include_upper_case:
        password += secrets.choice(string.ascii_uppercase)
    if include_special_character:
        password += secrets.choice(string.punctuation)
    if include_number:
        password += secrets.choice(string.digits)

    characters = string.ascii_lowercase

    if include_upper_case:
        characters += string.ascii_uppercase
    if include_special_character:
        characters += string.punctuation
    if include_number:
        characters += string.digits

    for _ in range(password_length - len(password)):
        password += secrets.choice(characters)

    password = list(password)
    random.SystemRandom().shuffle(password)
    password = "".join(password)
    return password


def validate_password_length(prompt):
    while True:
        try:
            password_length = int(input(f"\n{prompt}"))
            if password_length < 5:
                print("\nInvalid Input ⛔ Password should be more than four digit")
                continue
            return password_length
        except ValueError:
            print("\nInvalid input ⛔ Enter an integer")


def validate_include_choice(prompt):
    while True:
        include_option = input(f"\n{prompt}").lower()
        if include_option not in ("y", "n"):
            print("\nInvalid answer ⛔ Enter y/n ")
            continue
        return include_option == "y"


def main():
    password_length = validate_password_length("Enter password length: ")
    include_upper_case = validate_include_choice(
        "Do you want to include an uppercase (y/n): "
    )
    include_special_character = validate_include_choice(
        "Do you want to include a special character (y/n): "
    )
    include_number = validate_include_choice("Do you want to include a number (y/n): ")
    password = password_generator(
        password_length, include_upper_case, include_special_character, include_number
    )

    print(password)


if __name__ == "__main__":
    main()
