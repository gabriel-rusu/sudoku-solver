import time
from models.sudoku import Sudoku

def display(board):
    for line in board:
        for element in line:
            print(element, end=' ')
        print()


def solve(file):
    print('\n\nSudoku board to solve:')
    sudoku = Sudoku()
    board = sudoku.read_board(file)
    display(board)
    start = time.time()
    sudoku.solveSudoku(board)
    end = time.time()
    print('Solved board: ~', int((end - start)*100), 'ms')
    display(board)