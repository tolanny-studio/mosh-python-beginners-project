class Withdraw:
    def __init__(self,current_balance):
        self.__current_balance = current_balance
        self.__amount = self.validate_amount("Enter amount to withdraw : ")

    def validate_amount(self, prompt):
        try:
            amount = int(input(prompt))
        except Exception as e:
            print(e)
            return
        if not self.check_balance(amount):
            print(
                f"The {amount} you entered is less than the balance of {self.__current_balance} in the account"
            )
            return
        return amount

    def check_balance(self, amount):
        if amount <= self.__current_balance:
            return True
        return False

    def withdraw(self):
        self.__current_balance -= self.__amount
        print(
            f"{self.__amount} withdrawn\nThe current balance is now ${self.__current_balance}"
        )
        return self.__current_balance
