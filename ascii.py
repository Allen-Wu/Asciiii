import numpy as np
import imageio
import glob
import os

class ASCII:
    """
    array presentation of ascii characters
    """
    _ascii_dict = {}
    _x = 0
    _y = 0

    def __init__(self, eta=0.2, light=True):
        self.light = light
        self._construct_ascii_dict()
        self.eta = eta


    def get_shape(self):
        return self._x, self._y

    def get_array(self, id):
        return self._ascii_dict[id]

    def _ascii_array(self, fname):
        im = imageio.imread(fname)
        return im

    def _construct_ascii_dict(self):
        if self.light:
            for im_path in glob.glob('ascii/light/*.png'):
                bitmap = self._ascii_array(im_path)
                id = int(os.path.basename(im_path).split('.')[0])
                self._ascii_dict[id] = bitmap
        else:
            for im_path in glob.glob('ascii/light/*.png'):
                bitmap = self._ascii_array(im_path)
                id = int(os.path.basename(im_path).split('.')[0])
                self._ascii_dict[id] = bitmap
        self._x, self._y = self._ascii_dict[id].shape

    def _hamming_dis(self, a, b, gray_scale=False):
        if not gray_scale:
            xor_array = np.bitwise_xor(a, b)
            return np.count_nonzero(xor_array)
        else:
            # Calculate the avg of gray scale diff
            return np.average(np.absolute(a - b))

    def hamming_match(self, measure_grid, gray_scale=True):
        if measure_grid.mean() > 255 * (1 - self.eta):
            return ord(' ')
        if measure_grid.mean() < 255 * self.eta:
            return ord('#')

        id_max = 0
        distance_min = 256
        for id in self._ascii_dict:
            distance = self._hamming_dis(self._ascii_dict[id], measure_grid, gray_scale)
            if distance < distance_min:
                distance_min = distance
                id_max = id
        return id_max
