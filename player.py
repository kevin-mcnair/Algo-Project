import time
import random
import board
import Connect4AI

class Player:
	computerLogic = Connect4AI.AI()
	player = ""
	turnCount = 0 

	isComputer = False

	def __init__(self, playerType):
		self.isComputer = playerType

	def takeTurn(self, board):
		if self.isComputer:
			print("Computer's turn...")
			time.sleep(0.5)
			#Theoretically, if the Computer is taking the first turn, it could be random.
			
			if(self.turnCount == 0 and board.isBoardEmpty()):
				self.turnCount = self.turnCount + 1

				#could be a 'heuristic' to always have the computer drop in the center column (4) if they have the first move
				#According to internet, the only way to win a perfect game is to play that column first... soo optimal?
				return 4
			

			return self.computerLogic.chosenColumn(board)+1


			

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
			#test

		#USER player code below
		#--------------------------------------------------------------
		else:
			#get input from user
				while True:
					try:
						n = int(input("enter a number between 1 and 7: "))
						if 1 <= n <= 7:
							break
						print('try again')
					except KeyboardInterrupt:
						raise
					except:
						print("Please enter a valid number")
						continue
				self.turnCount = self.turnCount + 1
				return n
