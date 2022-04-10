from models.sudoku import Sudoku
import os
import time



def display(board):
    for line in board:
        for element in line:
            print(element, end=' ')
        print()

TEST_FOLDER = 'solver/tests/data'
all_options = {str(i) for i in range(1, 10)}

for test in os.listdir(TEST_FOLDER):
    print('\n\nSudoku puzzle')
    with open(os.path.join(TEST_FOLDER, test)) as file:
        board = []
        for line in file:
            board.append(line.strip().split(' '))
        display(board)
        solver = Sudoku()
        start = time.time()
        solver.solveSudoku(board)
        end = time.time()
        print('Solved: ~', int((end - start) * 1000), 'ms')
        display(board)

        print('Is valid solution? ', solver.validSudoku(board, all_options))
    