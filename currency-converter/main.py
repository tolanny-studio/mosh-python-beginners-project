from forex_python.converter import CurrencyRates

# Create a CurrencyRates object for retrieving live exchange rates.
currency = CurrencyRates()


def get_amount():
    """Prompt the user for a valid amount to convert."""
    while True:
        try:
            amount = float(input("Enter the amount: "))

            # Ensure the amount is positive.
            if amount < 1:
                print("Amount must be greater than 0️⃣")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def get_source_currency():
    """Prompt the user for the source currency and retrieve its exchange rates."""
    while True:
        source_currency = (
            input("Enter source currency💵(USD/EUR/CAD): ").upper().strip()
        )

        # Accept only the supported source currencies.
        if source_currency not in ("USD", "EUR", "CAD"):
            print("Invalid currency. Input from with the options💵💶")
            continue

        # Retrieve the available exchange rates for the selected currency.
        try:
            all_currency = currency.get_rates(source_currency)
            return source_currency, all_currency

        except Exception as e:
            print(f"Unable to retrieve exchange rates: {e}")


def get_target_currency(all_currency):
    """Prompt the user for a valid target currency."""
    while True:
        target_currency = input("Enter target currency: ").upper().strip()

        # Currency codes must contain exactly three letters.
        if len(target_currency) != 3:
            print("Invalid input ❌")
            continue

        # Ensure the target currency is supported by the API.
        if target_currency not in all_currency:
            print("Currency not in API 🪙")
            continue

        return target_currency


def currency_converter():
    """Convert an amount from one currency to another."""
    # Collect all information required for the conversion.
    amount = get_amount()
    source_currency, all_currency = get_source_currency()
    target_currency = get_target_currency(all_currency)

    # Perform the conversion and display the result.
    try:
        exchange = currency.convert(source_currency, target_currency, amount)
        print(f"{amount:.2f} {source_currency} equals {exchange:.2f} {target_currency}")

    except Exception as e:
        print(f"Conversion failed: {e}.")


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    currency_converter()