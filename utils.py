import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d, convolve1d

def plot_acc(data, type):
    fig = plt.figure()
    fig.set_figwidth(20)
    plt.suptitle("Accelerometer")

    if type == 'all':
        # X
        plt.subplot(3,1,1)
        plt.plot(data[0], data[1])
        plt.xlabel("Time (s)")
        plt.ylabel("X (m/s^2)")

        # Y
        plt.subplot(3,1,2)
        plt.plot(data[0], data[2])
        plt.xlabel("Time (s)")
        plt.ylabel("Y (m/s^2)")

        # Z
        plt.subplot(3,1,3)
        plt.plot(data[0], data[3])
        plt.xlabel("Time (s)")
        plt.ylabel("Z (m/s^2)")

    elif type == 'norm':
         # norm
        plt.plot(data[0], data[1])
        plt.xlabel("Time (s)")
        plt.ylabel("|a| (m/s^2)")

    plt.show()
    plt.close()

def plot_gyro(data, type):
    fig = plt.figure()
    fig.set_figwidth(20)
    plt.suptitle("Gyroscope")

    if type == 'all':
    # X
        plt.subplot(3,1,1)
        plt.plot(data[0], data[1])
        plt.xlabel("Time (s)")
        plt.ylabel("X (rad/s)")

        # Y
        plt.subplot(3,1,2)
        plt.plot(data[0], data[2])
        plt.xlabel("Time (s)")
        plt.ylabel("Y (rad/s)")

        # Z
        plt.subplot(3,1,3)
        plt.plot(data[0], data[3])
        plt.xlabel("Time (s)")
        plt.ylabel("Z (rad/s)")

    elif type == 'norm':
        plt.plot(data[0], data[1])
        plt.xlabel("Time (s)")
        plt.ylabel("|g| (rad/s)")

    plt.show()
    plt.close()

def weighted_moving_average(vol, dim=2, wl=16, sigma=4):
    '''
    :param vol: input volume
    :param dim: target dimension (0-2)
    :param wl: window length
    :param sigma: standard deviation of gaussian
    :return:
    '''
    # create 1d dirac impulse
    dirac = np.zeros(wl)
    dirac[int(wl // 2)] = 1
    gauss_weights = gaussian_filter1d(dirac, sigma=sigma)
    vol = convolve1d(vol, gauss_weights, axis=dim, mode='reflect', origin=0)
    return vol

#gets the base shift matrix for a particular g_b
def get_matrix(g_b):
    u_z = g_b
    u_x = np.cross(np.array([0,1,0]).T, u_z)
    u_y = np.cross(u_z, u_x)

    R = np.array([u_x/np.linalg.norm(u_x),
                u_y/np.linalg.norm(u_y),
                u_z/np.linalg.norm(u_z)])
    
    return R
