import random


def generate_four_unique_digit():
    four_unique_digit = ""
    while len(four_unique_digit) < 4:
        digit = str(random.randint(1, 9))
        if digit not in four_unique_digit:
            four_unique_digit += digit
    return four_unique_digit


def get_four_unique_digit():
    generated_digits = generate_four_unique_digit()
    print(generated_digits)
    guess_digits = input("Enter four unique digits: ")
    cow = 0
    bull = 0
    for index, digit in enumerate(guess_digits):
        if digit in generated_digits:
            cow += 1
            if index == generated_digits.find(digit):
                bull += 1
                cow -= 1
    print(f"There are {cow} cows, and {bull} bulls")

get_four_unique_digit()
