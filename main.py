# Text-Based Tic Tac Toe Game in Python

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def is_draw(board):
    return all(space != " " for space in board)


def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("🎮 Welcome to Tic Tac Toe!")
    print("Player X and Player O")
    print("Enter positions from 1 to 9 as shown below:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move: ")) - 1
            if board[move] != " ":
                print("⚠️ Position already taken. Try again.")
                continue
            board[move] = current_player
        except (ValueError, IndexError):
            print("❌ Invalid input. Choose a number between 1 and 9.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"🏆 Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
