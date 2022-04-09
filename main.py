from sudoku import Solver
import os
import time



def display(board):
    for line in board:
        for element in line:
            print(element, end=' ')
        print()

TEST_FOLDER = 'tests'
all_options = {str(i) for i in range(1, 10)}

for test in os.listdir('tests'):
    print('\n\nSudoku puzzle')
    with open(os.path.join(TEST_FOLDER, test)) as file:
        board = []
        for line in file:
            board.append(line.strip().split(' '))
        display(board)
        solver = Solver()
        start = time.time()
        solver.solveSudoku(board)
        end = time.time()
        print('Solved: ~', end - start)
        display(board)

        print('Is valid solution? ', solver.validSudoku(board, all_options))
    