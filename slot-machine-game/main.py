import random
from pathlib import Path

# Available slot machine symbols.
SYMBOLS = ["🍉", "🍊", "🍌"]

# Winning Matches
TWO_MATCH_MULTIPLIER = 2
THREE_MATCH_MULTIPLIER = 10

# File path to load balance

BALANCE_FILE = Path(__file__).parent / "balance.txt"


def validate_amount(prompt):
    """Prompt the user for a valid positive integer amount.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: A validated amount greater than zero.
    """
    while True:
        try:
            amount = int(input(prompt))
        except ValueError:
            print("Invalid Input ⛔ Amount should be an integer")
            continue

        if amount <= 0:
            print("Invalid amount ⛔ Amount should be greater than $0")
            continue

        return amount


def get_starting_amount():
    """Return the player's saved balance or prompt for a new one."""
    try:
        with open(BALANCE_FILE, "r") as file:
            balance = file.readline().strip()

            if not balance:
                return validate_amount("Enter starting amount: ")

            return int(balance)

    except FileNotFoundError:
        return validate_amount("Enter starting amount: ")


def save_balance(balance):
    with open(BALANCE_FILE, "w") as file:
        file.write(str(balance))


def load_balance(starting_amount):
    """Prompt the user for a valid betting amount.

    The betting amount cannot exceed the player's current balance.

    Args:
        starting_amount (int): The player's current balance.

    Returns:
        int: A validated betting amount.
    """
    while True:
        betting_amount = validate_amount("Enter betting amount: ")

        if betting_amount > starting_amount:
            print(
                "Invalid amount ⛔ Current balance amount should be greater than or equal to the betting amount."
            )
            continue

        return betting_amount


def spin_slots():
    """Spin the slot machine.

    Returns:
        list[str]: Three randomly selected slot symbols.
    """
    return [random.choice(SYMBOLS) for _ in range(len(SYMBOLS))]


def count_matches(selected_symbol):
    """Count the highest number of matching symbols.

    Args:
        selected_symbol (list[str]): The symbols produced by the slot machine.

    Returns:
        int:
            1 if all symbols are different,
            2 if two symbols match,
            3 if all three symbols match.
    """
    seen_symbols = []
    match_count = 1

    for symbol in selected_symbol:
        if symbol in seen_symbols:
            match_count += 1

        seen_symbols.append(symbol)

    return match_count


def display_symbol(selected_symbol):
    """Format the slot symbols for display.

    Args:
        selected_symbol (list[str]): The generated slot symbols.

    Returns:
        str: The formatted slot display.
    """
    return "| " + " | ".join(selected_symbol) + " |"


def play_game():
    """Perform one slot machine spin.

    Returns:
        tuple[int, str]:
            - Number of matching symbols.
            - Formatted slot machine display.
    """
    selected_symbol = spin_slots()

    return count_matches(selected_symbol), display_symbol(selected_symbol)


def replay_game():
    """Ask the player whether to play another round.

    Returns:
        bool: True if the player wants to continue, otherwise False.
    """
    while True:
        replay = input("\nDo you want to replay game 🔄️: ").lower().strip()

        if replay not in ("y", "n"):
            print("Invalid input ⛔ Enter character y or n")
            continue

        return replay == "y"


def main():
    """Run the slot machine game."""
    current_balance = get_starting_amount()

    while current_balance > 0:
        print(f"Current balance: ${current_balance}")
        bet_amount = load_balance(current_balance)
        amount_won = 0

        print(f"Bet amount: ${bet_amount}")

        # Deduct the player's bet before spinning.
        current_balance -= bet_amount

        match_count, selected_symbol_string = play_game()

        if match_count == 1:
            print("No match.")
        elif match_count == 2:
            print("Two symbols matched!")
            amount_won = TWO_MATCH_MULTIPLIER * bet_amount
            current_balance += amount_won
        else:
            print("Three symbols matched!")
            amount_won = THREE_MATCH_MULTIPLIER * bet_amount
            current_balance += amount_won
        save_balance(current_balance)
        print(f"\n{selected_symbol_string}")
        print(f"Amount Won: ${amount_won}")
        print(f"Current Balance: ${current_balance}")

        if not replay_game():
            print("Thanks for playing")
            break


if __name__ == "__main__":
    main()
