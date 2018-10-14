import numpy as np
import os
from asciiii.engine.ascii import ASCII
from itertools import product, repeat
from multiprocessing import Pool

# Clear output screen
def clear():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


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


# Transfer edge-detected image to ascii format
def img_to_ascii(ascii_candidate, img_matrix, return_flag=False, color=False, colorful=None):
    # print(img_matrix.shape, colorful.shape)
    grid_row, grid_col = ascii_candidate.get_shape()
    output_row = int(img_matrix.shape[0] / grid_row)
    output_col = int(img_matrix.shape[1] / grid_col)
    char_list = []
    res = np.zeros((output_row, output_col))
    for i in range(output_row):
        row_list = []
        for j in range(output_col):
            sub_matrix = img_matrix[(i*grid_row):(i*grid_row+grid_row), (j*grid_col):(j*grid_col+grid_col)]
            id_max = ascii_candidate.hamming_match(sub_matrix, True)
            if color:
                color_matrix = colorful[i*grid_row, j*grid_col, :]
                b, g, r = [color_matrix[i] for i in range(3)]
                row_list.append('\033[38;5;{}m'.format(r, g, b) + str(chr(id_max)) + '\033[0m')
            else:
                row_list.append(chr(id_max))
            if return_flag:
                res[i][j] = id_max
        char_list.append(row_list)
    output_string = ''
    for x in char_list:
        for y in x:
            output_string += y
        output_string += '\n'
    if return_flag:
        return res
    clear()
    print(output_string)
    return output_string


def img_to_ascii_multi(ascii_candidate, img_matrix):
    pool = Pool(processes=8)
    grid_row, grid_col = ascii_candidate.get_shape()
    output_row = int(img_matrix.shape[0] / grid_row)
    output_col = int(img_matrix.shape[1] / grid_col)

    row_size = list(range(output_row))
    col_size = list(range(output_col))

    sub_matrix = [img_matrix[(i*grid_row):(i*grid_row+grid_row), (j*grid_col):(j*grid_col+grid_col)] \
                  for i, j in product(row_size, col_size)]
    args = list(zip(sub_matrix, repeat(ascii_candidate._ascii_dict), repeat(ascii_candidate.eta)))
    char_list = np.array(pool.starmap(ASCII.hamming_match_static, args))
    output_string = ''
    for x in char_list.reshape((output_row, output_col)):
        for y in x:
            output_string += chr(y)
        output_string += '\n'
    # clear()
    print(output_string)
