from models.sudoku import Sudoku
import os
import time



def display(board):
    for line in board:
        for element in line:
            print(element, end=' ')
        print()

TEST_FOLDER = 'data'
all_options = {str(i) for i in range(1, 10)}

for test in os.listdir(TEST_FOLDER):
    print('\n\nSudoku puzzle')
    with open(os.path.join(TEST_FOLDER, test)) as file:
        board = []
        for line in file:
            board.append(line.strip().split(' '))
        display(board)
        sudoku = Sudoku()
        start = time.time()
        sudoku.solveSudoku(board)
        end = time.time()
        print('Solved: ~', time.ctime(end - start))
        display(board)

        print('Is valid solution? ', solver.validSudoku(board, all_options))