class Withdraw:
    def __init__(self, current_balance, amount):
        self.__current_balance = current_balance
        self.__amount = amount

    def check_balance(self, amount):
        if amount <= self.__current_balance:
            return True
        return False

    def validate_amount(self):
        if not self.check_balance(self.__amount):
            print(
                f"The {self.__amount} you entered is less than the balance of {self.__current_balance} in the account"
            )
            return
        return self.__amount

    def withdraw(self):
        if self.validate_amount():
            self.__current_balance -= self.__amount
            print(
                f"{self.__amount} withdrawn\nThe current balance is now ${self.__current_balance}"
            )
            return self.__current_balance
