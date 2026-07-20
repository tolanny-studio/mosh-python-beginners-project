from sys import exit
from screen import Screen
from deposit import Deposit
from withdraw import Withdraw
from validate import validate_amount
from balance import read_balance, write_balance
from termcolor import cprint


def main():
    # Read from file
    current_balance = read_balance()
    while True:
        screen = Screen()
        option = screen.get_option()

        if option == 1:
            # Check Balance
            cprint(f"\nThe balance is ${current_balance}", "green")
        elif option == 2:
            # Deposit
            amount = validate_amount("\nEnter deposit amount : ")
            if amount is None:
                continue
            deposit = Deposit(amount)
            current_balance = deposit.update_balance(current_balance)
            # Write to file
            write_balance(current_balance)

        elif option == 3:
            # Withdraw
            amount = validate_amount("\nEnter withdraw amount : ")
            if amount is None:
                continue
            withdraw = Withdraw(current_balance, amount)
            current_balance = withdraw.withdraw()
            # Write to file
            write_balance(current_balance)

        elif option == 4:
            # Exit application
            cprint("\nThanks for banking with us", "green")
            exit()
        else:
            break


if __name__ == "__main__":
    main()
