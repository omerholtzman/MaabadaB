import numpy as np
import matplotlib.pyplot as plt


def fraunhofer_fft(pattern):
    pass


def check_pattern(pattern):
    plt.imshow(pattern)
    plt.show()


def square_pattern(width, height, side):
    mtx = np.zeros((width, height))
    center = (width / 2, height / 2)
    for row in range(len(mtx)):
        for col in range(len(mtx[row])):
            if np.abs(row - center[0]) <= side / 2 and np.abs(col - center[1]) <= side / 2:
                mtx[row][col] = 1
    return mtx


def multi_square_pattern():
    pass


def hexagon_pattern():
    pass


def multi_hexagon_pattern():
    pass


def circle_pattern(width, height, radius):
    mtx = np.zeros((width, height))
    center = (width / 2, height / 2)
    for row in range(len(mtx)):
        for col in range(len(mtx[row])):
            if (row - center[0]) ** 2 + (col - center[1]) ** 2 <= radius ** 2:
                mtx[row][col] = 1
    return mtx


def spiral_pattern(width, height, thickness, radius):
    mtx = np.ones((width, height))
    center = (width / 2, height / 2)
    diag = int(np.sqrt(center[0] ** 2 + center[1] ** 2))
    for r in range(0, diag, 2 * thickness):
        for row in range(len(mtx)):
            for col in range(len(mtx[row])):
                if r ** 2 <= (row - center[0]) ** 2 + (col - center[1]) ** 2 <= (r + thickness) ** 2:
                    mtx[row][col] = 0
    return mtx


def grid_pattern(thickness):
    pass


if __name__ == '__main__':
    # crc = circle_pattern(100,100,10)
    # check_pattern(crc)
    # sqr = square_pattern(100, 100, 10)
    # check_pattern(sqr)
    sprl = spiral_pattern(100, 100, 4, 2)
    check_pattern(sprl)
