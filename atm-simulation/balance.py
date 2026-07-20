from pathlib import Path

BALANCE_FILE = Path(__file__).parent / "balance.txt"


def read_balance():
    balance = 0
    try:
        with open(BALANCE_FILE, "r") as file:
            try:
                _balance = int(file.read())
                balance = _balance
            except ValueError as e:
                print(e)
    except FileNotFoundError:
        print("File not found")
    return balance


def write_balance(current_balance):
    try:
        with open(BALANCE_FILE, "w") as file:
            if current_balance:
                file.write(str(current_balance))
    except FileNotFoundError:
        print("file not found")
