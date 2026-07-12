import random

PLAYER_1 = 1
PLAYER_2 = 2

current_player = PLAYER_1


def dice_roll():
    return random.choice(range(1, 7))


def switch_player():
    if current_player == PLAYER_1:
        return PLAYER_2
    return PLAYER_1


def play_game():
    while True:
        print(f"Player{current_player}'s turn")
        while True:
            print(f"You rolled a {dice_roll()}")
            roll_again = input("Roll again: ").lower()
            if roll_again in ("yes", "y"):
                continue
            break


def main():
    play_game()


if __name__ == "__main__":
    main()
