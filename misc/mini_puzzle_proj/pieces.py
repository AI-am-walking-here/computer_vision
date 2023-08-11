import numpy as np


class Piece:
    def __init__(self, label):
        self.label = label
        self.array = pieces[label]
        
    
    def Change_piece(self, new_label):
        """
        Changes the current piece to a new piece.

        Args:
            new_label (str): A single letter string representing the new piece to be used. 
                            This letter should be a key in the 'pieces' dictionary.
        """
        self.label = new_label
        self.array = pieces[new_label]

    def rotate(self):
        """
        Clockwise rotation
        """
        self.array = np.rot90(self.array)

    def flip_horizontal(self):
        """
        Flips Left-->Right
        """
        self.array = np.fliplr(self.array)

    def __str__(self):
        return self.label

pieces = {
    "A": np.array([
        ["A", ".", "."],
        ["A", "A", "A"],
    ]),
    "B": np.array([
        ["B", "B", "."],
        ["B", "B", "B"],
    ]),
    "C": np.array([
        ["C", ".", ".", "."],
        ["C", "C", "C", "C"],
    ]),
    "D": np.array([
        ["D", "D", "D", "D"],
        [".", ".", "D", "."],
    ]),
    "E": np.array([
        ["E", "E", ".", "."],
        [".", "E", "E", "E"],
    ]),
    "F": np.array([
        ["F", "."],
        ["F", "F"],
    ]),
    "G": np.array([
        ["G", "G", "G"],
        [".", ".", "G"],
        [".", ".", "G"],
    ]),
    "H": np.array([
        ["H", "H", "."],
        [".", "H", "H"],
        [".", ".", "H"],
    ]),
    "I": np.array([
        ["I", "I"],
        [".", "I"],
        ["I", "I"],
    ]),
    "J": np.array([
        ["J"],
        ["J"],
        ["J"],
        ["J"],
    ]),
    "K": np.array([
        ["K", "K"],
        ["K", "K"],
    ]),
    "L": np.array([
        [".", "L", "."],
        ["L", "L", "L"],
        [".", "L", "."],
    ]),
}

