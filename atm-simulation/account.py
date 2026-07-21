from termcolor import cprint
from balance import read_balance, write_balance
from validate import validate_amount


class Account:
    """Represent a bank account."""

    def __init__(self):
        """Load the account balance from storage."""
        self.__balance = read_balance()

    def get_balance(self):
        """Return the current account balance."""
        cprint(f"The current balance is ${self.__balance} 💵", "green")

    def deposit(self):
        """Deposit money into the account."""
        amount = validate_amount("\nEnter deposit amount: ")

        if amount is None:
            return

        if amount <= 0:
            cprint("\nAmount must be greater than $0.", "yellow")
            return

        self.__balance += amount

        write_balance(self.__balance)

        cprint(
            f"\n${amount} deposited." f"\nCurrent balance: ${self.__balance}",
            "green",
        )

    def withdraw(self):
        """Withdraw money from the account."""
        amount = validate_amount("\nEnter withdrawal amount: ")

        if amount is None:
            return

        if amount <= 0:
            cprint("\nAmount must be greater than $0.", "yellow")
            return

        if amount > self.__balance:
            cprint(
                f"\nInsufficient funds." f"\nCurrent balance: ${self.__balance}",
                "yellow",
            )
            return

        self.__balance -= amount

        write_balance(self.__balance)

        cprint(
            f"\n${amount} withdrawn." f"\nCurrent balance: ${self.__balance}",
            "magenta",
        )
