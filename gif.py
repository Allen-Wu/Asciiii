import os
import shutil
from os.path import join, exists
import numpy as np
import imageio
from PIL import Image
import cv2


def extractFrames(in_gif, out_folder):
    reader = imageio.get_reader(in_gif)
    if os.path.exists(out_folder):
        shutil.rmtree(out_folder)
    os.makedirs(out_folder)
    for i, im in enumerate(reader):
        edge_detected = cv2.Canny(im, 50, 200)
        imageio.imwrite("{}/{}_{}.gif".format(out_folder, os.path.basename(in_gif), i), edge_detected)
    return Image.open(in_gif).info['duration']


def GenerateGif(in_folder, out_gif, duration=10):
    with imageio.get_writer(out_gif, mode='I', duration=duration/1000) as writer:
        filenames = os.listdir(in_folder)
        for filename in filenames:
            image = imageio.imread(join(in_folder, filename))
            writer.append_data(image)
    writer.close()


# id = str(89832489)
# id = "temp"
# if os.path.exists(id):
#     shutil.rmtree(id)
# os.makedirs(id)
# duration = extractFrames('pikachu.gif', '{}/tempory'.format(id))
# GenerateGif('{}/tempory'.format(id), '{}/result.gif'.format(id), duration)
