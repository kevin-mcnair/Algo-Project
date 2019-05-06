class Piece(object):
    character = ''
    isComputer = False

    # The class "constructor" - It's actually an initializer 
    def __init__(self, isComputer, major):
        if(isComputer):
            self.isComputer = True
            self.character = 'X'
        
        else:
            self.isComputer = False
            self.character = 'O'

        
