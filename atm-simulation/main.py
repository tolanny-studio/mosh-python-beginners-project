from sys import exit
from screen import Screen
from deposit import Deposit
from balance import Balance
from withdraw import Withdraw


def main():
    current_balance = 300
    while True:
        screen = Screen()
        option = screen.get_option()

        if option == 1:
            # Check Balance
            balance = Balance()
            balance.set_balance(current_balance)
            balance.print_balance()
        if option == 2:
            # Deposit
            deposit = Deposit()
            current_balance = deposit.update_balance(current_balance)

        if option == 3:
            # Withdraw
            withdraw = Withdraw(current_balance)
            current_balance = withdraw.withdraw()

        if option == 4:
            exit()


if __name__ == "__main__":
    main()
