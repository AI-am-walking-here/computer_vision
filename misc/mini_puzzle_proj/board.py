import random
import time
from pieces import *


class GameBoard:
    def __init__(self):
        self.create_board(11,5)

    def create_board(width, height):
        board = []
        for _ in range(height):
            section = []
            for _ in range(width):
                section.append('.')
            board.append(section)
        return board

    def can_piece_fit(board, piece, x, y):
        try:
            for r, row in enumerate(piece):
                for c, spot in enumerate(row):
                    if spot != '.':
                        if board[r + y][c + x] != '.':
                            return False
            return True
        
        except IndexError:
            return False

    def place_piece(board, piece, x, y):
        try:
            for r, row in enumerate(piece):
                for c, spot in enumerate(row):
                    if spot != '.':
                        board[r + y][c + x] = spot
            return board
        except IndexError:
            print(f'Couldn\'t place piece at ({x} {y})')
            return board
        
    def remove_piece(board, piece, x, y):
        try:
            for r, row in enumerate(piece):
                for c, spot in enumerate(row):
                    if spot != '.':
                        board[r + y][c + x] = '.'
            return board
        except IndexError:
            print(f'Couldn\'t remove piece at ({x} {y})')
            return board

    def display(board):
        print()
        count = 0
        for row in board:
            for spot in row:
                if spot == '.':
                    count += 1
                print(spot, end=' ')
            print()
        print(f'Spots left: {count}')
        if count == 0:
            print('Congrats!')


    def find_solutions(board, pieces_left):
        # Brute force every possible combination
        if not pieces_left:
            display(board)
            return True

        piece = pieces_left[0]
        pieces_left.remove(piece)
        found_solution = False  # Flag to track if a solution is found

        for rotation in pieces[piece]:
            for x in range(len(board[0])):
                for y in range(len(board)):
                    if can_piece_fit(board, rotation, x, y):
                        place_piece(board, rotation, x, y)
                        display(board)
                        time.sleep(.01)
                        if find_solutions(board, pieces_left):
                            found_solution = True
                            break
                            
                        remove_piece(board, rotation, x, y)

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