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
			
			if(self.turnCount == 0 and board.isBoardEmpty() or str(board.grid[0][3]) == ' '):
				self.turnCount = self.turnCount + 1

				#According to internet, the only way to win a perfect game is to play the 4th column first... soo optimal?
				return 4
			return self.computerLogic.chosenColumn(board)+1


			
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
