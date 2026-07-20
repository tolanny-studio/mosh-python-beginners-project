from sys import exit
from screen import Screen
from deposit import Deposit
from withdraw import Withdraw
from validate import validate_amount


def main():
    current_balance = 300
    while True:
        screen = Screen()
        option = screen.get_option()

        if option == 1:
            # Check Balance
            print(f"The balance is ${current_balance}")
        if option == 2:
            # Deposit
            amount = validate_amount("Enter deposit amount : ")
            if not amount:
                continue
            deposit = Deposit(amount)
            current_balance = deposit.update_balance(current_balance)

        if option == 3:
            # Withdraw
            amount = validate_amount("Enter withdraw amount : ")
            if not amount:
                continue
            withdraw = Withdraw(current_balance)
            current_balance = withdraw.withdraw()

        if option == 4:
            exit()


if __name__ == "__main__":
    main()
