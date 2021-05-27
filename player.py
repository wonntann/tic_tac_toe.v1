import math
import random

class Player:

    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    
    # next player move
    def get_move(self, game):
        pass



# computer player
class RandomComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        # get a random valid pot for next move
        square = random.choice(game.available_moves())
        return square


# human player
class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn, Input move 0-9: ')

            """ 
                check if correct value: 
                    try to cast it to an integer
                    if not an integer, say invalid
                    if not available spot, say invalid
            """
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # only if successful
            except ValueError:
                print('Invalid square. Try again.')

        return val