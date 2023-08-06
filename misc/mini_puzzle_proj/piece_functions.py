import numpy as np

def rotate_shape(chosen_piece):
    chosen_piece = np.rot90(chosen_piece, k=-1) # Clockwise rotation
    return chosen_piece

def flip_horizontal(chosen_piece):
    return np.fliplr(chosen_piece) # Flips Left-->Right

