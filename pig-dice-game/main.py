import random

player = {
    "player_1": {"id": 1, "score": 0},
    "player_2": {"id": 2, "score": 0},
}


def dice_roll():
    return random.choice(range(1, 7))


def switch_player(current_player):
    return 2 if current_player == 1 else 1


def play_game():
    current_player = player["player_1"]["id"]

    while True:
        current = player[f"player_{current_player}"]
        turn_score = 0

        print(f"\nPlayer {current_player}'s turn")

        while True:
            dice_number = dice_roll()
            print(f"You rolled a {dice_number}")

            if dice_number == 1:
                turn_score = 0
                print("You rolled a 1! You scored 0 this turn.")

                print(
                    f"Current scores: Player 1: {player['player_1']['score']}, "
                    f"Player 2: {player['player_2']['score']}"
                )

                current_player = switch_player(current_player)
                break

            # Add the roll to the turn score immediately
            turn_score += dice_number

            while True:
                roll_again = input("Roll again (y/n): ").lower()

                if roll_again not in ("y", "yes", "n", "no"):
                    print("Invalid input! Enter (y/n)")
                    continue
                break

            if roll_again in ("y", "yes"):
                continue

            # Bank the turn score
            current["score"] += turn_score

            print(f"You scored {turn_score} this turn.")

            print(
                f"Current scores: Player 1: {player['player_1']['score']}, "
                f"Player 2: {player['player_2']['score']}"
            )

            current_player = switch_player(current_player)
            break


def main():
    play_game()


if __name__ == "__main__":
    main()