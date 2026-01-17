# Text-Based Tic Tac Toe Game in Python

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "


def print_board(board):
    print("\n")
    display = [
        board[i] if board[i] != EMPTY else str(i + 1)
        for i in range(9)
    ]
    print(f" {display[0]} | {display[1]} | {display[2]} ")
    print("---|---|---")
    print(f" {display[3]} | {display[4]} | {display[5]} ")
    print("---|---|---")
    print(f" {display[6]} | {display[7]} | {display[8]} ")
    print("\n")


def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]
    return any(all(board[i] == player for i in condition)
               for condition in win_conditions)


def is_draw(board):
    return all(cell != EMPTY for cell in board)


def get_valid_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): "))
            if move not in range(1, 10):
                print("❌ Enter a number between 1 and 9.")
                continue

            index = move - 1
            if board[index] != EMPTY:
                print("⚠️ That position is already taken.")
                continue

            return index
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def tic_tac_toe():
    board = [EMPTY] * 9
    current_player = PLAYER_X
    turn_count = 0

    print("🎮 Welcome to Tic Tac Toe!")
    print("Select positions as shown below:")

    while True:
        print_board(board)
        move = get_valid_move(board, current_player)
        board[move] = current_player
        turn_count += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"🏆 Player {current_player} wins in {turn_count} moves!")
            break

        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X


def main():
    while True:
        tic_tac_toe()
        replay = input("🔁 Play again? (y/n): ").strip().lower()
        if replay != "y":
            print("👋 Thanks for playing Tic Tac Toe!")
            break


if __name__ == "__main__":
    main()


           
