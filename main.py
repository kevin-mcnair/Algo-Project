
def printBoard():
	print("_______________")

	for x in range(0,6):   #printing the rows
		for y in range(0,8): #printing the columns
				if((x == 5) and (y != 7)):
					print("|", end="\u0332") #underlines the space characters on the last row 
				else:
					print("|", end=" ")
			 	#INSERT BOARD DATA HERE

		print()
	




if __name__ == '__main__':
	
	printBoard()