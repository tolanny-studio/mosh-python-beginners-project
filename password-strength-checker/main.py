import re

# Maps the calculated password strength score to a descriptive rating.
STRENGTH_DICT = {
    0: "Very Weak",
    1: "Weak",
    2: "Medium",
    3: "Strong",
    4: "Very Strong",
    5: "Excellent",
}


def password_strength(password):
    """Calculate the strength score of a password.

    A password earns one point for each of the following criteria:
    - Has at least 8 characters.
    - Contains at least one digit.
    - Contains at least one lowercase letter.
    - Contains at least one uppercase letter.
    - Contains at least one special character.

    Args:
        password (str): The password to evaluate.

    Returns:
        int: The password strength score ranging from 0 to 5.
    """
    strength = 0

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
    """Prompt the user for a password and display its strength rating."""
    password = input("Enter a password: ")
    strength = password_strength(password)

    print(STRENGTH_DICT[strength])


if __name__ == "__main__":
    main()