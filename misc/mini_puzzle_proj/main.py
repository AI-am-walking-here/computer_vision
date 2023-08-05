from board import GameBoard
from display import Display


BOARD_WIDTH = 11
BOARD_HEIGHT = 5


# Initialize a GameBoard + Display Class instance
game_board = GameBoard(BOARD_WIDTH, BOARD_HEIGHT)

display = Display(game_board.board_matrix)  # Pass the board matrix to Display



display.print_display()