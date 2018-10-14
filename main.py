import argparse
import glob
import time
from grid_matching import zero_padding, img_to_ascii
from edge_detect import Sketch
from ascii import ASCII
import cv2

IMAGE_WIDTH = 800

def process(sketcher, ascii_mapper, path):
    
    edged_image = sketcher.convert(path)
    row, col = ascii_mapper.get_shape()
    padded_img = zero_padding(edged_image, row, col)
    img_to_ascii(ascii_mapper, padded_img)

def real_time_streaming(ascii_mapper, sketcher):
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edged_image = sketcher.convert('', frame=gray)
        row, col = ascii_mapper.get_shape()

        # Enlarge the image twice and padding
        # edge_detected = cv2.resize(edge_detected, (0, 0), fx=1, fy=1)
        padded_img = zero_padding(edged_image, row, col)
        img_to_ascii(ascii_mapper, padded_img)

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image', type=str, help='input image file path')
    parser.add_argument('--line_number', type=int, default=IMAGE_WIDTH, help='desired image width')
    args = parser.parse_args()
    args_dict = vars(args)

    im_path = args_dict["input_image"]
    line_number = args_dict['line_number']

    ascii_mapper = ASCII(eta=0.05)
    sketcher = Sketch(line_number)
    # process(sketcher, ascii_mapper, im_path, line_number)

    # Real time image to ascii streaming
    real_time_streaming(ascii_mapper, sketcher)

    # Testing for the images in data folder
    for im_path in glob.glob('data/*.png'):
        process(sketcher, ascii_mapper, im_path)


if __name__ == '__main__':
    main()
