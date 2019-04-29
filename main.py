import random

class Board:

	grid = [[]]
	gameOver = False

	def __init__(self):
		self.grid = [[(0,0) for x in range(6)] for y in range(7)]
		self.gameOver = False

	def addPiece(self, row, col):
		print("Add Piece")

	def printBoard(self):
		print("printBoard")

	def isGameOver(self):
		return self.gameOver

	def gameIsOver(self):
		self.gameOver = True

	def checkForWin(self):
		return False

class Player:

	isComputer = False

	def __init__(self, playerType):
		self.isComputer = playerType

	def takeTurn(self):
		if self.isComputer:
			#insert algorithm here bois
			print("I am a computer")
		else:
			#get input from user
			print("I am a user")

if __name__ == '__main__':

	#instantiate board
	theBoard = Board()

	#instantiate two new player objects
	player = Player(False)
	computer = Player(True)

	print("Welcome to Connect 4!")
	print("Flipping coin to see who goes first...")
	#generate either true or false, if the coin is true, the computer goes first
	coin = random.choice([True, False])
	print(coin)

	#if computer goes first, let the computer take its turn, otherwise don't do anything
	if coin:
		#computer takes turn first
		computer.takeTurn()

	#start while loop with condition gameOver
	while(theBoard.gameOver == False):
		#print board
		theBoard.printBoard()
		#player takes turn
		player.takeTurn()
		#print board
		theBoard.printBoard()
		#check for win
		gameHasBeenWon = theBoard.checkForWin()
		#if win, break
		if gameHasBeenWon:
			break
		#otherwise, computer takes turn
		computer.takeTurn()
		#print board again
		theBoard.printBoard
		#check for win
		gameHasBeenWon = theBoard.checkForWin()
		#if win, break
		if gameHasBeenWon:
			break