import random


# def play_game():
#     while True:
#         play = input("Roll the dice? (y/n): ").lower()

#         if play in ["yes", "y"]:
#             random_number_1 = random.randrange(1, 7)
#             random_number_2 = random.randrange(1, 7)
#             print((random_number_1, random_number_2))
#         elif play in ["no", "n"]:
#             print("Thanks for playing")
#             break
#         else:
#             print("Invalid input")


# play_game()


def play_game():
   
    while True:
        play = input("Roll the dice? (y/n): ").lower()

        if play in ["yes", "y"]:
            random_number_1 = random.randint(1, 6)
            random_number_2 = random.randint (1, 6)
            print((random_number_1, random_number_2))
        elif play in ["no", "n"]:
            print("Thanks for playing")
            break
        else:
            print("Invalid input")


play_game()
