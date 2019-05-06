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

	def gameIsOver(self):
		self.gameOver = True

		if(self.checkForTie() == True):
			print("Draw!")
			print("Game Over.")
		else:
			print("Game Over.")

	#returns boolean, TRUE if 4 of same piece are found 
	def checkForWin(self):

		return self.gameOver
	#returns boolean, false if no 4 pieces found 
	# def checkForWin(self):
	# 	rows = len(self.grid)
	# 	columns = len(self.grid[0])

	# 	for i in range(len(self.grid)):
	# 		for j in range(len(self.grid[i])):
	# 			for dr, dc in self.directions:
	# 				win = True
	# 				for length in range(1, 4):
	# 					r = i + dr*length
	# 					c = j + dc*length

	# 				if win:
	# 					return True
	# 	return False
				

	# def checkPiece(self, row, column, length):
	# 	rows = len(self.grid)
	# 	columns = len(self.grid[0])

	# 	for dr, dc in self.directions:
	# 		foundWinner = True

	# 		for i in range(1, length):
	# 			r = row + dr*i
	# 			c = column + dc*i

	# 			if r not in range(rows) or c not in range(columns):
	# 				foundWinner = False
	# 				break

	# 			if self.grid[r][c] != self.grid[row][column]:
	# 				foundWinner = False
	# 				break

	# 		if foundWinner:
	# 			return True

	# 	return False
	# @KEVIN THIS IS THE STUFF I WaS WORKING ON	


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

	def doesSquareContainWinner(self, x, y):
			print("Searching... (" + x + ',' + y + ")")
			return True 

	#returns boolean, TRUE if 4 of same piece are found 
	def checkForWin(self):
		for row in range(len(self.grid), 0, -1):
			for col in range(len(self.grid[row-1])):
				if(str(self.grid[row-1][col]) == ' '):
					continue
				else:
					self.doesSquareContainWinner(row-1, col)
		return False
	
	def checkVertical(self,x,y):
		token = self.grid[x][y]
		count = 0

		for i in range(0,5):

			if(self.grid[i][y].character == token.character and self.grid[x][y] != " "):
				count = count + 1
			else:
				count = 0

			if(count >= 4):
				return True

		return False