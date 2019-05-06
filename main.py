from __future__ import print_function
import random
import board
import player
import time


if __name__ == '__main__':

	#instantiate board
	theBoard = board.Board()

	#instantiate two new player objects
	computer = player.Player(True)
	player = player.Player(False)


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
		#check for tie
		tieCheck = theBoard.checkForTie()
		#player takes turn
		theBoard.takeTurn(player)
		#print board
		theBoard.printBoard()

		#check for win
		gameHasBeenWon = theBoard.checkForWin()
		#if win, break

		if gameHasBeenWon or tieCheck:
			if(player.isComputer):
				theBoard.gameIsOver(0)
			else:
				theBoard.gameIsOver(1)
			break

		#check for tie
		tieCheck = theBoard.checkForTie()
		
		#otherwise, computer takes turn
		theBoard.takeTurn(computer)
		#print board again
		theBoard.printBoard()
		
		#check for win
		gameHasBeenWon = theBoard.checkForWin()
		#if win, break

		if gameHasBeenWon or tieCheck:
			if(player.isComputer):
				theBoard.gameIsOver(0)
			else:
				theBoard.gameIsOver(1)
			break

		#**************************************************************
		#IMPORTANT
		#as of right now, the game doesn't end
 		#Board's checkForWin method will have to be altered to actually check for a win
		#this will need to be done by checking for any 4 adjacent pieces on the board
		#***************************************************************
		