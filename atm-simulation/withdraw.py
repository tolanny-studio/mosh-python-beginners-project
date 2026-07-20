class Withdraw:
    """Represent a withdrawal transaction."""

    def __init__(self, current_balance, amount):
        """
        Initialize a withdrawal transaction.

        Args:
            current_balance (int): Current account balance.
            amount (int): Amount to withdraw.
        """
        self.__current_balance = current_balance
        self.__amount = amount

    def check_balance(self):
        """
        Check whether there is enough balance.

        Returns:
            bool: True if the withdrawal is allowed.
        """
        return self.__amount <= self.__current_balance

    def validate_amount(self):
        """
        Validate the withdrawal amount.

        Returns:
            bool: True if the amount is valid.
        """
        if self.__amount <= 0:
            print("Withdrawal amount must be greater than $0.")
            return False

        if not self.check_balance():
            print(
                f"The amount entered (${self.__amount}) exceeds "
                f"the current balance (${self.__current_balance})."
            )
            return False

        return True

    def withdraw(self):
        """
        Withdraw money from the account.

        Returns:
            int: The updated account balance.
        """
        if not self.validate_amount():
            return self.__current_balance

        self.__current_balance -= self.__amount

        print(
            f"${self.__amount} withdrawn.\n"
            f"The current balance is now ${self.__current_balance}"
        )

        return self.__current_balance