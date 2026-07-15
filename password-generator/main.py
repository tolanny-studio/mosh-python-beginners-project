import string
import random
import secrets

# Secure random number generator used for shuffling passwords.
SYSTEM_RANDOM = random.SystemRandom()


def password_generator(
    password_length, include_upper_case, include_special_character, include_number
):
    """Generate a random password based on the selected requirements.

    The generated password always contains at least one character from each
    selected category (uppercase letters, digits, and special characters).
    The remaining characters are chosen from the combined character pool and
    the final password is shuffled to ensure a random order.

    Args:
        password_length (int): Desired length of the password.
        include_upper_case (bool): Whether to include uppercase letters.
        include_special_character (bool): Whether to include special characters.
        include_number (bool): Whether to include digits.

    Returns:
        str: A randomly generated password.
    """
    password = ""

    # Guarantee at least one character from each selected category.
    if include_upper_case:
        password += secrets.choice(string.ascii_uppercase)

    if include_special_character:
        password += secrets.choice(string.punctuation)

    if include_number:
        password += secrets.choice(string.digits)

    # Build the pool of allowed characters.
    characters = string.ascii_lowercase

    if include_upper_case:
        characters += string.ascii_uppercase

    if include_special_character:
        characters += string.punctuation

    if include_number:
        characters += string.digits

    # Fill the remaining password length.
    for _ in range(password_length - len(password)):
        password += secrets.choice(characters)

    # Shuffle the password so required characters appear in random positions.
    password = list(password)
    SYSTEM_RANDOM.shuffle(password)

    return "".join(password)


def validate_password_length(prompt):
    """Prompt the user until a valid password length is entered.

    The password length must be an integer greater than or equal to 5.

    Args:
        prompt (str): Message displayed to the user.

    Returns:
        int: A valid password length.
    """
    while True:
        try:
            password_length = int(input(f"\n{prompt}"))

            if password_length < 5:
                print("\nInvalid Input ⛔ Password length must be at least 5 characters.")
                continue

            return password_length

        except ValueError:
            print("\nInvalid input ⛔ Enter an integer")


def validate_include_choice(prompt):
    """Prompt the user for a yes/no response.

    Args:
        prompt (str): Message displayed to the user.

    Returns:
        bool: True if the user enters 'y'; otherwise False.
    """
    while True:
        include_option = input(f"\n{prompt}").lower()

        if include_option not in ("y", "n"):
            print("\nInvalid answer ⛔ Enter y/n ")
            continue

        return include_option == "y"


def main():
    """Run the password generator program."""
    password_length = validate_password_length("Enter password length: ")

    include_upper_case = validate_include_choice(
        "Do you want to include an uppercase (y/n): "
    )
    include_special_character = validate_include_choice(
        "Do you want to include a special character (y/n): "
    )
    include_number = validate_include_choice(
        "Do you want to include a number (y/n): "
    )

    password = password_generator(
        password_length,
        include_upper_case,
        include_special_character,
        include_number,
    )

    print(f"\nGenerated password: {password}")


if __name__ == "__main__":
    main()