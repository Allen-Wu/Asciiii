import argparse
import glob
import cv2
import numpy as np
from grid_matching import zero_padding, img_to_ascii
from edge_detect import Sketch
from ascii import ASCII
import time
import signal
import sys

def process(sketcher, ascii_mapper, path):
    edged_image = sketcher.convert(path)
    row, col = ascii_mapper.get_shape()
    padded_img = zero_padding(edged_image, row, col)
    img_to_ascii(ascii_mapper, padded_img)

def sigterm_handler(_signo, _stack_frame):
    print('Gracefully shut down real time streaming.')
    sys.exit(0)

def real_time_streaming(ascii_mapper, sketcher):
    # Set graceful interruption
    signal.signal(signal.SIGINT, sigterm_handler)

    cap = cv2.VideoCapture(0)

    while True:
        start = time.time()
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edged_image = sketcher.convert('', frame=gray)
        row, col = ascii_mapper.get_shape()

        # Enlarge the image twice and padding
        # edge_detected = cv2.resize(edge_detected, (0, 0), fx=1, fy=1)
        padded_img = zero_padding(edged_image, row, col)
        padded_img = np.flip(padded_img, axis=1)
        img_to_ascii(ascii_mapper, padded_img)
        end = time.time()
        print('fps: {:f}'.format(1 / (end - start)))

def run(**args_dict):
    im_path = args_dict['file']
    line_number = args_dict['line']

    ascii_mapper = ASCII(eta=args_dict['eta'], light=args_dict['light'])
    sketcher = Sketch(line_number)

    if im_path:
        process(sketcher, ascii_mapper, im_path)

    elif args_dict['video']:
        # Real time image to ascii streaming
        real_time_streaming(ascii_mapper, sketcher)

    else:
        # Testing for the images in data folder
        for im_path in glob.glob('data/*.jpg'):
            process(sketcher, ascii_mapper, im_path)



def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, help='input image file path')
    parser.add_argument('-l', '--line', action='store', type=int, default=800, help='desired image width')
    parser.add_argument('-v', '--video', action='store_true', default=False, help='real-time video mode, need your camera')
    parser.add_argument('-e', '--eta', action='store', type=float, default=0.15, help='hyper-parameter for ascii matching')
    parser.add_argument('-li', '--light', action='store_true', default=True, help='use a small set of ascii with high frequenty')
    args = parser.parse_args()
    args_dict = vars(args)

    run(**args_dict)




if __name__ == '__main__':
    main()
