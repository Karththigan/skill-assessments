import random
import time


print("Welcome to Tic-Tac-Toe!")

user_symbol = input("Do you want to be Player X or Player O? (X/O) ").upper()

valid_symbols = ["X", "O"]

while user_symbol not in valid_symbols:
    user_symbol = input("Please choose one of either 'X' or 'O': ").upper()

computer_symbol = "O" if user_symbol == "X" else "X"

round_num = 1
game_over = False

curr_player_is_user = True if user_symbol == "X" else False

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

def print_board(board):
    print("   " + "   ".join(str(col) for col in range(0, 3)))
    for row_idx, row in enumerate(board):
        print(f"{row_idx}  " + " | ".join(row))

def place_cpu_move(board, symbol):
    # Find all available spots on the board
    empty_positions = [
        (row_idx, col_idx)
        for row_idx in range(3)
        for col_idx in range(3)
        if board[row_idx][col_idx] == "-"
    ]

    if not empty_positions:
        raise ValueError("No empty spots left on the board!")

    row, col = random.choice(empty_positions)

    board[row][col] = symbol

    return row, col


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]

    return False

def is_valid_placement(row_num, col_num, board):
    if board[row_num][col_num] == "-":
        return True
    return False

while not game_over:
    print(f"========== ROUND {round_num} ========== \n")
    if curr_player_is_user:
        print(f"It is Player {user_symbol}'s turn")
        print_board(board)
        turn_over = False
        while not turn_over:
            print(f"Where do you want to draw a {user_symbol}?")
            time.sleep(1)
            try:
                row_num = int(input("Row? "))
                col_num = int(input("Col? "))

                if (0 <= row_num < len(board)) and (0 <= col_num < len(board[0])):
                    if is_valid_placement(row_num, col_num, board):
                        board[row_num][col_num] = user_symbol
                        turn_over = True
                    else:
                        print("That spot is already taken. Please choose another!")
                else:
                    print("Row and column must be within the board's range.")
            except ValueError:
                print("Please enter a valid number for row and column.")

        print_board(board)
        print(f"Player {user_symbol} turn is over!")
        time.sleep(2)
    else:
        print(f"It is Player {computer_symbol}'s turn")
        place_cpu_move(board, computer_symbol)
        print_board(board)
        print(f"Player {computer_symbol} turn is over!")
        time.sleep(2)

    game_over = check_winner(board)
    round_num += 1
    curr_player_is_user = not curr_player_is_user

print(f"GAME OVER! The winner is: {check_winner(board)}")


