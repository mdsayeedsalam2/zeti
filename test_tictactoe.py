# File name: test_tictactoe.py
# Contains Python unit tests code for tic tac toe game code shown in tictactoe.py file
import unittest
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):

# checks whether creating variable sized empty TicTacToe board or not
    def test_create_variable_sized_empty_board(self):
        self.assertEqual(TicTacToe.create_board(self, 4), [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']])
        self.assertEqual(TicTacToe.create_board(self, 3), [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])


# checks whether determining row-wise win or not
    def test_row_wise_win(self):
        self.assertTrue(TicTacToe.does_player_win(self, 'X', [['X', 'X', 'X'], ['-', '-', '-'], ['-', '-', '-']]))
        self.assertFalse(TicTacToe.does_player_win(self, 'O', [['X', 'X', 'X'], ['-', '-', '-'], ['-', '-', '-']]))

# checks whether determining column-wise win or not
    def test_column_wise_win(self):
        self.assertTrue(TicTacToe.does_player_win(self, 'O', [['O', '-', '-'], ['O', '-', '-'], ['O', '-', '-']]))
        self.assertFalse(TicTacToe.does_player_win(self, 'X', [['O', '-', '-'], ['O', '-', '-'], ['O', '-', '-']]))

# checks whether determining 1st diagonally(top-left to bottom-right) win or not
    def test_1st_diagonal_win(self):
        self.assertTrue(TicTacToe.does_player_win(self, 'O', [['O', '-', '-'], ['-', 'O', '-'], ['-', '-', 'O']]))
        self.assertFalse(TicTacToe.does_player_win(self, 'X', [['O', '-', '-'], ['-', 'O', '-'], ['-', '-', 'O']]))
 
# checks whether determining 2nd diagonally(bottom-left to top-right) win or not
    def test_2nd_diagonal_win(self):
        self.assertTrue(TicTacToe.does_player_win(self, 'X', [['-', '-', 'X'], ['-', 'X', '-'], ['X', '-', '-']]))
        self.assertFalse(TicTacToe.does_player_win(self, 'O', [['-', '-', 'X'], ['-', 'X', '-'], ['X', '-', '-']]))

# checks whether the TicTacToe board is filled or not
    def test_filled(self):
        self.assertTrue(TicTacToe.is_filled(self, [['O', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]))
        self.assertFalse(TicTacToe.is_filled(self, [['O', 'O', 'X'], ['X', '-', 'O'], ['O', 'X', 'O']]))

# checks whether swap player for the next turn or not
    def test_player_swap(self):
        self.assertEqual(TicTacToe.swap_player_turn(self,'X'), 'O')
        self.assertEqual(TicTacToe.swap_player_turn(self,'O'), 'X')


# checks for empty places on TicTacToe board
    def test_empty_places(self):
        self.assertEqual(TicTacToe.empty_places(self, [['O', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]), [])
        self.assertEqual(TicTacToe.empty_places(self, [['O', '-', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]), [(0,1)])
        self.assertEqual(TicTacToe.empty_places(self, [['O', '-', 'X'], ['-', 'X', 'O'], ['O', 'X', '-']]), [(0,1),(1,0),(2,2)])
