import numpy as np
import pandas as pd
import os
import utils

def preprocess_data(acc_filename, gyro_filename):
    # load data as dataframe
    acc_df = pd.read_csv(acc_filename, sep=',',header=0)
    gyro_df = pd.read_csv(gyro_filename, sep=',',header=0)

    # dataframe to numpy array
    acc = np.asarray([
        acc_df['Time (s)'].to_numpy(dtype=float),
        acc_df['X (m/s^2)'].to_numpy(dtype=float), 
        acc_df['Y (m/s^2)'].to_numpy(dtype=float), 
        acc_df['Z (m/s^2)'].to_numpy(dtype=float)
    ])
    gyro = np.asarray([
        gyro_df['Time (s)'].to_numpy(dtype=float),
        gyro_df['X (rad/s)'].to_numpy(dtype=float), 
        gyro_df['Y (rad/s)'].to_numpy(dtype=float), 
        gyro_df['Z (rad/s)'].to_numpy(dtype=float)
    ])

    acc_norm = np.linalg.norm(acc[1::], axis=0)
    acc_norm = np.array([acc[0], acc_norm])
    gyro_norm = np.linalg.norm(gyro[1::], axis=0)
    gyro_norm = np.array([gyro[0], gyro_norm])

    filtered_acc_norm = utils.weighted_moving_average(acc_norm, dim=1, wl=21)
    filtered_gyro_norm = utils.weighted_moving_average(gyro_norm, dim=1, wl=21)

    filtered_acc_all = np.concatenate([np.expand_dims(acc[0], 0), utils.weighted_moving_average(acc[1::], dim=1, wl=21)],  axis=0)
    filtered_gyro_all = np.concatenate([np.expand_dims(gyro[0], 0), utils.weighted_moving_average(gyro[1::], dim=1, wl=21)],  axis=0)

    filename = os.path.basename(os.path.dirname(acc_filename))

    np.save("preprocessed_data/" + filename + "_acc_norm.npy", filtered_acc_norm)
    np.save("preprocessed_data/" + filename + "_gyro_norm.npy", filtered_gyro_norm)
    np.save("preprocessed_data/" + filename + "_acc_all.npy", filtered_acc_all)
    np.save("preprocessed_data/" + filename + "_gyro_all.npy", filtered_gyro_all)