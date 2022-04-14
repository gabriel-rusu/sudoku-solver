from models.sudoku import Sudoku
from utils.tools import solve
from tests import tester
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--test', help='Runs a specific test by number or all if -1 is specified:', type=int)
parser.add_argument('--filepath', help='Reads the sudoku board from the specified file path and solves it:', type=str)
parser.parse_args()

args = parser.parse_args()
if args.test:
    tester.run_tests(args.test)
elif args.file:
    solve(open(args.file))

