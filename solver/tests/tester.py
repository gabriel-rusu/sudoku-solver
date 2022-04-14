from models.sudoku import Sudoku
import os
import time
from utils.tools import solve

TEST_FOLDER = 'solver/tests/data/'
all_options = {str(i) for i in range(1, 10)}


def run_tests(test_no=-1):
    for test in os.listdir(TEST_FOLDER):
        with open(os.path.join(TEST_FOLDER, test)) as file:
            if test_no == -1 or str(test_no) in file.name:
                solve(file)