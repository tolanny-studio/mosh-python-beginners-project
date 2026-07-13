import random


def generate_four_unique_digit():
    four_unique_digit = ""
    while len(four_unique_digit) < 4:
        digit = str(random.randint(1, 9))
        if digit not in four_unique_digit:
            four_unique_digit += digit
    return four_unique_digit


def validate_digit(digits):
    digit_list = []
    for digit in digits:
        if not (digit >= "0" and digit <= "9"):
            return False
        if digit not in digit_list:
            digit_list.append(digit)
        else:
            return False
    if len(digits) != 4:
        return False
    return True


def get_digits():
    guess_digits = input("Enter four unique digits: ")
    if not validate_digit(guess_digits):
        print("Invalid digit")
        return False
    return guess_digits


def compare_digits():
    generated_digits = generate_four_unique_digit()
    print(generated_digits)
    while True:
        guess_digits = get_digits()
        if not guess_digits:
            continue
        cow = 0
        bull = 0
        for index, digit in enumerate(guess_digits):
            if digit in generated_digits:
                cow += 1
                if index == generated_digits.find(digit):
                    bull += 1
                    cow -= 1
        print(f"There are {cow} cows, and {bull} bulls")
        if bull == 4:
            break


def main():
    compare_digits()


if __name__ == "__main__":
    main()
