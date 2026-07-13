import random
import sys

WINNING_SCORE = 100
LOSING_ROLL = 1

player = {
    "player_1": {"id": 1, "score": 0},
    "player_2": {"id": 2, "score": 0},
}


def dice_roll():
    return random.randint(1, 6)


def switch_player(current_player):
    return 2 if current_player == 1 else 1


def check_winner():
    for player_data in player.values():
        if player_data["score"] >= WINNING_SCORE:
            return player_data


def display_scores():
    print(
        f"Current scores: Player 1: {player['player_1']['score']}, "
        f"Player 2: {player['player_2']['score']}"
    )


def play_game():
    current_player = player["player_1"]["id"]

    while True:
        player_data = player[f"player_{current_player}"]
        turn_score = 0

        print(f"\nPlayer {current_player}'s turn")

        while True:

            dice_number = dice_roll()
            print(f"You rolled a {dice_number}")
            if dice_number == LOSING_ROLL:
                turn_score = 0
                print("You rolled a 1! You scored 0 this turn.")
                player[f"player_{current_player}"]["score"] = 0
                display_scores()

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
            player_data["score"] += turn_score

            winner = check_winner()
            if winner:
                print(f"The winner of the game is {winner["id"]} with a score of 100")
                return

            print(f"You scored {turn_score} this turn.")

            display_scores()

            current_player = switch_player(current_player)
            break


def main():
    play_game()


if __name__ == "__main__":
    main()
