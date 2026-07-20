class Screen:
    """Display the ATM menu and collect a valid menu option."""
    def __init__(self):
        print("\nWELCOME TO THE ATM!\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit ")

        self.__option = self.__validate_option("\nPlease enter an option: ")

    def __validate_option(self, prompt):
        while True:
            try:
                option = int(input(prompt))
            except ValueError:
                print("Invalid input")
                continue

            if option not in (1, 2, 3, 4):
                print("Invalid option. Enter between 1 - 4")
                continue

            return option

    def get_option(self):
        return self.__option
