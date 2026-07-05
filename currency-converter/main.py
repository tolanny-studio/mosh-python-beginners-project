from forex_python.converter import CurrencyRates

currency = CurrencyRates()


def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount < 1:
                print("Amount must be greater than 0️⃣")
                continue
            return amount
        except ValueError:
            print(f"Please enter a valid number.")


def get_source_currency():
    while True:
        source_currency = (
            input("Enter source currency💵(USD/EUR/CAD): ").upper().strip()
        )
        if source_currency not in ("USD", "EUR", "CAD"):
            print("Invalid currency. Input from with the options💵💶")
            continue
        try:
            all_currency = currency.get_rates(source_currency)
            return source_currency, all_currency
        except Exception as e:
            print(f"Unable to retrieve exchange rates: {e}")


def get_target_currency(all_currency):
    while True:

        target_currency = input("Enter target currency: ").upper().strip()
        if len(target_currency) != 3:
            print("Invalid input ❌")
            continue
        if target_currency not in all_currency:
            print("Currency not in API 🪙")
            continue
        return target_currency


def currency_converter():
    amount = get_amount()
    source_currency, all_currency = get_source_currency()
    target_currency = get_target_currency(all_currency)
    try:
        exchange = currency.convert(source_currency, target_currency, amount)
        print(f"{amount:.2f} {source_currency} equals {exchange:.2f} {target_currency}")
    except Exception as e:
        print(f"Conversion failed: {e}.")


if __name__ == "__main__":
    currency_converter()
