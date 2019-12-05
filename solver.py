#A suduko solver with Backtracking

class Sudoku_Solver:
    def __init__ (self,sudoku):
        self.grid = [[0 for x in range(9) for y in range(9)]]
        self.grid = sudoku
        self.curr = [0,0]


    def EmptyFinder(self):
        for row in range (9):
            for col in range(9):
                if (self.grid[row][col]==0):
                    self.curr =  [row,col]
                    return True
        return False


    def inRow (self, row, num):
        for j in range(9):
            if(self.grid[row][j] == num):
                return True
        return False


    def inCol (self, col, num):
        for i in range(9):
            if self.grid[i][col] == num:
                return True
        return False        


    def inBox (self, row, col, num):
        r = row - row%3
        c = col - col%3
        for i in range(3):
            for j in range(3):
                if (self.grid[i+r][j+c]==num):
                    return True
        return False


    def isSafe(self,row,col,num):
        return not self.inRow( row, num) and not self.inCol(col, num) and not self.inBox (row, col, num)


    def solveSudoku (self):
        
        self.curr = [0,0]

        if (not self.EmptyFinder()):
            return True

        row = self.curr[0]
        col = self.curr[1]

        for num in range(1,10):
            if self.isSafe(row,col,num):
                self.grid[row][col]=num
                if self.solveSudoku():
                    return True

                self.grid[row][col] = 0

        return False


    def printSudoku (self):
        for i in range(9):
            print (self.grid[i])


if __name__ == "__main__":
    sudoku = [[0 for x in range(9) for y in range(9)]]

    sudoku =[[3,0,6,5,0,8,4,0,0], 
             [5,2,0,0,0,0,0,0,0], 
             [0,8,7,0,0,0,0,3,1], 
             [0,0,3,0,1,0,0,8,0], 
             [9,0,0,8,6,3,0,0,5], 
             [0,5,0,0,9,0,6,0,0], 
             [1,3,0,0,0,0,2,5,0], 
             [0,0,0,0,0,0,0,7,4], 
             [0,0,5,2,0,6,3,0,0]]

    MySudoku = Sudoku_Solver(sudoku)
    if(MySudoku.solveSudoku()):
        MySudoku.printSudoku()
    else:
        print("No Solution found")