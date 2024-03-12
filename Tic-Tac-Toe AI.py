import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to evaluate the score of the board for the Minimax algorithm
def evaluate(board):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0
    else:
        return None

# Minimax function with alpha-beta pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move using the Minimax algorithm
def best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X'
    ai_player = 'O'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player's move
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    board[row][col] = human_player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print_board(board)

        # Check if the human player has won
        if check_winner(board, human_player):
            print("You win! Congratulations!")
            break

        # Check if the board is full
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI player's move
        print("AI player is making a move...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = ai_player

        print_board(board)

        # Check if the AI player has won
        if check_winner(board, ai_player):
            print("AI player wins! Better luck next time.")
            break

        # Check if the board is full
        if is_board_full(board):
            print("It's a draw!")
            break

# Start the Tic-Tac-Toe game
play_tic_tac_toe()