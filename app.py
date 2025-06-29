"""Here's a simple implementation of a Tic Tac Toe game in Python:"""


# Tic Tac Toe game in Python

board = [' ' for _ in range(9)] # Initialize the game board with empty spaces

def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return False

def main():
    current_player = 'X'
    while True:
        print_board()
        move = input("Player {}, enter your move (1-9): ".format(current_player))
        if board[int(move) - 1] == ' ':
            board[int(move) - 1] = current_player
            result = check_win()
            if result:
                print_board()
                if result == 'Tie':
                    print("It's a tie!")
                else:
                    print("Player {} wins! Congratulations!".format(result))
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again.")

if __name__ == '__main__':
    main()


"""How to Play:

1. Run the script.
2. The game board will be displayed.
3. Enter your move by typing a number between 1 and 9, corresponding to the space where you'd like to place your piece (X or O).
4. The game will check for a win or tie after each move.
5. If there's a win or tie, the game will end and display the final board.

Have fun playing Tic Tac Toe!"""