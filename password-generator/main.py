import string
import random


def password_generator(
    password_length, include_upper_case, include_special_character, include_number
):
    password = ""
    if include_upper_case:
        password += random.choice(string.ascii_uppercase)
    if include_special_character:
        password += random.choice(string.punctuation)
    if include_number:
        password += random.choice(string.digits)

    characters = string.ascii_lowercase

    if include_upper_case:
        characters += string.ascii_uppercase
    if include_special_character:
        characters += string.punctuation
    if include_number:
        characters += string.digits

    for _ in range(password_length - len(password)):
        password += random.choice(characters)

    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    return password


def validate_password_length(prompt):
    while True:
        try:
            password_length = int(input(prompt))
        except ValueError:
            print("Invalid input⛔. Enter an integer")
        return password_length
        


def main():
    password_length = validate_password_length("Enter password length: ")
    include_upper_case = (
        input("Do you want to include an uppercase (y/n): ").lower() == "y"
    )
    include_special_character = (
        input("Do you want to include a special character (y/n): ").lower() == "y"
    )
    include_number = input("Do you want to include a number (y/n): ").lower() == "y"
    password = password_generator(
        password_length, include_upper_case, include_special_character, include_number
    )

    print(password)


if __name__ == "__main__":
    main()
