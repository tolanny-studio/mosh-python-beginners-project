class Deposit:
    def __init__(self):
        self.__deposit = self.validate_deposit("Enter deposit amount: ")

    def validate_deposit(self, prompt):

        try:
            amount = int(input(prompt))
        except Exception as e:
            print(f"{amount} is an invalid amount")
            return
        if amount < 0:
            print("Invalid input ! Amount should not be less than $0")
            return
        return amount

    def update_balance(self, current_balance):
        current_balance += self.__deposit
        print(f"${self.__deposit} deposited.\nThe current balance is now ${current_balance}")
        return current_balance
