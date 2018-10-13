import numpy as np
import imageio
import glob
import os

ascii_dict = {}

def ascii_array(fname):
    im = imageio.imread(fname)
    return 255 - im

def construct_ascii_dict():
    for im_path in glob.glob('ascii/*.png'):
        bitmap = ascii_array(im_path)
        id = int(os.path.basename(im_path).split('.')[0])
        ascii_dict[id] = bitmap

def main():
    construct_ascii_dict()
    print(ascii_dict)

if __name__ == '__main__':
    main()
