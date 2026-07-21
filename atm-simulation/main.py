from sys import exit
from screen import Screen
from termcolor import cprint
from account import Account


def atm():
    account = Account()

    while True:
        screen = Screen()
        option = screen.get_option()

        if option == 1:
            # Check Balance
            account.get_balance()
        elif option == 2:
            account.deposit()

        elif option == 3:
            # Withdraw
            account.withdraw()

        elif option == 4:
            # Exit application
            cprint("\nThanks for banking with us 💵 ", "green")
            exit()
        else:
            break


def main():
    atm()


if __name__ == "__main__":
    main()
