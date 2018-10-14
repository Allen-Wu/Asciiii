import glob
import cv2
import numpy as np
from asciiii.engine.grid_matching import zero_padding, img_to_ascii
from asciiii.engine.edge_detect import Sketch
from asciiii.engine.ascii import ASCII
from asciiii.engine.img_tool import real_time_gif
import time
import signal
import sys
from asciiii import util


def process(sketcher, ascii_mapper, path, color):
    edged_image, colorful = sketcher.convert(path, color=color)
    row, col = ascii_mapper.get_shape()
    padded_img = zero_padding(edged_image, row, col)
    return img_to_ascii(ascii_mapper, padded_img, color=color, colorful=colorful)


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

    ascii_mapper = ASCII(eta=args_dict['eta'], light=args_dict['light'])
    sketcher = Sketch(args_dict['line'])

    if im_path:
        return process(sketcher, ascii_mapper, im_path, args_dict['color'])

    elif args_dict['video']:
        # Real time image to ascii streaming
        real_time_streaming(ascii_mapper, sketcher)

    elif args_dict['gif']:
        real_time_gif(3, 'result', ascii_mapper, sketcher)

    else:
        # Testing for the images in data folder
        for im_path in glob.glob(util.get_abs_path('data/*.jpg')):
            process(sketcher, ascii_mapper, im_path, args_dict['color'])
