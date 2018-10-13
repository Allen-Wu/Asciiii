import numpy as np
import imageio
import glob
import os

class ASCII:
    ascii_dict = {}

    def __init__(self):
        self.construct_ascii_dict()

    def get_array(self, id):
        return self.ascii_dict[id]

    def ascii_array(self, fname):
        im = imageio.imread(fname)
        return 255 - im

    def construct_ascii_dict(self):
        for im_path in glob.glob('ascii/*.png'):
            bitmap = self.ascii_array(im_path)
            id = int(os.path.basename(im_path).split('.')[0])
            self.ascii_dict[id] = bitmap
