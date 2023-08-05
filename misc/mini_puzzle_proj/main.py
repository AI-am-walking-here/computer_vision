from board import GameBoard
from display import Display
from pieces import pieces

# Initial Variables
BOARD_WIDTH = 11
BOARD_HEIGHT = 5
pieces_avaliable = ['A','B','C','D','E','F','G','H','I','J','K','L',]

# Initialize a GameBoard + Display Class instance
game_board = GameBoard(BOARD_WIDTH, BOARD_HEIGHT)
display = Display(game_board.board_matrix)  # Pass the board matrix to Display

print(game_board.can_piece_fit("a",1,1))

# Print the Board
display.print_display()