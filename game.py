from collections import namedtuple, Counter
import time
import random
import sys

Cell = namedtuple('Cell', ['x', 'y'])

# Constants
WHITE_SPACE = u"\u25A1"
FILLED_SPACE = u"\u25A0"
CLEAR_SCREEN = "\033[2J\033[1;1H"
NEW_LINE = '\n'


def get_neighbor_cells(cell, bounded):
    # This is a generator and will hold the neighbors created until the end
    for y in range(cell.y - 1, cell.y + 2):
        for x in range(cell.x - 1, cell.x + 2):
            # Check to make sure that the tuple generated is not equal to the cell passed to the function
            if (x, y) != (cell.x, cell.y):
                # Handling for the bounded option
                # All cells generated need to be positive and less than or equal to the matrix
                if bounded:
                    if (0 <= x <= X) and (0 <= y <= Y):
                        yield Cell(x, y)
                else:
                    yield Cell(x, y)


def get_neighbor_count(board):
    # The checks all of the Alive cells and finds their neighbors
    neighbor_counts = Counter()
    for cell in board:
        # call to the generator
        for neighbor in get_neighbor_cells(cell, is_bounded):
            neighbor_counts[neighbor] += 1

    return neighbor_counts


def generate_next_board(board):
    new_board = set()
    # Get the dict key and value at once
    neighbors = get_neighbor_count(board)
    for cell, count in neighbors.items():
        # A cell generates if it has three neighbors
        # An alive cell remains if it has two neighbors
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)

    return new_board


def generate_initial_board(x, y):
    # default values or x=8, y=6
    board = set()
    for row in range(y):
        for column in range(x):
            if random.randrange(2) == 1:
                board.add(Cell(int(column), int(row)))

    return board


def board_to_display(board, column, row):
    # Start with an empty string
    board_string = ""

    # Order must be row then column
    for y in range(row):
        for x in range(column):
            if Cell(x, y) in board:
                board_string += FILLED_SPACE
            else:
                board_string += WHITE_SPACE

        # After the last column insert a new line character
        board_string += NEW_LINE

    # String out extra white space characters
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
        print("Acceptable values are positive integers greater than 1!")
        X = int(input("Enter the number of columns"))
        Y = int(input("Enter the number of rows"))

f = generate_initial_board(X, Y)
is_bounded = True

for generations in range(20):
    # Input the current board and return the updated board as a Set()
    f = generate_next_board(f)

    # Clear the screen
    print(CLEAR_SCREEN)

    # Display the board
    print(board_to_display(f, X, Y))

    # Sleep for a 100ms
    time.sleep(0.1)
