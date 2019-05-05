from __future__ import print_function
import random
import time
import board

class Player:
	
	turnCount = 0 

	isComputer = False

	def __init__(self, playerType):
		self.isComputer = playerType



	#def checkPiece(self,piece, direction):
	#checkPiece will see if there is a friendly piece in the direction selected.
	#
	# Key for direction:
	#
	#	1	2	3
	#	4	(P)	5
	#	6	7	8
	#
	# Where (P) is the piece 
		
	#	if(direction==1): 
		#upper left diagonol

		
	# 	if(direction==1): 
	# 	#upper left diagonal
			
	# 	elif(direction==2):
	# 	#upper middle

	# 	elif(direction==3):
	# 	#upper right diagonal

	# 	elif(direction==4):
	# 	#left middle

	# 	elif(direction==5):
	# 	#right middle

	# 	elif(direction==6):
	# 	#lower left diagonal

	# 	elif(direction==7):
	# 	#lower middle

	# 	elif(direction==8):
	# 	#lower right

	# 	else:
	# 		return False

	def takeTurn(self):
		if self.isComputer:
			print("Computer's turn...")
			time.sleep(1.5)
		
			#Theoretically, if the Computer is taking the first turn, it could be random.
			if(self.turnCount == 0):
				self.turnCount = self.turnCount + 1

				#return random.choice([1, 2, 3, 4, 5, 6, 7])
				#could be a 'heuristic' to always have the computer drop in the center column (4) if they have the first move
				#According to internet, the only way to win a perfect game is to play that column first... soo optimal?
				return 4
			return random.choice([1,2,3,4,5,6,7])

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
			

		#USER player code below
		#--------------------------------------------------------------
		else:
			#get input from user
				while True:
					n = int(input("enter a number between 1 and 7: "))
					if 1 <= n <= 7:
						break
					print('try again')
			
				self.turnCount = self.turnCount + 1
				return n


if __name__ == '__main__':

	#instantiate board
	theBoard = board.Board()

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
		