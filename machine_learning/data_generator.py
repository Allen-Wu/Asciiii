import glob
from collections import defaultdict
from engine.grid_matching import zero_padding
from engine.edge_detect import Sketch
from engine.ascii import ASCII
import torch
import random
import scipy.signal
import numpy as np

IMAGE_WIDTH = 500


def img_to_ascii(ascii_candidate, img_matrix, counter, index, disk):
    grid_row, grid_col = ascii_candidate.get_shape()
    output_row = int((img_matrix.shape[0]-2) / grid_row)
    output_col = int((img_matrix.shape[1]-2) / grid_col)
    # char_list = []
    for i in range(1, output_row-1):
        # row_list = []
        for j in range(1, output_col-1):
            sub_matrix = img_matrix[(i*grid_row):(i*grid_row+grid_row), (j*grid_col):(j*grid_col+grid_col)]
            id_max, _ = ascii_candidate.hamming_match(sub_matrix, True)
            if counter[chr(id_max)] in index[chr(id_max)]:
                Gx = scipy.signal.convolve2d(
                    sub_matrix, np.array([[1, -1]]),
                    mode='same', boundary='fill', fillvalue=0
                )
                Gy = scipy.signal.convolve2d(
                    sub_matrix, np.array([[1], [-1]]),
                    mode='same', boundary='fill', fillvalue=0
                )
                g_orientation = np.arctan2(Gy, Gx)
                disk[chr(id_max)] += [g_orientation]
            counter[chr(id_max)] += 1
    #         row_list.append(chr(id_max))
    #     char_list.append(row_list)
    # output_string = ''
    # for x in char_list:
    #     for y in x:
    #         output_string += y
    #     output_string += '\n'
    # clear()
    # print(output_string)


ascii_mapper = ASCII()


counter_result = {' ': 126156, ',': 2318, '.': 1564, '~': 1023, '_': 4408, '#': 3829, '^': 1434, '"': 2724, '=': 917, '<': 262, ']': 1224, '(': 231, '|': 471, '-': 505, '/': 497, '\\': 553, 'X': 831, '[': 1272, ')': 193, 'Y': 368, '+': 463, ':': 171, 'V': 788, '`': 1605, 'T': 305, '>': 259}
index = defaultdict(list)
for ch, count in counter_result.items():
    index[ch] = random.sample(list(range(0, count)), 150)

counter = defaultdict(int)
disk = defaultdict(list)

sketcher = Sketch(800)
for path in glob.glob('../data/result800/*'):
    edged_image = sketcher.convert(path)
    row, col = ascii_mapper.get_shape()

    padded_img = zero_padding(edged_image, row, col)
    img_to_ascii(ascii_mapper, padded_img, counter, index, disk)

sketcher = Sketch(500)
for path in glob.glob('../data/result800/*'):
    edged_image = sketcher.convert(path)
    row, col = ascii_mapper.get_shape()

    padded_img = zero_padding(edged_image, row, col)
    img_to_ascii(ascii_mapper, padded_img, counter, index, disk)

sketcher = Sketch(1000)
for path in glob.glob('../data/result800/*'):
    edged_image = sketcher.convert(path)
    row, col = ascii_mapper.get_shape()

    padded_img = zero_padding(edged_image, row, col)
    img_to_ascii(ascii_mapper, padded_img, counter, index, disk)

print(counter)
label_to_char = {}
char_to_label = {}
label = 0
for ch, arr in disk.items():
    temp = torch.tensor(arr)
    print(ch, temp.shape)
    torch.save(temp, 'AsciiOri/ascii_img_{}.pt'.format(label))
    label_to_char[label] = ch
    char_to_label[ch] = label
    label += 1
    temp = torch.load('AsciiOri/ascii_img_{}.pt'.format(label-1))
    print(temp)

print(label_to_char)
print(char_to_label)


