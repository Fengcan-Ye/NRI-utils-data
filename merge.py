import numpy as np

vel_train_1 = np.load('data/vel_train_part1_springs5.npy')
vel_train_2 = np.load('data/vel_train_part2_springs5.npy')
np.save('data/vel_train.springs5.npy', np.stack([vel_train_1, vel_train_2], axis=0))

loc_train_1 = np.load('data/loc_train_part1_springs5.npy')
loc_train_2 = np.load('data/loc_train_part2_springs5.npy')
np.save('data/loc_train.springs5.npy', np.stack([loc_train_1, loc_train_2], axis=0))