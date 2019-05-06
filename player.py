import time
import random
import board

class Player:
	board = board.Board()
	player = ""
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
			if(self.turnCount == 0 and len(self.board.grid) == 0 ):
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
			#test

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