import random

SYMBOLS = ["🍉", "🍊", "🍌"]


def validate_amount(prompt):
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
    return validate_amount("Enter starting amount: ")


def get_betting_amount(starting_amount):

    while True:
        betting_amount = validate_amount("Enter betting amount: ")
        if betting_amount > starting_amount:
            print(
                "Invalid amount ⛔ Current balance Amount should be greater than betting amount"
            )
            continue
        return betting_amount


def spin_slots():
    selected_symbol = []
    for _ in range(len(SYMBOLS)):
        selected_symbol.append(random.choice(SYMBOLS))
    return selected_symbol

def count_matches():
  pass

def play_game():
    selected_symbol = spin_slots()
    symbol_occurrence = 1
    symbol_occurrence_list = []
    selected_symbol_string = ""

    for index, symbol in enumerate(selected_symbol):
        if index < len(selected_symbol) - 1:
            selected_symbol_string += f"| {symbol} "
        else:
            selected_symbol_string += f"| {symbol} |"

        if symbol in symbol_occurrence_list:
            symbol_occurrence += 1
        symbol_occurrence_list.append(symbol)

    return symbol_occurrence, selected_symbol_string


def replay_game():
    while True:
        replay = input("\nDo you want to replay game 🔄️: ").lower()
        if replay not in ("y", "n"):
            print("Invalid input ⛔ Enter character y or n")
            continue
        return replay == "y"


def main():
    current_balance = get_starting_amount()
    while current_balance > 0:
        print(f"Current balance: ${current_balance}")

        while True:
            bet_amount = get_betting_amount(current_balance)
            amount_won = 0
            print(f"Bet amount: ${bet_amount}")
            if bet_amount:
                symbol_occurrence, selected_symbol_string = play_game()
                current_balance -= bet_amount
                if symbol_occurrence == 1:

                    current_balance += amount_won
                elif symbol_occurrence == 2:

                    amount_won = 2 * bet_amount
                    current_balance += amount_won
                else:

                    amount_won = 10 * current_balance
                    current_balance += amount_won
                print(f"\n{selected_symbol_string}")
                print(f"Amount Won: ${amount_won}")
                print(f"Current Balance: ${current_balance}")
                if not replay_game():
                    break
        print("Thanks for playing")
        break


if __name__ == "__main__":
    main()
