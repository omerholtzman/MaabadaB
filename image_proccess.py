import cv2
from simulation import *
from skimage.metrics import structural_similarity

def ssim(imageA,imageB):
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print(f"SSIM: {score}")

def centerize(mtx):
    maxx = np.unravel_index (np.argmax (mtx, axis=None), mtx.shape)
    center = (int(np.ceil(mtx.shape[0] / 2)), int(np.ceil(mtx.shape[1] / 2)))
    side = np.min(mtx.shape)
    diff = (center[0]-maxx[0], center[1]-maxx[1])
    new = np.zeros_like(mtx)
    for row in range(len(mtx)):
        for col in range(len(mtx[0])):
            if 0 <= row+diff[0] < side and 0 <= col+diff[1] < side:
                new[row+diff[0]][col+diff[1]] = mtx[row][col]
    return new


def load_image(file_name):
    img = cv2.imread (file_name, 0)
    img = centerize(img)
    img = noramlize(img)
    plt.imshow (img, vmin=0, vmax=256)
    plt.title("real image")
    plt.colorbar ()
    plt.show ()
    return img


if __name__ == '__main__':
    sqr = r'pictures\square.jpg'
    img_sqr = load_image (sqr)

    grid_thk = r'pictures\grid\thick.jpg'
    img_grd_thk = load_image (grid_thk)

    grid_thn = r'pictures\grid\thin.jpg'
    img_grd_thn = load_image (grid_thn)

    hex = r'pictures\heaxgons.jpg'
    img_hex = load_image (hex)

    sprl_thk = r'pictures\spirales\thickest.jpg'
    img_sprl_thk = load_image (sprl_thk)

    sprl_thn = r'pictures\spirales\thinest.jpg'
    img_sprl_thn = load_image (sprl_thn)

    sprl_mid = r'pictures\spirales\mid.jpg'
    img_sprl_mid = load_image (sprl_mid)
