from __future__ import print_function
import random
import time

class Board:

	grid = [[]]
	gameOver = False
	#this is a list that keeps track of how many pieces are each column
	#makes sure the pieces get inserted at the "top" of each stack
	colCounters = [0,0,0,0,0,0]

	def __init__(self):
		self.grid = [[" " for x in range(6)] for y in range(7)]
		self.gameOver = False

	def addPiece(self, col, player):
		#make sure they don't go over the height of the board
		if self.colCounters[col-1]<=6:
			if player.isComputer:
				#Computer gets X
				self.grid[self.colCounters[col-1]][col-1] = "X"
			else:
				#User gets O
				self.grid[self.colCounters[col-1]][col-1] = "O"
			#increment the counter for that column
			self.colCounters[col-1] = self.colCounters[col-1] + 1
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
		print("|1|2|3|4|5|6| ")

	def gameIsOver(self):
		self.gameOver = True

	def checkForWin(self):
		return self.gameOver

	def takeTurn(self, thePlayer):
		success = False
		while success == False:
			chosenCol = thePlayer.takeTurn()
			success = self.addPiece(chosenCol, thePlayer)

class Player:
	
	turnCount = 0 

	isComputer = False

	def __init__(self, playerType):
		self.isComputer = playerType

	def takeTurn(self):
		if self.isComputer:
			print("Computer's turn...")
			time.sleep(1.5)
		
			#Theoretically, if the Computer is taking the first turn, it could be random.
			if(self.turnCount == 0)
				self.turnCount = self.turnCount + 1
				return random.choice([1, 2, 3, 4, 5, 6])


			#**************************************************************
			#IMPORTANT
			#insert algorithm here bois instead of the random number choice
			#have it return the number of the row that it chooses to play in
			#
			#Priorities (from our outline):
			#-Place block for win (which means we need to be able to look at the blocks around it)
			#-Place to block player win (in this order):
			#	- Vertical
			#	-Diagonal									
			#	-Horizontal
			#	- Below Diagonal
			#	- Below Disconnected
			#
			#	Do we need to make the computer recognize these different situations?
			#	- place own block to continue
			#***************************************************************
			
		else:
			#get input from user
			userInput = input("Your turn! Which row would you like to drop your piece in (1-6)?: ")
			while userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 5 and userInput != 6:
				userInput = input("Please enter a row on the board: ")
			self.turnCount = self.turnCount + 1
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

	#if computer goes first, let the computer take its turn, otherwise don't do anything
	if coin:
		#computer takes turn first
		print("")
		print("Computer goes first...")
		print("")
		time.sleep(.5)
		theBoard.takeTurn(computer)
		#print board
		theBoard.printBoard()

	else:
		print("")
		print("You go first...")
		print("")
		time.sleep(.5)

		#print board
		theBoard.printBoard()

	#start while loop with condition gameOver
	while(theBoard.gameOver == False):
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

		#**************************************************************
		#IMPORTANT
		#as of right now, the game doesn't end
 		#Board's checkForWin method will have to be altered to actually check for a win
		#this will need to be done by checking for any 4 adjacent pieces on the board
		#***************************************************************
		