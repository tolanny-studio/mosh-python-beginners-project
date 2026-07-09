from termcolor import cprint

# Constants used throughout the game.
LINE = "---+---+---"
BOARD_SIZE = 3


def display_board(board):
    """Display the current state of the Tic-Tac-Toe board."""

    for index, row in enumerate(board):
        cprint(LINE, "yellow")
        cprint(f" {row[0]} | {row[1]} | {row[2]}", "yellow")

        if index != BOARD_SIZE - 1:
            cprint(LINE, "yellow")


def switch_player(player):
    """Return the next player's symbol."""

    if player == "X":
        return "O"
    return "X"


def is_full_board(board):
    """Return True if the board contains no empty spaces."""

    for row in board:
        if " " in row:
            return False
    return True


def check_winner(board):
    """Return True if the board contains a winning combination."""

    # Check rows.
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns.
    for column in range(BOARD_SIZE):
        if board[0][column] == board[1][column] == board[2][column] != " ":
            return True

    # Check the main diagonal.
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    # Check the anti-diagonal.
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def validate_coordinate(prompt):
    """Prompt the user until a valid board coordinate is entered."""

    while True:
        try:
            coordinate = int(input(prompt))
        except ValueError:
            cprint("Please enter a whole number 🔄️", "red")
            continue

        if coordinate not in range(BOARD_SIZE):
            cprint("Please enter a valid input 🔄️", "red")
            continue

        return coordinate


def get_coordinate():
    """Prompt the user for valid row and column coordinates."""

    row = validate_coordinate("Enter row coordinate (0-2): ")
    column = validate_coordinate("Enter column coordinate (0-2): ")

    return row, column


def replay_game():
    """Ask the user whether to play another game."""

    while True:
        replay = input("Do you wish to replay? (y/n): ").lower()

        if replay not in ("y", "n"):
            cprint("Invalid input ❌. Enter 'y' or 'n'.", "red")
            continue

        return replay == "y"


def play_game(board):
    """Run a single Tic-Tac-Toe game."""

    current_player = "X"

    while not is_full_board(board):
        # Get a valid move from the current player.
        row, column = get_coordinate()
        coordinate = board[row][column]

        # Ensure the selected square is empty.
        if coordinate != " ":
            cprint("Current coordinate is not empty, try another coordinate 🔄️", "red")
            display_board(board)
            continue

        # Place the current player's mark on the board.
        board[row][column] = current_player
        display_board(board)

        # End the game if the current move creates a winning combination.
        if check_winner(board):
            cprint(f"{current_player} is the winner 💯", "blue")
            return

        # Pass the turn to the other player.
        current_player = switch_player(current_player)

    # The board is full and no player has won.
    cprint("It's a draw! 🤝", "cyan")


def main():
    """Start the game and continue until the user chooses to quit."""

    while True:
        # Create a new empty game board.
        board = [[" ", " ", " "] for _ in range(BOARD_SIZE)]

        display_board(board)
        play_game(board)

        if not replay_game():
            cprint("Thanks for playing! 👋", "green")
            break


if __name__ == "__main__":
    main()