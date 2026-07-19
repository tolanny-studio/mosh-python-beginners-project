class Balance:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, balance):
        self.__balance += balance

    def print_balance(self):
        print(f"The balance is ${self.__balance}")
