import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from tqdm import tqdm

def noramlize(mtx):
    norma = mtx / np.max (mtx)
    return norma*256


def fraunhofer_fft(pattern):
    ft = np.fft.ifftshift (pattern)
    ft = np.fft.fft2 (ft)
    ft = np.fft.fftshift (ft)
    sim = noramlize (np.abs (ft))
    # sim = np.power (sim, 2)
    plt.imshow (sim, vmin=0, vmax=10)
    plt.title ("simulated")
    plt.colorbar ()
    plt.show ()
    return sim


def check_pattern(pattern, title="hole", lim=1):
    plt.imshow (pattern, vmin=0, vmax=lim)
    plt.title (title)
    plt.colorbar ()
    plt.show ()


def square_pattern(width, height, side):
    mtx = np.zeros ((width, height))
    center = (width / 2, height / 2)
    for row in range (len (mtx)):
        for col in range (len (mtx[row])):
            if np.abs (row - center[0]) <= side / 2 and np.abs (col - center[1]) <= side / 2:
                mtx[row][col] = 1
    return mtx


def multi_square_pattern(width, height, edge, diff):
    mtx = square_pattern (width, height, 4 * edge + 3 * diff)
    return grid_pattern (width, height, diff, edge, mtx, True)


def hexagon_generator(edge_length, offset):
    """Generator for coordinates in a hexagon."""
    x, y = offset
    for angle in range (0, 360, 60):
        x += np.cos (np.radians (angle)) * edge_length
        y += np.sin (np.radians (angle)) * edge_length
        yield x, y


def hexagon_pattern(width, height, edge):
    image = Image.new ('L', (width, height), 'black')
    draw = ImageDraw.Draw (image)
    hexagon = hexagon_generator (edge, offset=(width / 2 - edge / 2, height / 2 - edge / 2))
    draw.polygon (list (hexagon), outline='white', fill='white')
    I = np.asarray (image)
    return I


def circle_pattern(width, height, radius):
    mtx = np.zeros ((width, height))
    center = (width / 2, height / 2)
    for row in range (len (mtx)):
        for col in range (len (mtx[row])):
            if (row - center[0]) ** 2 + (col - center[1]) ** 2 <= radius ** 2:
                mtx[row][col] = 1
    return mtx


def spiral_pattern(width, height, thickness_b, thickness_w, radius):
    mtx = np.ones ((width, height))
    center = (width / 2, height / 2)
    diag = int (np.sqrt (center[0] ** 2 + center[1] ** 2))
    for row in tqdm(range (len (mtx))):
        for col in range (len (mtx[row])):
            if (row - center[0]) ** 2 + (col - center[1]) ** 2 <= radius ** 2:
                mtx[row][col] = 0
    for r in tqdm(range (radius, diag, thickness_w + thickness_b)):
        for row in range (len (mtx)):
            for col in range (len (mtx[row])):
                if r ** 2 <= (row - center[0]) ** 2 + (col - center[1]) ** 2 <= (r + thickness_b) ** 2:
                    mtx[row][col] = 0
    return mtx


def grid_pattern(width, height, thickness_b, thickness_w, mtx=None, ismtx=False):
    if not ismtx:
        mtx = np.ones ((width, height))
    center = (width // 2, height // 2)
    for i in range (-thickness_b // 2, thickness_b // 2):
        mtx[:, center[0] + i] = 0
        mtx[center[1] + i] = 0
    for a in range (thickness_b // 2, center[0] - thickness_w, thickness_w + thickness_b):
        for i in range (thickness_b):
            if center[0] + a + thickness_w + i < width:
                mtx[:, center[0] + a + thickness_w + i - 1] = 0
            if center[0] - a - thickness_w - i > 1:
                mtx[:, center[0] - a - thickness_w - i] = 0
    for a in range (thickness_b // 2, center[1] - thickness_w, thickness_w + thickness_b):
        for i in range (thickness_b):
            if center[1] + a + thickness_w + i < height:
                mtx[center[1] + a + thickness_w + i - 1] = 0
            if center[1] - a - thickness_w - i > 1:
                mtx[center[1] - a - thickness_w - i] = 0
    # center = (width / 2, height / 2)
    # for row in range (len (mtx)):
    #     for col in range (len (mtx[row])):
    #         if (row - center[0]) ** 2 + (col - center[1]) ** 2 > 100 ** 2:
    #             mtx[row][col] = 0
    return mtx


if __name__ == '__main__':
    # crc = circle_pattern(1000,1000,10)
    # check_pattern(crc)
    # fraunhofer_fft(crc,100)

    # sqr = square_pattern (2044, 2044, 80)
    # check_pattern (sqr)
    # fraunhofer_fft (sqr)

    sprl = spiral_pattern(100, 100, 4, 2, 6)
    check_pattern(sprl)
    fraunhofer_fft(sprl)
    #
    # grid = grid_pattern(100,100,4,4)
    # check_pattern(grid)
    # fraunhofer_fft(grid)
    #
    # multi = multi_square_pattern (100, 100, 2, 2)
    # check_pattern (multi)
    # fraunhofer_fft(multi)
    #
    # hexa = hexagon_pattern(1000,1000,20)
    # check_pattern(hexa)
    # fraunhofer_fft (hexa,10000)
