import argparse
import glob
import time
from grid_matching import zero_padding, img_to_ascii
from edge_detect import Sketch
from ascii import ASCII

IMAGE_WIDTH = 800

def process(sketcher, ascii_mapper, path):
    
    edged_image = sketcher.convert(path)
    row, col = ascii_mapper.get_shape()
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

    start = time.time()

    # Testing for the images in data folder
    for im_path in glob.glob('data/*.png'):
        process(sketcher, ascii_mapper, im_path)

    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()
