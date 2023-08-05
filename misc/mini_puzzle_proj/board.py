import random
import time
from pieces import *


class GameBoard:
    def __init__(self, width, height):
        self.board_matrix = self.create_board(width, height)
        

    def create_board(self, width, height):
        board_matrix = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append('.')
            board_matrix.append(row)
        return board_matrix

    def can_piece_fit(self, board_matrix, piece, x, y):
        try:
            for r, row in enumerate(piece):
                for c, spot in enumerate(row):
                    if spot != '.':
                        if board_matrix[r + y][c + x] != '.':
                            return False
            return True
        
        except IndexError:
            return False

    def place_piece(self, board_matrix, piece, x, y):
        try:
            for r, row in enumerate(piece):
                for c, spot in enumerate(row):
                    if spot != '.':
                        board_matrix[r + y][c + x] = spot
            return board_matrix
        except IndexError:
            print(f'Couldn\'t place piece at ({x} {y})')
            return board_matrix
        
    def remove_piece(self, board_matrix, piece, x, y):
        try:
            for r, row in enumerate(piece):
                for c, spot in enumerate(row):
                    if spot != '.':
                        board_matrix[r + y][c + x] = '.'
            return board_matrix
        except IndexError:
            print(f'Couldn\'t remove piece at ({x} {y})')
            return board_matrix


    def find_solutions(self,board_matrix, pieces_left):
        # Brute force every possible combination
        if not pieces_left:
            display(board_matrix)
            return True

        piece = pieces_left[0]
        pieces_left.remove(piece)
        found_solution = False  # Flag to track if a solution is found

        for rotation in pieces[piece]:
            for x in range(len(board_matrix[0])):
                for y in range(len(board_matrix)):
                    if can_piece_fit(board_matrix, rotation, x, y):
                        place_piece(board_matrix, rotation, x, y)
                        display(board_matrix)
                        time.sleep(.01)
                        if find_solutions(board_matrix, pieces_left):
                            found_solution = True
                            break
                            
                        remove_piece(board_matrix, rotation, x, y)

                if found_solution:
                    break

            if found_solution:
                break

        pieces_left.append(piece)
        return found_solution


def main():
    board_width = 11
    board_height = 5
    board = create_board(board_width, board_height)
    pieces_left = ['A','B','C','D','E','F','G','H','I','J','K','L',]
    board = [
        ['E', 'K', 'K', 'H', 'D', 'D', 'D', 'D', '.', '.', '.', ],
        ['E', 'K', 'K', 'H', 'H', 'D', 'G', '.', '.', '.', '.', ],
        ['E', 'E', 'F', 'F', 'H', 'H', 'G', '.', '.', '.', '.', ],
        ['I', 'E', 'I', 'F', 'G', 'G', 'G', '.', '.', '.', '.', ],
        ['I', 'I', 'I', 'J', 'J', 'J', 'J', '.', '.', '.', '.', ],
    ]
    pieces_left = ['A','B','C','L']
    find_solutions(board, pieces_left)

if __name__ == '__main__':
    main()