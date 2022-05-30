import matplotlib.pyplot as plt
import numpy as np

def plot_acc(data):
    plt.figure()
    plt.suptitle("Accelerometer")
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
    
    plt.show()
    plt.close()

def plot_gyro(data):
    plt.figure()
    plt.suptitle("Gyroscope")
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

    plt.show()
    plt.close()