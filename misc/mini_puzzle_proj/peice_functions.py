def rotate_shape(shape):
    rows = len(shape)
    cols = len(shape[0])
    rotated_shape = [[shape[rows - 1 - j][i] for j in range(rows)] for i in range(cols)]
    return rotated_shape

def flip_shape_horizontal(shape):
    return [row[::-1] for row in shape]

def get_all_orientations(shape):
    orientations = []
    for _ in range(4):
        orientations.append(shape)
        shape = rotate_shape(shape)
    flipped_shape = flip_shape_horizontal(shape)
    for _ in range(4):
        orientations.append(flipped_shape)
        flipped_shape = rotate_shape(flipped_shape)
    return orientations

# Example usage
shape_example = [
    ['.', '.','.'],
    ['X', '.','.'],
    ['X', 'X','X'],
]

orientations_list = get_all_orientations(shape_example)

# Printing the result
for i, orientation in enumerate(orientations_list, 1):
    print('[')
    for row in orientation:
        print(row, )
    print('],')