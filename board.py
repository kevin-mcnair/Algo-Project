class Board:

	grid = [[]]
	gameOver = False
	#this is a list that keeps track of how many pieces are each column
	#makes sure the pieces get inserted at the "top" of each stack
	colCounters = []

	def __init__(self):
		self.grid = [[" " for x in range(7)] for y in range(6)]
		self.gameOver = False
		self.colCounters = [0,0,0,0,0,0,0]

	def addPiece(self, col, player):
		#make sure they don't go over the height of the board
		column = col-1

		if self.colCounters[column]<6:
			if player.isComputer:
				#Computer gets X
				self.grid[self.colCounters[column]][column] = "X"
			else:
				#User gets O
				self.grid[self.colCounters[column]][column] = "O"
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

	#returns boolean, false if no 4 pieces found 
	def checkForWin(self):
		return self.gameOver

	def takeTurn(self, thePlayer):
		success = False
		while success == False:
			chosenCol = thePlayer.takeTurn()
			success = self.addPiece(chosenCol, thePlayer)
