import time
from models.sudoku import Sudoku


all_options = {str(i) for i in range(1, 10)}

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
    print('Is valid solution: ', sudoku.valid_sudoku(board, all_options))