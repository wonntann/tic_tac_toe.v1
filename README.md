# tic_tac_toe.v1

STEPS
======
* Create [player.py]()
    * Import libraries
    * Create class for player
        * Computer
        * Human 

* Create [game.py]()
    * Create class for board
        * Print board
        * Use [@staticmethod](https://python-reference.readthedocs.io/en/latest/docs/functions/staticmethod.html) 
        * [Enumerate](https://docs.python.org/3/library/enum.html)

* Add movements to [player.py]()
    * Import libraries
    * Create class framework for player movement 
        * Computer
        * Human 


* Add movements to [player.py]()
    * Fill in move class for player
        * Computer
        * Human 


* Check if make move and win [game.py]()
    * Within the @staticmethod, check for:
        * Available moves
        * Empty squares
        * Non-empty squares

        * Make a move and call in main function to print the game

        * Check the winner
            * Add conditional to make move
            * Call in main function, checking the current_winner and to see if the game should be returned

        * Define the winner
            * Create function to assess the row, column, diagonal 


* Finish up the game:
        
        
            if __name__ == '__main__':
                **** insert function calls **** 
        


    * Import from player.py

    
        from player import HumanPlayer, RandomComputerPlayer
    

    * [Python File Naming Conventions](https://www.freecodecamp.org/news/if-name-main-python-example/)

