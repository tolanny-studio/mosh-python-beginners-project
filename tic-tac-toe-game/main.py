from termcolor import cprint

LINE = "---+---+---"
BOARD_SIZE = 3


def display_board(board):
    for index, row in enumerate(board):
        cprint(LINE, "yellow")
        cprint(f" {row[0]} | {row[1]} | {row[2]}", "yellow")

        if index != 2:
            cprint(LINE, "yellow")


def switch_player(player):

    if player == "X":
        return "O"
    return "X"


def is_full_board(board):
    for row in board:
        if " " in row:
            return False
    return True


def check_winner(board):

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != " ":
            return True

    # Check main diagonal
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    # Check anti-diagonal
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def validate_coordinate(prompt):
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
    row = validate_coordinate("Enter row coordinate (0-2): ")
    column = validate_coordinate("Enter column coordinate (0-2): ")
    return row, column


def replay_game():
    while True:
        replay = input("Do you wish to replay ? (y,n) ").lower()

        if replay not in ("y", "n"):
            print("Invalid input❌. Enter y or n ")
            continue
        if replay == "y":
            return True
        return False


def play_game(board):

    current_player = "X"

    while not is_full_board(board):
        row, column = get_coordinate()
        coordinate = board[row][column]

        if coordinate != " ":
            cprint("Current coordinate is not empty, try another coordinate 🔄️", "red")
            display_board(board)
            continue

        board[row][column] = current_player
        display_board(board)

        if check_winner(board):
            cprint(f"{current_player} is the winner 💯", "blue")
            return

        current_player = switch_player(current_player)

    cprint("It's a draw! 🤝", "cyan")

def main():
    while True:
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        display_board(board)
        play_game(board)
        if not replay_game():
            cprint("Thanks for playing","green")
            break


if __name__ == "__main__":
    main()
