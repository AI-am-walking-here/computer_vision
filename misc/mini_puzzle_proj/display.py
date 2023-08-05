class Display:
    def __init__(self,board_matrix):
        self.count = 0   # To be used later
        self.board_matrix = board_matrix


    def print_display(self):
        for row in self.board_matrix:
            for spot in row:
                print(spot, end=" ")
            print() # Prints a new line