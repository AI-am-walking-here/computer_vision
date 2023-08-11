import pygame
from board import GameBoard
from pieces import Piece
from pointer import Pointer

class Game:
    def __init__(self, game_board, pointer, current_piece):
        self.game_board = game_board
        self.pointer = pointer
        self.current_piece = current_piece
        pygame.init()
        self.window_size = 500
        self.window = pygame.display.set_mode((self.window_size, self.window_size))
        self.cell_size = self.window_size // game_board.width

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()
            pygame.display.flip()

        pygame.quit()

    def draw(self):
        for y, row in enumerate(self.game_board.board_matrix):
            for x, spot in enumerate(row):
                color = (255, 255, 255) if spot == '.' else (255, 0, 0)
                pygame.draw.rect(self.window, color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))