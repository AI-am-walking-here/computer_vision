from board import GameBoard
from display import Display
from pieces import pieces
from piece_functions import *



# Global Variables
BOARD_WIDTH = 11
BOARD_HEIGHT = 5


# Initial Variables
pointer_location = (1,1)
pieces_avaliable = ['A','B','C','D','E','F','G','H','I','J','K','L',]
chosen_piece_label = pieces_avaliable[0] # Defaults to what is left
current_piece = pieces[chosen_piece_label] # Uses the 'label' to search in the pieces dictionary for the np array


# Initialize a GameBoard + Display Class instance
game_board = GameBoard(BOARD_WIDTH, BOARD_HEIGHT)
display = Display(game_board.board_matrix)  # Pass the board matrix to Display


print(game_board.can_piece_fit(current_piece, pointer_location))


# Print the Board
display.print_display()