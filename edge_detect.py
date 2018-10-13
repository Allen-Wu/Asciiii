import argparse
import cv2
import scipy.signal
import numpy as np
from matplotlib import pyplot as plt


def save_img(img, edges):
    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122)
    plt.imshow(edges, cmap='gray')
    plt.title('Edge Image')
    plt.xticks([])
    plt.yticks([])
    # plt.show()

    plt.savefig("test_out.png")
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image', help='The input image file.')

    args = parser.parse_args()

    args_dict = vars(args)

    in_img = cv2.imread(args_dict["input_image"], 0)
    Gx = scipy.signal.convolve2d(
        in_img, np.array([[1, -1]]),
        mode='same', boundary='fill', fillvalue=0
    )
    Gy = scipy.signal.convolve2d(
        in_img, np.array([[1], [-1]]),
        mode='same', boundary='fill', fillvalue=0
    )

    g_intensity = np.sqrt(np.power(Gx, 2) + np.power(Gy, 2))
    print(np.mean(g_intensity[np.nonzero(g_intensity)]))
    g_orientation = np.arctan2(Gy, Gx)
    edge_detected = cv2.Canny(in_img, 50, 200)
    save_img(in_img, edge_detected)
