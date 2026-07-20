class Deposit:
    def __init__(self, amount):
        self.__deposit = amount

    def validate_deposit(self):
        if self.__deposit <= 0:
            print("Invalid input ! Amount should greater than $0")
            return
        return self.__deposit

    def update_balance(self, current_balance):
        if self.validate_deposit():
            current_balance += self.__deposit
            print(
                f"${self.__deposit} deposited.\nThe current balance is now ${current_balance}"
            )
            return current_balance
