import heapq

class Sudoku:
    
    def line_options(self, i, board) -> set:
        options = set();
        for j in range(len(board[i])):
            if self.notEmpty(board[i][j]):
                options.add(board[i][j])
        return options;
    
    def col_options(self, i, board) -> set:
        options = set();
        for j in range(len(board)):
            if self.notEmpty(board[j][i]):
                options.add(board[j][i])
        return options;
    
    def unitOptions(self, i_start, j_start, board, li = False):
        options = set()
        for i in range(3*i_start, 3*(i_start + 1)):
            for j in range(3*j_start, 3*(j_start + 1)):
                if self.notEmpty(board[i][j]):
                    options.add(board[i][j])
        return options
                
    def notEmpty(self,position):
        return position != '.'
    
    def options_of(self, i, j ,board, all_options):
        lineExclusion = self.line_options(i, board)
        colExclusion = self.col_options(j, board)
        unitExclusion = self.unitOptions(i//3, j//3, board)
        options = all_options - lineExclusion - colExclusion - unitExclusion
        return options
    
    def updatePaths(self,i_start ,j_start ,board, all_options):
        for i in range(len(board)):
            if not self.notEmpty(board[i][j_start]):
                options = self.options_of(i, j_start, board, all_options)
                if len(options) == 1:
                    board[i][j_start] = options.pop()
                    self.updatePaths(i, j_start, board, all_options)
                        
        for j in range(len(board[i_start])):
            if not self.notEmpty(board[i_start][j]):
                options = self.options_of(i_start, j, board, all_options)
                if len(options) == 1:
                    board[i_start][j] = options.pop()
                    self.updatePaths(i_start, j, board, all_options)
        
        
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        all_options = {str(i) for i in range(1, 10)}
        restart = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if not self.notEmpty(board[i][j]):
                    options = self.options_of(i, j, board, all_options)
                    if len(options) == 1:
                        board[i][j] = options.pop()
                        self.updatePaths(i, j ,board, all_options)
        
        
        positions = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if not self.notEmpty(board[i][j]):
                    options = self.options_of(i, j, board, all_options)
                    positions.append((len(options),i,j))
        heapq.heapify(positions)
        self.solveEmpty(positions, all_options, board)
        
    def solveEmpty(self, positions, all_options, board):
        if self.validSudoku(board, all_options):
            return True
        _, i, j = heapq.heappop(positions)
        options = self.options_of(i, j, board, all_options)
        for option in options:
            board[i][j] = option
            if self.solveEmpty(positions, all_options, board):
                return True
        else:
            board[i][j] = '.'
            heapq.heappush(positions, (len(options), i, j))
            
    def validSudoku(self,board, all_options):
        
        for i in range(len(board)):
            line = set()
            for j in range(len(board[i])):
                if board[i][j] in line:
                    return False
                elif board[i][j] != '.':
                    line.add(board[i][j])
                    
        for j in range(len(board[0])):
            col = set()
            for i in range(len(board)):
                if board[i][j] in col:
                    return False
                elif board[i][j] != '.':
                    col.add(board[i][j])

        for i in range(3):
            for j in range(3):
                if len(all_options) != len(self.unitOptions(i, j, board)):
                    return False
        return True
