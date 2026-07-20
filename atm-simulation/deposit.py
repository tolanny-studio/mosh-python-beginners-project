class Deposit:
    """Represent a deposit transaction."""

    def __init__(self, amount):
        """
        Initialize a deposit transaction.

        Args:
            amount (int): The amount to deposit.
        """
        self.__deposit = amount

    def validate_deposit(self):
        """
        Validate the deposit amount.

        Returns:
            bool: True if the deposit amount is valid,
            otherwise False.
        """
        if self.__deposit <= 0:
            print("Invalid input! Amount must be greater than $0.")
            return False
        return True

    def update_balance(self, current_balance):
        """
        Add the deposit amount to the current balance.

        Args:
            current_balance (int): The current account balance.

        Returns:
            int: The updated account balance.
        """
        if not self.validate_deposit():
            return current_balance

        current_balance += self.__deposit

        print(
            f"${self.__deposit} deposited.\n"
            f"The current balance is now ${current_balance}"
        )

        return current_balance