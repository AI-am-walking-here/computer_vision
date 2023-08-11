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
            list: A 2D list (matrix) with the choose piece type replace with empty spaces "."
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


    def place_piece(self, piece, coordinate):
        """
        Places a game piece onto the game board at a specific coordinate.

        Args:
            piece (Piece object): An instance of Piece class representing the game piece.
            coordinate (tuple): A tuple representing the coordinates (x, y) on the board where the top-left cell of the piece should be placed.
        """
        x, y = coordinate
        piece_array = piece.array # Piece Class Object

        if self.can_piece_fit(piece, coordinate):
            for r, row in enumerate(piece_array):
                for c, spot in enumerate(row):
                    if spot != '.':
                        self.board_matrix[r + y][c + x] = spot
        else:
            print(f"Couldn't place piece at ({x}, {y})")

        return self.board_matrix


    def remove_piece(self, coordinate):
        """
        Removes a game piece on the game board at a specific coordinate.

        Args:
            coordinate (tuple): A tuple representing the coordinates (x, y) on the board where the top-left cell of the piece should be placed.

        Returns:
            bool: Returns True if the game piece can fit at the specified coordinate on the game board without colliding with any existing pieces or going outside the bounds of the board. Returns False otherwise.
        """
        x, y = coordinate
        try:
            piece = self.board_matrix[y,x]
            if piece != '.':
                self.board_matrix[self.board_matrix == piece] = '.' # Creates a True/False mask over the matrix
        except IndexError:
            return
