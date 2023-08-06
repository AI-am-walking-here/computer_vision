from pieces import pieces


class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board_matrix = self.create_board(width, height)
        

    def create_board(self, width, height):
        """
        Creates a 2D matrix representing a game board.

        Args:
            width (int): The width of the game board. This parameter dictates the number of columns in the board.

            height (int): The height of the game board. This parameter dictates the number of rows in the board.

        Returns:
            list: A 2D list (matrix) filled with '.' as placeholders, representing an empty game board. Each '.' represents a cell on the board.

        Note:
            This function assumes valid integer inputs for width and height. It does not handle erroneous inputs, negative values, or non-integer types. 

            The game board is initialized with all cells as '.', indicating they're unoccupied. Different symbols may later replace these placeholders to represent game pieces or players.

        """
        board_matrix = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append('.')
            board_matrix.append(row)
        return board_matrix
    
    def can_piece_fit(self, piece, coordinate):
        """
        Checks if a game piece can fit onto the game board at a specific coordinate.

        Args:
            piece (Piece): An instance of the Piece class.
            coordinate (tuple): A tuple representing the coordinates (x, y) on the board where the top-left cell of the piece should be placed.

        Returns:
            bool: Returns True if the game piece can fit at the specified coordinate on the game board without colliding with any existing pieces or going outside the bounds of the board. Returns False otherwise.
        """
        x, y = coordinate  # Unpacking the tuple into x and y
        try:
            for r, row in enumerate(piece.array): # r is index and row is item
                for c, spot in enumerate(row): # c is index and spot is item
                    if spot != '.':
                        if self.board_matrix[r + y][c + x] != '.':
                            return False
            return True

        except IndexError:
            return False



#######################



    # def place_piece(self, piece, x, y):
    #     if self.can_piece_fit(piece, x, y):
    #         for i, row in enumerate(piece):
    #             for j, value in enumerate(row):

    #         return self.board_matrix
        
    #     else:
    #         print(f'Couldn\'t place piece at ({x}, {y})')




        
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