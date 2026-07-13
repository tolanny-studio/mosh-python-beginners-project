import random

player = {"player_1": (1, 0), "player_2": (2, 0)}




def dice_roll():
    return random.choice(range(1, 7))


def switch_player(current_player):
    return 2 if current_player == 1 else 1


def play_game():
    current_player = player["player_1"][0]
    while True:
        print(f"Player {current_player}'s turn")
        while True:
            dice_number = dice_roll()
            print(f"You rolled a {dice_number}")
            if dice_number == 1:
                break
        current_player = switch_player(current_player)


def main():
    play_game()


if __name__ == "__main__":
    main()
