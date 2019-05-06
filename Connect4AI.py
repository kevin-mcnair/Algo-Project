import random
import board

class AI: 
    def chosenColumn(self, theBoard):

        #check to see if there are a lot of 0's in the first row
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
            print('Total consecutive Os in col ' + str(col))
            print(totalOs)
            if totalOs >= 3:
                print("Making move based on Os" + str(col))
                return col

        return random.choice([0,1,2,3,4,5,6])