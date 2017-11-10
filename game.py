from collections import namedtuple, Counter
import time
import random
import sys

Cell = namedtuple('Cell', ['x', 'y'])
X = 10
Y = 10

# Constants
WHITE_SPACE = u"\u25A1"
FILLED_SPACE = u"\u25A0"
CLEAR_SCREEN = "\033[2J\033[1;1H"
NEW_LINE = '\n'


def get_neighbor_cells(cell, is_bounded=True):
    """
    This is a generator function that yields results of the neighbors
    :param cell: named tuple
    :param is_bounded: boolean default to True
    """
    for y in range(cell.y - 1, cell.y + 2):
        for x in range(cell.x - 1, cell.x + 2):
            if (x, y) != (cell.x, cell.y):
                # Handling for the bounded option
                if is_bounded:
                    if (0 <= x <= X) and (0 <= y <= Y):
                        yield Cell(x, y)
                else:
                    yield Cell(x, y)


def get_neighbor_count(board, is_bounded=True):

    """
    This is the most important function of the program to check each alive cell to find neighbors
    :param board: set with named tuples
    :param is_bounded: boolean default to True
    :return: a Count object with counts for each named tuple
    """
    neighbor_counts = Counter()
    for cell in board:
        for neighbor in get_neighbor_cells(cell, is_bounded):
            neighbor_counts[neighbor] += 1

    return neighbor_counts


def generate_next_board(board):
    """
    Generate the next board based on the neighbor counts from alive cells
    :param board: set with named tuples
    :return: a new set with the alive cells
    """
    new_board = set()
    neighbors = get_neighbor_count(board)
    for cell, count in neighbors.items():
        """
        Game rules:
        A cell generates if it has three neighbors
        An alive cell remains if it has two neighbors
        """
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)

    return new_board


def generate_initial_board(X=10, Y=10):

    """
    Generates the intial set for the board
    :param X: positive integer
    :param Y: positive integer
    :return: set with named tuples
    """
    board = set()
    for row in range(Y):
        for column in range(X):
            if random.randrange(2) == 1:
                board.add(Cell(int(column), int(row)))

    return board


def board_to_display(board, column, row):
    """
    Makes a string for display on the console
    :param board: set with named tuples
    :param column: positive integer
    :param row: positive integer
    :return: string with whitespace stripped
    """
    board_string = ""

    for y in range(row):
        for x in range(column):
            if Cell(x, y) in board:
                board_string += FILLED_SPACE
            else:
                board_string += WHITE_SPACE

        board_string += NEW_LINE

    return board_string.strip()


if __name__ == '__main__':

    try:
        X = int(sys.argv[1])
        Y = int(sys.argv[2])

        time.sleep(5)

        if X <= 2 or Y <= 2:
            raise ValueError


    except IndexError:
        X = 10
        Y = 10
        print("No values entered. Using default values of {} and {}".format(X, Y))
        time.sleep(1)

    except ValueError:

        try:
            print("Acceptable values are positive integers greater than 1!")
            X = int(input("Enter the number of columns: "))
            Y = int(input("Enter the number of rows: "))

            if X <= 2 or Y <= 2:
                raise ValueError

        except ValueError:
            print("You tried! The system will pick now")
            time.sleep(1)
            X = random.randrange(25)
            Y = random.randrange(25)

    f = generate_initial_board(X, Y)
    is_bounded = True

    for generations in range(20):
        f = generate_next_board(f)

        print(CLEAR_SCREEN)

        print(board_to_display(f, X, Y))

        time.sleep(0.1)
