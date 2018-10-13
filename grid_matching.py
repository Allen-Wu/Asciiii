import numpy as np
import os

# Padding zeros for input image to be right size
def zero_padding(img_matrix, grid_row, grid_col):
    row, col = img_matrix.shape
    resize_row, resize_col = img_matrix.shape
    if (row % grid_row) != 0:
        resize_row = (row // grid_row + 1) * grid_row
    if (col % grid_col) != 0:
        resize_col = (col // grid_col + 1) * grid_col
    # Padding zeros
    if resize_row > row:
        padding_rows = np.ones((resize_row - row, col)) * 255
        img_matrix = np.vstack((img_matrix, padding_rows))
    if resize_col > col:
        padding_cols = np.ones((resize_row, resize_col - col)) * 255
        img_matrix = np.hstack((img_matrix, padding_cols))
    return img_matrix

def img_to_ascii(ascii_candidate, img_matrix):
    grid_row, grid_col = ascii_candidate.get_shape()
    output_row = int(img_matrix.shape[0] / grid_row)
    output_col = int(img_matrix.shape[1] / grid_col)
    char_list = []
    for i in range(output_row):
        row_list = []
        for j in range(output_col):
            sub_matrix = img_matrix[(i*grid_row):(i*grid_row+grid_row), (j*grid_col):(j*grid_col+grid_col)]
            id_max, _ = ascii_candidate.hamming_match(sub_matrix, True)
            row_list.append(chr(id_max))
        char_list.append(row_list)
    output_string = ''
    for x in char_list:
        for y in x:
            output_string += y
        output_string += '\n'
    os.system('clear')
    print(output_string)

# # Only for testing
# def main():
#     # Test for zero padding
#     # Grid matrix
#     grid_candidate = np.random.rand(3, 2)
#     img_matrix = np.random.rand(7, 5)
#     print(img_matrix)
#     print(zero_padding(img_matrix, grid_candidate))
#
#     # Test for Hamming Distance
#     grid_candidate = []
#     candidate_one = np.array([[1, 0, 1], [1, 0, 1], [1, 0, 1]])
#     candidate_two = np.array([[0, 1, 0], [0, 1, 0], [0, 0, 1]])
#     measure_grid = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
#     grid_candidate.append(candidate_one)
#     grid_candidate.append(candidate_two)
#     print("Best index: ", hamming_grid_match(grid_candidate, measure_grid))
#
#
# if __name__ == '__main__':
#     main()