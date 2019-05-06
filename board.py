import piece

class Board:

	grid = [[]]
	gameOver = False
	#this is a list that keeps track of how many pieces are each column
	#makes sure the pieces get inserted at the "top" of each stack
	colCounters = []
	directions = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1), ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
	)

	def __init__(self):
		self.grid = [[" " for x in range(7)] for y in range(6)]
		self.gameOver = False
		self.colCounters = [0,0,0,0,0,0,0]

	def addPiece(self, col, player):
		thePiece = piece.Piece(player.isComputer)
		#make sure they don't go over the height of the board
		
		column = col-1
		#Col is the user given value, column is the actual column to be used

		# BOARD CREATION BELOW

		if self.colCounters[column]<6:
			if thePiece.isComputer:
				#Computer gets X
				self.grid[self.colCounters[column]][column] = thePiece
			else:
				#User gets O
				self.grid[self.colCounters[column]][column] = thePiece
			#increment the counter for that column
			self.colCounters[column] = self.colCounters[column] + 1
			return True
		else:
			#only print out the error message for the user
			if player.isComputer == False:
				print("Oops! That column is full! Try again.")
			return False

	def printBoard(self):
		print("______________")
		for row in range(len(self.grid), 0, -1):
			for col in range(len(self.grid[row-1])):
				print("|" + str(self.grid[row-1][col]), end = '')
			print("|")
		print("--------------")
		print("|1|2|3|4|5|6|7| ")

	def gameIsOver(self, player):
		self.gameOver = True

		if(self.checkForTie() == True):
			print("Game Over. It's a Draw!")
		else:
			if(player == 0):
				print("Game Over. Computer Wins!")
			else:
				print("Game Over. Player Wins!")

	def checkForTie(self):
		fullColumns = 0

		for x in range(0,6):
			if(self.colCounters[x] == 6):
				fullColumns = fullColumns + 1

		if(fullColumns==6):
			return True
		else:
			return False

	def takeTurn(self, thePlayer):
		success = False
		while success == False:
			chosenCol = thePlayer.takeTurn(self)
			print(chosenCol)
			success = self.addPiece(chosenCol, thePlayer)

	def isBoardEmpty(self):
		for row in range(len(self.grid), 0, -1):
			for col in range(len(self.grid[row-1])):
				if(str(self.grid[row-1][col]) == ' '):
					continue
				else:
					return False
		return True

	def checkHorizontal(self, x, y, char):
		longestHor = 0
		#print("Searching Horizontal... (" + str(x) + ',' + str(y) + ")")
		try:
			if self.grid[x][y].character == char:
				longestHor = longestHor + 1
				if str(self.grid[x][y+1]) == char:
					longestHor = longestHor + 1
					if str(self.grid[x][y+2]) == char:
						longestHor = longestHor + 1
						if str(self.grid[x][y+3]) == char:
							longestHor = longestHor + 1
							return True
			else:
				print(longestHor)
				return False
		except IndexError:
			return False
	
	def checkDiagonal(self, x, y):
		#print("Searching Diagonal... (" + str(x) + ',' + str(y) + ")")
		return False

	def checkVertical(self,x,y):
		token = self.grid[x][y]
		count = 0
		#print("Searching Vertical... (" + str(x) + ',' + str(y) + ")")

		for i in range(0,5):
			if(str(self.grid[i][y]) == str(token)):
				count = count + 1
			else:
				count = 0

			if(count >= 4):
				return True

		return False

	def doesSquareContainWinner(self, x, y, char):
		#print("Searching... (" + str(x) + ',' + str(y) + ")" + char)
		if(self.checkHorizontal(x, y, char) or self.checkVertical(x, y) or self.checkDiagonal(x, y)):
			return True
		else:
			return False 

	#returns boolean, TRUE if 4 of same piece are found 
	def checkForWin(self):
		for row in range(0, len(self.grid)):
			for col in range(len(self.grid[row-1])):
				if(str(self.grid[row][col]) == ' '):
					continue
				else:
					if(self.doesSquareContainWinner(row, col, self.grid[row][col].character)):
						return True
					continue

		return False
	
	def checkVertical(self,x,y):
		token = self.grid[x][y]
		count = 0
		print("Searching Vertical... (" + str(x) + ',' + str(y) + ")")

		for i in range(0,5):
			#print("Comparison char: " + str(self.grid[x][y]) + " Comparing At: " + "(" +str(i) + ',' + str(y) + ")") 
			#print()
			#print("Count: " + str(count))

			if(str(self.grid[i][y]) == str(token)):
				#print("Char:" + str(self.grid[i][y]))
				count = count + 1
			else:
				
				count = 0

			if(count >= 4):
				return True


		return False