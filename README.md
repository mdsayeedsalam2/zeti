# zeti
This project has implemented the logic of the Tic Tac Toe game using Python. There will be two players in a game. Two signs X and O represent each player.

File tictactoe.py contains tic tac toe game's code that does not use native Python loops. This program supports variable sized TicTacToe board, e.g. 3x3 / 5x5 / 7x7 / 100x100 board size. It works for board sizes 3x3 to 4x4 as upper_size = 4 is set in the code. Just change the value of upper_size = 7 to work for board sizes from 3x3 to 7x7 etc. The game is automatically played by the program and hence no user input is needed.

File test_tictactoe.py contains Python unit tests code for tic tac toe game code shown in tictactoe.py file.

Also set up Github action that can automatically run unit tests on each new commit.
