import random

# Game rules.
WINNING_SCORE = 100
LOSING_ROLL = 1

# Stores each player's ID and total score.
players = {
    "player_1": {"id": 1, "score": 0},
    "player_2": {"id": 2, "score": 0},
}


def dice_roll():
    """Return a random dice roll between 1 and 6."""
    return random.randint(1, 6)


def switch_player(current_player):
    """Return the ID of the next player."""
    return 2 if current_player == 1 else 1


def check_winner(players):
    """Return the winning player's data if they have reached the winning score."""
    for player_data in players.values():
        if player_data["score"] >= WINNING_SCORE:
            return player_data


def display_scores():
    """Display the current scores of both players."""
    print(
        f"Current scores: Player 1: {players['player_1']['score']}, "
        f"Player 2: {players['player_2']['score']}"
    )


def play_game():
    """Run the main game loop until a player wins."""
    current_player = players["player_1"]["id"]

    while True:
        player_data = players[f"player_{current_player}"]
        turn_score = 0

        print(f"\nPlayer {current_player}'s turn")

        while True:
            dice_number = dice_roll()
            print(f"You rolled a {dice_number}")

            # Rolling a 1 resets the player's total score and ends their turn.
            if dice_number == LOSING_ROLL:
                print("You rolled a 1! You scored 0 this turn.")
                player_data["score"] = 0
                display_scores()

                current_player = switch_player(current_player)
                break

            # Accumulate points earned during the current turn.
            turn_score += dice_number

            # Keep prompting until a valid response is entered.
            while True:
                roll_again = input("Roll again (y/n): ").lower()

                if roll_again not in ("y", "yes", "n", "no"):
                    print("Invalid input! Enter (y/n)")
                    continue
                break

            # Continue the current turn if the player chooses to roll again.
            if roll_again in ("y", "yes"):
                continue

            # Bank the turn score into the player's total score.
            player_data["score"] += turn_score

            winner = check_winner(players)
            if winner:
                print(f"Player {winner['id']} wins with {winner['score']} points!")
                return

            print(f"You scored {turn_score} this turn.")
            display_scores()

            # Pass control to the other player.
            current_player = switch_player(current_player)
            break


def main():
    """Start the dice game."""
    play_game()


if __name__ == "__main__":
    main()