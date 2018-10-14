import cv2
import scipy.signal
import numpy as np
import os
import imageio

# THRESHOLD_LOW = 220
# THRESHOLD_HIGH = 255


def canny_custom(im_path):
    """
    deprecated canny edge detection implementation
    """
    in_img = cv2.imread(im_path, 0)
    # Calculate gradients and orientation
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

    # Canny edge detection
    edge_detected = cv2.Canny(in_img, 50, 100)
    return edge_detected


def NWG(img_out):
    """
    unused function
    """
    # img_out = cv2.threshold(path, THRESHOLD_LOW, THRESHOLD_HIGH, cv2.THRESH_BINARY)[1]
    #
    # print(img_out.shape)
    # imageio.imwrite('test/init.jpg', img_out)
    H, W = img_out.shape
    flag = True
    g = 1
    index=0
    while flag:
        g = 1 - g
        flag = False
        img = img_out.copy()

        for i in range(1, H-1):
            for j in range(1, W-1):
                if img[i][j] > 0:
                    p = [
                        0 if img[i - 1, j] == 0 else 1,
                        0 if img[i - 1, j + 1] == 0 else 1,
                        0 if img[i, j + 1] == 0 else 1,
                        0 if img[i + 1, j + 1] == 0 else 1,
                        0 if img[i + 1, j] == 0 else 1,
                        0 if img[i + 1, j - 1] == 0 else 1,
                        0 if img[i, j - 1] == 0 else 1,
                        0 if img[i - 1, j - 1] == 0 else 1,
                    ]

                    b = np.sum(p)

                    if 1 < b < 7:
                        a = np.array(p) - np.array(p[1:]+[p[0]])
                        a = np.where(a == -1)[0].size

                        c = 0
                        if (p[0] == 0 and p[1] == 0 and p[2] == 0 and p[5] == 0 and p[4] == 1 and p[6] == 1) or (
                                p[2] == 0 and p[3] == 0 and p[4] == 0 and p[7] == 0 and p[6] == 1 and p[0] == 1):
                            c = 1

                        if a == 1 or c == 1:
                            e = (p[2] + p[4]) * p[0] * p[6]
                            f = (p[6] + p[0]) * p[4] * p[2]
                            if (g == 0 and e == 0) or (g == 1 and f == 0):
                                img_out[i][j] = 0
                                flag = True
        # print("save", index)
        imageio.imwrite('test/{}.jpg'.format(index), img_out)
        index += 1

    return img_out


class Sketch:
    """
    class for edge detection
    """
    neighborhood = np.array(
        [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]],
        np.uint8)

    def __init__(self, width=500):
        self.width = width

    def convert(self, path, frame=None, color=False):
        # print(path)
        if path == '':
            gray = frame
        else:
            gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        # cv2.imwrite("_gray.jpg", gray)
        ratio = self.width / gray.shape[1]

        gray = cv2.resize(gray, (0, 0), fx=ratio, fy=ratio)

        dilated = cv2.dilate(gray, self.neighborhood, iterations=1)
        # cv2.imwrite("_dilated.jpg", dilated)

        diff = cv2.absdiff(dilated, gray)
        # cv2.imwrite("_diff.jpg", diff)
        # diff = NWG(dilated)

        contour = 255 - diff
        # cv2.imwrite("./output.jpg", contour)
        contour = cv2.threshold(contour, np.mean(contour)-20, 255, cv2.THRESH_BINARY)[1]

        # print(path, np.mean(contour), np.mean(contour[contour>100]))

        if color:
            colorful = cv2.imread(path, cv2.IMREAD_COLOR)
            colorful = cv2.GaussianBlur(colorful, (15, 15), 0)

            colorful = cv2.resize(
                colorful, (contour.shape[1], contour.shape[0]),
                interpolation=cv2.INTER_AREA
            )
            colorful = cv2.GaussianBlur(colorful, (3, 3), 0)

            return contour, colorful

        return contour


if __name__ == '__main__':

    filenames = os.listdir("data")
    sketch = Sketch()
    for filename in filenames:
        imageio.imwrite("result500/"+filename, sketch.convert("data/"+filename))
