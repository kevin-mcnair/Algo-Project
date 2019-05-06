import random
import board

class AI: 
    def chosenColumn(self, theBoard):

        #first checks to see if it can win
        try:
            for y in range(0, 5):
                for x in range(0, 6):
                    if theBoard.grid[x][y] == ' ':
                        continue
                    if theBoard.grid[x][y].character == "X":
                        if str(theBoard.grid[x][y+1]) == "X":
                            if str(theBoard.grid[x][y+2]) == "X":
                                return y+3
                        elif str(theBoard.grid[x][y-1]) == "X":
                            if str(theBoard.grid[x][y-2]) == "X":
                                return y-3
                        elif str(theBoard.grid[x+1][y]) == "X":
                            if str(theBoard.grid[x+2][y]) == "X":
                                return y
                
        except IndexError:
            print("Out of bounds")
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

            return random.choice([0,1,2,3,4,5,6])