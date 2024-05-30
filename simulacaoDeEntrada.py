def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    moves = [(0, 0), (0, 1), (1, 1), (0, 2), (2, 2)]  # movimentos para teste
    current_move = 0
    print_board(board)
    while current_move < len(moves):
        row, col = moves[current_move]
        if board[row][col] == ' ':
            if current_move % 2 == 0:
                board[row][col] = 'X'
            else:
                board[row][col] = 'O'
            if check_winner(board, 'X'):
                print("X wins!")
                break
            elif check_winner(board, 'O'):
                print("O wins!")
                break
            elif is_board_full(board):
                print("Draw!")
                break
            print_board(board)
        current_move += 1
    print_board(board)

if _name_ == "_main_":
    main()
""" Explicação da função minimax
Vamos debugar e explicar a função minimax passo a passo, pelo menos nas 5 primeiras iterações:

Primeira iteração:

A função é chamada com o tabuleiro inicial e is_maximizing = True.
Como o tabuleiro está vazio, ela tenta o primeiro movimento para 'O' e chama minimax recursivamente.
Segunda iteração:

O tabuleiro tem 'O' no primeiro lugar.
A função é chamada para is_maximizing = False.
Tenta todos os movimentos para 'X' e chama minimax recursivamente.
Terceira iteração:

Continua com as tentativas de movimento, alternando entre 'O' e 'X', chamando minimax recursivamente até alcançar um estado terminal (vitória, empate ou tabuleiro cheio)."""
