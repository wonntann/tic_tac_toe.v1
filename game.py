import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:

    def __init__(self):
        self.board = self.make_board()  # single list for 3x3 board
        self.current_winner = None # track the winner

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        # getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ', ' | '.join(row), ' |')
    
    # figure which numbers coorespond to each location
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 ...
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] 
        for row in number_board:
            print('| ', ' | '.join(row), ' |')


    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def empty_squares(self):
        return ' ' in self.board # return a boolean

    def num_empty_squares(self):
        return self.board.count(' ') # count the number of spaces on the board


    def make_move(self, square, letter):
        # only move if valid and assign square to letter then return true
        # return false if invalid
        if self.board[square] == ' ':
            self.board[square] = letter

            # add to check the winner, pass in last move
            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False
    
    def winner(self, square, letter):
        # winner conditions
        # winner for a row index
        row_ind = square // 3
        # list of items in the selected row
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]): 
            return True # if all in a row

        # check column index
        col_ind = square % 3
        # add to the column index to get every value in the row and put in list
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]): 
            return True # if all in a row

        # check diagonal index
        # if square is even number (0, 2, 4, 6, 8)
        if square % 2  == 0: # divisible by 2
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]): 
                return True 
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # left to right diagonal
            if all([spot == letter for spot in diagonal2]): 
                return True 
        # if all checks fail, then not true
        return False


# main game loop
def play(game, x_player, o_player, print_game=True):
    # returns winner (the letter) or None if a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter

    """
        iterate while empty squares are present
        default return which breaks out of loop
    """ 

    while game.empty_squares():
        # get move from correct player
        if letter == 'O':
            square = o_player.get_move(game)
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square =x_player.get_move(game)

        # make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter, 'makes a move to square {}'.format(square))
                game.print_board()
                print('') # empty line

            # if current_winner not set then a letter has won and return the game
            if game.current_winner:
                if print_game:
                    print(letter, 'wins!')
                return letter # ends the loop and exits the game

            # alternate letters after make move
            letter = 'O' if letter == 'X' else 'X' # switch players

            """ 
            easier version of line 66:
                if letter == 'X':
                    letter = 'O'
                else:
                    letter = 'X'
            """

        # Add a pause by importing time
        time.sleep(0.8)

    if print_game:             # not in the while loop
        print('It\'s a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe() # instance of TicTacToe()
    play(t, x_player, o_player, print_game=True)
