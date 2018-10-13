import numpy as np
import imageio
import glob
import os

class ASCII:
    _ascii_dict = {}

    def __init__(self):
        self._construct_ascii_dict()

    def get_array(self, id):
        return self._ascii_dict[id]

    def _ascii_array(self, fname):
        im = imageio.imread(fname)
        return 255 - im

    def _construct_ascii_dict(self):
        for im_path in glob.glob('ascii/*.png'):
            bitmap = self._ascii_array(im_path)
            id = int(os.path.basename(im_path).split('.')[0])
            self._ascii_dict[id] = bitmap

    def hamming_match(self, measure_grid, gray_scale=True):
        id_max = 0
        distance_min = 1e10
        for id in self._ascii_dict:
            distance = hamming_dis(self._ascii_dict[id], gray_scale)
            if distance < distance_min:
                distance_min = distance
                id_max = id
        return id, distance_min

    def _hamming_dis(a, b, gray_scale=False):
        if gray_scale == False:
            xor_array = np.bitwise_xor(a, b)
            return np.count_nonzero(xor_array)
        else:
            # Calculate the sum of gray scale diff
            return np.absolute(a - b).sum()