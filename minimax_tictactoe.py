def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if board[row][col] == ' ':
            board[row][col] = 'X'
            if check_winner(board, 'X'):
                print("X wins!")
                break
            elif is_board_full(board):
                print("Draw!")
                break
            board[row][col] = 'O'
            print_board(board)
            if check_winner(board, 'O'):
                print("O wins!")
                break
            elif is_board_full(board):
                print("Draw!")
                break
        print_board(board)

if _name_ == "_main_":
    main()
