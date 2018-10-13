import argparse
import cv2
import scipy.signal
import numpy as np
from grid_matching import *
from edge_detect import *
from ascii import *


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image', help='The input image file.')
    parser.add_argument('--line_number', help='The number of output lines')

    args = parser.parse_args()

    args_dict = vars(args)

    line_number = int(args_dict['line_number'])
    # Read the image file
    in_img = cv2.imread(args_dict["input_image"], 0)

    # Calculate gradients and orientation
    Gx = scipy.signal.convolve2d(
        in_img, np.array([[1, -1]]),
        mode='same', boundary='fill', fillvalue=0
    )
    Gy = scipy.signal.convolve2d(
        in_img, np.array([[1], [-1]]),
        mode='same', boundary='fill', fillvalue=0
    )

    g_intensity = np.sqrt(np.power(Gx, 2) + np.power(Gy, 2))
    print(np.mean(g_intensity[np.nonzero(g_intensity)]))
    g_orientation = np.arctan2(Gy, Gx)

    # Canny edge detection
    edge_detected = cv2.Canny(in_img, 50, 200)

    save_img(in_img, edge_detected)
    # Matrix representations for ascii character
    ascii_candidates = ASCII()
    
    candidate_row, candidate_col = ascii_candidates.get_shape()

    print("Candidate row and col: ", candidate_row, candidate_col)
    
    # Resize the input image
    # print('Original size: ', edge_detected.shape)
    # ratio = candidate_row * line_number // edge_detected.shape[0]
    # print('Ratio: ', ratio)
    # resized_img = cv2.resize(edge_detected, (candidate_row * line_number, edge_detected.shape[1] * ratio))
    # resized_img = cv2.resize(edge_detected, (100, 50))
    # print('Resized size: ', resized_img.shape)  

    padded_img = zero_padding(edge_detected, candidate_row, candidate_col)
    img_to_ascii(ascii_candidates, padded_img)

if __name__ == '__main__':
    main()