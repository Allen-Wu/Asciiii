import  os
import numpy as np
import cv2
import imageio

THRESHOLD_LOW = 220
THRESHOLD_HIGH = 255


def NWG(path):
    img_out = cv2.threshold(path, THRESHOLD_LOW, THRESHOLD_HIGH, cv2.THRESH_BINARY)[1]

    print(img_out.shape)
    imageio.imwrite('test/init.jpg', img_out)
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
        print("save", index)
        imageio.imwrite('test/{}.jpg'.format(index), img_out)
        index += 1

    return img_out


def sketch(path):
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # cv2.imwrite("_gray.jpg", gray)

    neiborhood24 = np.array([[1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1]],
                            np.uint8)
    dilated = cv2.dilate(gray, neiborhood24, iterations=1)
    # cv2.imwrite("_dilated.jpg", dilated)

    diff = cv2.absdiff(dilated, gray)
    # cv2.imwrite("_diff.jpg", diff)

    contour = 255 - diff
    # cv2.imwrite("./output.jpg", contour)

    # print(path, np.mean(contour), np.mean(contour[contour>100]))

    return cv2.threshold(contour, np.mean(contour)-20, 255, cv2.THRESH_BINARY)[1]


filenames = os.listdir("data")
for filename in filenames:
    imageio.imwrite("result/"+filename, sketch("data/"+filename))