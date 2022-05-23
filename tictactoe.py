# File name: tictactoe.py
# Contains tic tac toe game's code in python
# There will be two players in a game. Two signs X and O represent each player. 
# This program supports variable sized TicTacToe board, eg 3x3 / 5x5 / 7x7 / 100x100 board size

import random
from enum import IntEnum

class TicTacToe:
# Initialize TicTacToe board as an empty list
    board = []

# Different states
    class STATES(IntEnum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4


# Positions player's marker in a cell of the grid
    def place_marker(self, symbol, row, column):
        if self.board[row][column] != '-':
            raise ValueError("This slot is occupied")
        self.board[row][column] = symbol


# Get size of TicTacToe board from user
    def get_board_size(self):
        size = -1

        # taking size of borad as user input
        # This block makes sure user enters correct board size only
        while True:
            user_input = input("Enter size of TicTacToe board: ")
            try:
                size = int(user_input)
                if size > 2:
                    break
                else:
                    print("The size must be an integer number greater than 2")
            except ValueError:
                print("The size must be an integer number greater than 2")

        return size


# Create a variable sized TicTacToe board using a 2-dimensional list and initialize each cell as empty using '-'
    def create_board(self, size):

# Initialize TicTacToe board as an empty list
        board = [] 
        for i in range(size):
            row = []
            for j in range(size):
                row.append('-')
            board.append(row)
        return board


# Get the 1st player as 0 or 1 randomly
    def get_first_player_randomly(self):
        return random.randint(0, 1)


# Checks whether the player wins or not
# A player wins if the player places his/her sign completely row-wise or column-wise, or diagonally.
    def does_player_win(self, player, board):
        win = None
        n = len(board)

        # checking row-wise placement of the player's sign
        for i in range(n):
            win = True
            for j in range(n):
                if board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking column-wise placement of the player's sign
        for i in range(n):
            win = True
            for j in range(n):
                if board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonal(top-left to bottom-right) placement of the player's sign
        win = True
        for i in range(n):
            if board[i][i] != player:
                win = False
                break
        if win:
            return win

       # checking diagonal(bottom-left to top-right) placement of the player's sign
        win = True
        for i in range(n):
            if board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False


# Check whether the board is filled or not. If filled then draw
    def is_filled(self, board):
        for row in board:
            for item in row:
                if item == '-':
                    return False
        return True


# swap player for the next turn
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'


# Show the board as we will show the board multiple times to the users while they are playing.
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()


# Start the game
    def start(self):

# Get the board size from user
        size = self.get_board_size()

# creates an empty board
        board = TicTacToe.board = self.create_board(size)

# Select the first turn of the player randomly as 'X' or 'O'
        player = 'X' if self.get_first_player_randomly() == self.STATES.CROSS_TURN else 'O'

# Initialze game status
        status = -1

# an infinite loop that breaks when the game is over (either win or draw).
        while True:
            print(f"Player {player} turn")

# Show the board to the player to select the spot for the next move
            self.show_board()

            # Ask the player to enter the row and column number
            # This block makes sure user only enters correct row and column numbers
            while True:
                try:
                    row, col = list(map(int, input("Enter row and column numbers to position player's marker: ").split()))
                    if row > 0 and row <= size and col > 0 and col <= size:
                        if board[row - 1][col - 1] == '-':
                            break
                        else:
                            print("This slot is already occupied. Try an empty spot.")
                    else:
                        print(f"The row and column numbers must be integer number from 1 to {size}")
                except ValueError:
                    print(f"The row and column numbers must be integer number from 1 to {size}")

            print()

            # Update the spot with the respective player sign
            self.place_marker(player, row - 1, col - 1)

            # checking whether current player has won or not. If won, change the status and break infinite loop
            if self.does_player_win(player, board):
                status = self.STATES.CROSS_WON if player == 'X' else self.STATES.NAUGHT_WON
                break

            # checking whether the game is draw or not. If board is filled, then draw, change the status and break infinite loop
            if self.is_filled(board):
                status = self.STATES.DRAW
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the result of the game
        if status == self.STATES.CROSS_WON:
            print("Player X wins the game!")
        elif status == self.STATES.NAUGHT_WON:
            print("Player O wins the game!")
        elif status == self.STATES.DRAW:
            print("Match Draw!")

        # showing the final view of board
        self.show_board()


# Driver. Starts the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
