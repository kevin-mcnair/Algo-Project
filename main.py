
def printBoard():
	print("_______________")

	for x in range(0,6):   #printing the rows
		for y in range(0,8): #printing the columns
				print("|", end=" ")
			 	#INSERT BOARD DATA HERE

		print()
	print("_______________")




if __name__ == '__main__':
	
	printBoard()