import random
import time

class Board:

	grid = [[]]
	gameOver = False

	def __init__(self):
		self.grid = [[(0,0) for x in range(6)] for y in range(7)]
		self.gameOver = False

	def addPiece(self, row):
		print("Add Piece")

	def printBoard(self):
		print("printBoard")

	def gameIsOver(self):
		self.gameOver = True

	def checkForWin(self):
		return self.gameOver

	def takeTurn(self, thePlayer):
		chosenRow = thePlayer.takeTurn()
		self.addPiece(chosenRow)

class Player:

	isComputer = False

	def __init__(self, playerType):
		self.isComputer = playerType

	def takeTurn(self):
		if self.isComputer:
			#insert algorithm here bois instead of the random number
			#have it return the number of the row that it chooses to play in
			print("Computer's turn...")
			time.sleep(2)
			return random.choice([1, 2, 3, 4, 5, 6, 7])
		else:
			#get input from user
			userInput = input("Your turn! Which row would you like to drop your piece in (1-6)?: ")
			while userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 5 and userInput != 6 and userInput != 7:
				userInput = input("Please enter a row on the board: ")
			return userInput


if __name__ == '__main__':

	#instantiate board
	theBoard = Board()

	#instantiate two new player objects
	player = Player(False)
	computer = Player(True)

	print("----------------------")
	print("Welcome to Connect 4!")
	print("----------------------")
	print("Flipping coin to see who goes first...")
	#generate either true or false, if the coin is true, the computer goes first
	coin = random.choice([True, False])
	print(coin)

	#if computer goes first, let the computer take its turn, otherwise don't do anything
	if coin:
		#computer takes turn first
		print("Computer goes first...")
		time.sleep(.3)
		theBoard.takeTurn(computer)

	else:
		print()
		print("You go first...")
		print()

	#start while loop with condition gameOver
	while(theBoard.gameOver == False):
		#print board
		theBoard.printBoard()
		#player takes turn
		theBoard.takeTurn(player)
		#print board
		theBoard.printBoard()
		#check for win
		gameHasBeenWon = theBoard.checkForWin()
		#if win, break
		if gameHasBeenWon:
			theBoard.gameIsOver()
			break
		#otherwise, computer takes turn
		theBoard.takeTurn(computer)
		#print board again
		theBoard.printBoard()
		#check for win
		gameHasBeenWon = theBoard.checkForWin()
		#if win, break
		if gameHasBeenWon:
			theBoard.gameIsOver()
			break

		theBoard.gameIsOver()