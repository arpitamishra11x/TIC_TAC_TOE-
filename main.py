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
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)


def is_draw(board):
    return " " not in board


def get_valid_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("❌ Please choose a number between 1 and 9.")
                continue

            index = move - 1
            if board[index] != " ":
                print("⚠️ Position already taken. Choose another.")
                continue

            return index
        except ValueError:
            print("❌ Invalid input. Numbers only.")


def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("🎮 Welcome to Tic Tac Toe!")
    print("Positions are numbered as:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board(board)
        move = get_valid_move(board, current_player)
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🏆 Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        tic_tac_toe()
        replay = input("🔁 Do you want to play again? (y/n): ").lower()
        if replay != "y":
            print("👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()
