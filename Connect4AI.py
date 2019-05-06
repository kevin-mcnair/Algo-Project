import random
import board

class AI: 
    def chosenColumn(self, theBoard):

        #first checks to see if it can win
        for y in range(0, 5):
            for x in range(0, 6):
                if theBoard.grid[x][y] == ' ':
                    continue
                if theBoard.grid[x][y].character == "X":
                    if (y+1) < 6 and str(theBoard.grid[x][y+1]) == "X":
                        if (y+2) < 6 and str(theBoard.grid[x][y+2]) == "X":
                            if (y+3) < 6:
                                return y+3
                    elif (y-1) >= 0 and str(theBoard.grid[x][y-1]) == "X":
                        if (y-2) >= 0 and str(theBoard.grid[x][y-2]) == "X":
                            if (y-3) >= 0:
                                return y-3
                    elif (x+1) < 7 and str(theBoard.grid[x+1][y]) == "X":
                        if (x+2) < 7 and str(theBoard.grid[x+2][y]) == "X":
                            if (x+3) < 7:
                                return y
                    else:
                        continue
            
        #this is a simple blocking algorithm
        totalOs = 0
        for col in range(0, 5):
            totalOs = 0
            for row in range(0, 6):
                if theBoard.grid[row][col] == ' ':
                    continue
                if theBoard.grid[row][col].character == "O":
                    totalOs = totalOs + 1
                else:
                    totalOs = 0
            if totalOs >= 3:
                return col
        
        print("It's getting here")
        return random.choice([0,1,2,3,4,5,6])