import random


def generate_four_unique_digit():
    """Generate and return a string of four unique random digits (1–9)."""
    four_unique_digit = ""

    # Keep generating digits until four unique digits have been collected.
    while len(four_unique_digit) < 4:
        digit = str(random.randint(1, 9))

        # Add the digit only if it has not already been generated.
        if digit not in four_unique_digit:
            four_unique_digit += digit

    return four_unique_digit


def validate_digit(digits):
    """
    Validate the user's guess.

    A valid guess must:
    - Contain exactly four characters.
    - Consist only of numeric digits.
    - Contain no duplicate digits.

    Args:
        digits (str): The user's input.

    Returns:
        bool: True if the input is valid, otherwise False.
    """
    if len(digits) != 4:
        return False

    if not digits.isdigit():
        return False

    seen_digits = set()

    for digit in digits:
        if digit in seen_digits:
            return False
        seen_digits.add(digit)

    return True


def get_digits():
    """
    Prompt the user to enter four unique digits.

    Returns:
        str | bool: The validated digit string if valid; otherwise False.
    """
    guess_digits = input("Enter four unique digits: ").strip()

    if not validate_digit(guess_digits):
        print("Invalid input. Please enter exactly four unique numeric digits.")
        return False

    return guess_digits


def compare_digits():
    """Run the Bulls and Cows game until the player guesses correctly."""
    generated_digits = generate_four_unique_digit()

    # Remove this line when you no longer want to reveal the answer.
    print(generated_digits)

    while True:
        guess_digits = get_digits()

        if not guess_digits:
            continue

        cow_count = 0
        bull_count = 0

        # Compare each guessed digit with the generated number.
        for index, digit in enumerate(guess_digits):
            if digit == generated_digits[index]:
                bull_count += 1
            elif digit in generated_digits:
                cow_count += 1

        print(f"There are {cow_count} cows and {bull_count} bulls.")

        if bull_count == 4:
            print("Congratulations! You guessed the correct number.")
            break


def main():
    """Start the Bulls and Cows game."""
    compare_digits()


if __name__ == "__main__":
    main()