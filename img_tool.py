import os
import shutil
from os.path import join
import numpy as np
import imageio
from PIL import Image
import cv2

ASCII_ROOT = "ascii/"


def gradient_intensity_and_orientation(in_img):
    """
    Detect the image of gradient intensity and gradient orientations.
    :param in_img: an image numpy array
    :return: g_intensity, g_orientation
    """
    Gx = scipy.signal.convolve2d(
        in_img, np.array([[1, -1]]),
        mode='same', boundary='fill', fillvalue=0
    )
    Gy = scipy.signal.convolve2d(
        in_img, np.array([[1], [-1]]),
        mode='same', boundary='fill', fillvalue=0
    )

    g_intensity = np.sqrt(np.power(Gx, 2) + np.power(Gy, 2))
    g_orientation = np.arctan2(Gy, Gx)
    return g_intensity, g_orientation


# id = str(89832489)
# id = "temp"
# if os.path.exists(id):
#     shutil.rmtree(id)
# os.makedirs(id)

def extractFrames(in_gif, out_folder):
    """
    template: duration = extractFrames('pikachu.gif', '{}/tempory'.format(id))
    :param in_gif: filename for input image
    :param out_folder: directory for output
    :return: duration between frames
    """
    reader = imageio.get_reader(in_gif)
    if os.path.exists(out_folder):
        shutil.rmtree(out_folder)
    os.makedirs(out_folder)
    for i, im in enumerate(reader):
        edge_detected = cv2.Canny(im, 50, 200)
        imageio.imwrite("{}/{}_{}.gif".format(out_folder, os.path.basename(in_gif), i), edge_detected)
    return Image.open(in_gif).info['duration']


def GenerateGif(in_folder, out_gif, duration=10):
    """
    template: GenerateGif('{}/tempory'.format(id), '{}/result.gif'.format(id), duration)
    :param in_folder: directory for input
    :param out_gif: directory and filename for output image
    :param duration: the time gap between frames, read before
    :return:
    """
    with imageio.get_writer(out_gif, mode='I', duration=duration/1000) as writer:
        filenames = os.listdir(in_folder)
        for filename in filenames:
            image = imageio.imread(join(in_folder, filename))
            writer.append_data(image)
    writer.close()


def ascii_to_img(ascii):
    """
    Convert an ascii numpy to a image numpy.
    :param ascii: an ascii numpy
    :return: a image numpy
    """
    rows = []
    for row in ascii:
        imgs = [Image.open(join(ASCII_ROOT, "{}.png".format(ord(c)))) for c in row]
        rows += [np.hstack((np.asarray(i) for i in imgs))]

    image = np.vstack((np.asarray(r) for r in rows))
    image = Image.fromarray(image)
    image.save('ascii.jpg')
