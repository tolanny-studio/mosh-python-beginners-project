def validate_amount(prompt):
    try:
        amount = int(input(prompt))
        return amount
    except ValueError:
        print("The type should be of integer")
        
