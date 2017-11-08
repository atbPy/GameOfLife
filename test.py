from game import (
    Cell, get_neighbor_cells, get_neighbor_count,
    generate_next_board, generate_initial_board, board_to_display)
import unittest
from collections import namedtuple, Counter


class GameOfLifeTest(unittest.TestCase):
    def test_get_neighbor_cells(self):
        cell = Cell(1, 1)
        expected = set([
            Cell(0, 0), Cell(0, 1), Cell(0, 2),
            Cell(1, 0), Cell(1, 2), Cell(2, 0),
            Cell(2, 1), Cell(2, 2)])
        actual = set(get_neighbor_cells(cell))
        self.assertEqual(expected, actual)

    def test_get_neighbor_count(self):
        board = set([Cell(0, 0), Cell(1, 1)])
        expected = Counter({Cell(x=1, y=0): 2,
                            Cell(x=0, y=1): 2,
                            Cell(x=1, y=1): 1,
                            Cell(x=0, y=0): 1,
                            Cell(x=2, y=0): 1,
                            Cell(x=2, y=1): 1,
                            Cell(x=0, y=2): 1,
                            Cell(x=1, y=2): 1,
                            Cell(x=2, y=2): 1})
        actual = get_neighbor_count(board)
        self.assertEqual(expected, actual)

    def test_empty_generate_next_board(self):
        board = set([Cell(0, 0), Cell(1, 0)])
        actual = generate_next_board(board)
        expected = set()
        self.assertEqual(expected, actual)

    def test_generate_next_board(self):
        board = set([Cell(0, 0), Cell(1, 0), Cell(1, 1)])
        actual = generate_next_board(board)
        expected = set([Cell(x=0, y=0), Cell(x=1, y=0), Cell(x=1, y=1), Cell(x=0, y=1)])
        self.assertEqual(expected, actual)

    def test_persistent_square(self):
        board = set([Cell(0, 0), Cell(1, 0), Cell(0, 1), Cell(1, 1)])
        actual = generate_next_board(board)
        expected = set([Cell(x=0, y=0), Cell(x=1, y=0), Cell(x=1, y=1), Cell(x=0, y=1)])
        self.assertEqual(expected, actual)

    def test_blink_line(self):
        board = set([Cell(1, 0), Cell(1, 1), Cell(1, 2)])
        actual = generate_next_board(board)
        expected = set([Cell(x=1, y=1), Cell(x=0, y=1), Cell(x=2, y=1)])
        self.assertEqual(expected, actual)


    def test_board_to_display(self):
        board = set([Cell(0, 0), Cell(1, 0), Cell(0, 1), Cell(1, 1)])
        actual = board_to_display(board, 10, 10)
        expected = "■■□□□□□□□□\n■■□□□□□□□□\n□□□□□□□□□□\n□□□□□□□□□□\n□□□□□□□□□□\n" \
                   "□□□□□□□□□□\n□□□□□□□□□□\n□□□□□□□□□□\n□□□□□□□□□□\n□□□□□□□□□□"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()