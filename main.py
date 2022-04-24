from image_proccess import *
from simulation import *


def MSE(diff):
    mse = np.square (diff).mean ()


def compare_real_and_simulated(real, simulated):
    diff = simulated - real
    check_pattern (diff, "difference")

def square():
    img = r'pictures\square.jpg'
    real = load_image (img)
    width, height = real.shape
    multi = multi_square_pattern(width*10,height*10,14,6)
    check_pattern (multi, "hole", 1)
    simulated = fraunhofer_fft (multi)
    compare_real_and_simulated (real, simulated)


def thick_grid():
    img = r'pictures\grid\thick.jpg'
    real = load_image (img)
    width, height = real.shape
    grid = grid_pattern (width, height, 40, 40)
    check_pattern (grid,lim=1)
    simulated = fraunhofer_fft (grid)


    return simulated
    # compare_real_and_simulated (real, simulated)


def thin_grid():
    img = r'pictures\grid\thin.jpg'
    real = load_image (img)
    width, height = real.shape
    grid = grid_pattern (width*4-4, height*4, 20, 20)
    check_pattern (grid,lim=1)
    simulated = fraunhofer_fft (grid)



def hexagon():
    img = r'pictures\heaxgons.jpg'
    real = load_image (img)
    width, height = real.shape
    hexa = hexagon_pattern (width, height, 20)
    check_pattern (hexa)
    simulated = fraunhofer_fft (hexa)
    ssim(real,simulated)


def spiral_thick():
    img = r'pictures\spirales\thickest.jpg'
    real = load_image (img)
    width, height = real.shape
    sprl = spiral_pattern (width//2, height//2, 40, 40, 20)
    check_pattern (sprl)
    simulated = fraunhofer_fft (sprl)


def spiral_thin():
    img = r'pictures\spirales\thinest.jpg'
    real = load_image (img)
    width, height = real.shape
    sprl = spiral_pattern (width//2, height//2, 8, 8, 4)
    check_pattern (sprl)
    simulated = fraunhofer_fft (sprl)


def spiral_mid():
    img = r'pictures\spirales\mid.jpg'
    real = load_image (img)
    width, height = real.shape
    sprl = spiral_pattern (width//2, height//2, 20, 20, 10)
    check_pattern (sprl)
    simulated = fraunhofer_fft (sprl)


def send_to_middle(matrix, thresh: float = 0.05):
    SCALER = 2
    SECOND_SCALER = 1
    INCREASE_AMPLITUDE = 4
    DECREASE_AMPLITUDE = 2
    center_location = len(matrix) // 2 - 1
    edge_size = len(matrix) // 2 - 1
    for i in range(edge_size - 1):
        for j in range(-edge_size + 1, edge_size - 1):
            if matrix[center_location + i][center_location + j] > thresh:
                matrix[center_location + i // SCALER * SECOND_SCALER][center_location + j // SCALER * SECOND_SCALER] = matrix[center_location + i][center_location + j] * INCREASE_AMPLITUDE
                matrix[center_location + i][center_location + j] = matrix[center_location + i][center_location + j] / DECREASE_AMPLITUDE

            if matrix[center_location - i][center_location + j] > thresh:
                matrix[center_location - i // SCALER * SECOND_SCALER][center_location + j // SCALER * SECOND_SCALER] = matrix[center_location - i][
                    center_location + j] * INCREASE_AMPLITUDE
                matrix[center_location - i][center_location + j] = matrix[center_location - i][center_location + j] / DECREASE_AMPLITUDE

            if matrix[center_location + j][center_location - i] > thresh:
                matrix[center_location + j // SCALER * SECOND_SCALER][center_location - i // SCALER * SECOND_SCALER] = matrix[center_location + j][
                    center_location - i] * INCREASE_AMPLITUDE
                matrix[center_location + j][center_location - i] = matrix[center_location + j][center_location - i] / DECREASE_AMPLITUDE

            if matrix[center_location + j][center_location + i] > thresh:
                matrix[center_location + j // SCALER * SECOND_SCALER][center_location + i // SCALER * SECOND_SCALER] = matrix[center_location + j][
                    center_location + i] * INCREASE_AMPLITUDE
                matrix[center_location + j][center_location + i] = matrix[center_location + j][center_location + i] / DECREASE_AMPLITUDE
    return matrix


def decrease_size():
    matrix = send_to_middle (thick_grid ())
    print (matrix)
    plt.imshow (matrix, vmin=0, vmax=1)
    plt.title ("")
    plt.colorbar ()
    plt.show ()



if __name__ == '__main__':
    # square ()
    # thick_grid()
    # thin_grid ()
    # hexagon ()
    # spiral_thick ()
    spiral_thin ()
    # spiral_mid ()

    # crc = circle_pattern(1000,1000,10)
    # check_pattern(crc)
    # fraunhofer_fft(crc,100)

    # multi = multi_square_pattern (100, 100, 2, 2)
    # check_pattern (multi)
    # fraunhofer_fft(multi)
