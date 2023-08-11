from board import GameBoard
from display import Display
from pointer import Pointer
from pieces import Piece




# Global Variables
BOARD_WIDTH = 11
BOARD_HEIGHT = 5


# Initial Variables
pieces_avaliable = ['A','B','C','D','E','F','G','H','I','J','K','L',]
default_label = pieces_avaliable[0] # Defaults to what is left


# Initialize a GameBoard + Display + Pointer Class instance
game_board = GameBoard(BOARD_WIDTH, BOARD_HEIGHT)
display = Display(game_board.board_matrix)  # Pass the board matrix to Display
pointer = Pointer()
current_piece = Piece(default_label)


current_piece.rotate()
print(current_piece)
print(pointer)
game_board.place_piece(current_piece, pointer.position())


# Print the Board
display.print_display()