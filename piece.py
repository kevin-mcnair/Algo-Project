class Piece:
    character = 'O'
    isComputer = False

    # The class "constructor" - It's actually an initializer 
    def __init__(self, isComputer):
        if(isComputer):
            self.isComputer = True
            self.character = 'X'

    def __str__(self):
        return self.character

