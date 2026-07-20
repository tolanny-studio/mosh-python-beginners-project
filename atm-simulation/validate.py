def validate_amount(prompt):
    """
    Prompt the user for an integer amount.

    Args:
        prompt (str): Message displayed to the user.

    Returns:
        int | None:
            The entered integer if valid,
            otherwise None.
    """
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None