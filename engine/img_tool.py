import os
import shutil
from os.path import join
import numpy as np
import imageio
from PIL import Image
import cv2
import scipy
import time
from engine.grid_matching import zero_padding, img_to_ascii

ASCII_ROOT = "ascii/light"

# Generate a real time gif with specific duration
def real_time_gif(duration, filename, ascii_mapper, sketcher):
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    curr_time = time.time()
    img_list = []
    ascii_img_list = []
    gif_name = filename
    temp_folder = 'temp_gif'
    temp_gif = 'temp_real'

    while (curr_time - start_time) < duration:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_list.append(gray)
        curr_time = time.time()

    cap.release()

    for x in img_list:
        edged_image = sketcher.convert('', frame=x)
        row, col = ascii_mapper.get_shape()

        # Enlarge the image twice and padding
        # edge_detected = cv2.resize(edge_detected, (0, 0), fx=1, fy=1)
        padded_img = zero_padding(edged_image, row, col)
        padded_img = np.flip(padded_img, axis=1)
        res = img_to_ascii(ascii_mapper, padded_img, return_flag=True)
        ascii_img_list.append(ascii_to_img(res, save_flag=False))

    imageio.mimsave('{}.gif'.format(temp_gif), ascii_img_list)
    extractFrames('{}.gif'.format(temp_gif), temp_folder)
    GenerateGif(temp_folder, '{}.gif'.format(gif_name), duration * 100)
    # Remove temporary files
    os.system('rm {} -rf'.format(temp_folder))
    os.system('rm {}.gif'.format(temp_gif))

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


def ascii_to_img(ascii, save_flag=True):
    """
    Convert an ascii numpy to a image numpy.
    :param ascii: an ascii numpy
    :return: a image numpy
    """
    rows = []
    for row in ascii:
        imgs = [Image.open(join(ASCII_ROOT, "{}.png".format(int(c)))) for c in row]
        rows += [np.hstack((np.asarray(i) for i in imgs))]

    image = np.vstack((np.asarray(r) for r in rows))
    if save_flag:
        image = Image.fromarray(image)
        image.save('ascii.jpg')
    else:
        return image
