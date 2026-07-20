from pathlib import Path

BALANCE_FILE = Path(__file__).parent / "balance.txt"


def read_balance():
    with open(BALANCE_FILE, "r") as file:
            try:
                return int(file.read())   
            except FileNotFoundError:
                print("File not found")
                return 0
            except ValueError as e:
                print("Invalid balance format in file")
                return 0




def write_balance(current_balance):
    try:
        with open(BALANCE_FILE, "w") as file:
            if current_balance:
                file.write(str(current_balance))
    except FileNotFoundError:
        print("file not found")
