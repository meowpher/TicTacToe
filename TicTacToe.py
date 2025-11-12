"""Python Tic Tac Toe Game"""
import random

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def get_free_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def player_move(board, player):
    while True:
        try:
            pos = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = pos // 3, pos % 3
            if 0 <= pos <= 8 and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print('Invalid move, try again.')
        except ValueError:
            print('Please enter a number from 1 to 9.')

def machine_move(board, player):
    move = random.choice(get_free_positions(board))
    board[move[0]][move[1]] = player
    print(f"Machine plays at: {move[0]*3 + move[1] + 1}")

def main():
    print('Welcome to Tic Tac Toe!')
    mode = input('Choose mode: 1 - Player vs Machine, 2 - Player vs Player: ')
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        if mode == '1' and current_player == 'O':
            machine_move(board, 'O')
        else:
            player_move(board, current_player)
        if check_winner(board, current_player):
            print_board(board)
            print(f'Player {current_player} wins!')
            break
        if not get_free_positions(board):
            print_board(board)
            print('The game is a draw!')
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()