# -*- coding: utf-8 -*-
#
# Developed by Haozhe Xie <cshzxie@gmail.com>

import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def get_volume_views(volume, save_dir, n_itr):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    volume = np.swapaxes(volume,2,1)
    volume = volume.squeeze().__ge__(0.5)
    fig = plt.figure()
    ax = fig.gca(projection=Axes3D.name)
    # ax.set_box_aspect([1,1,1])
    ax.set_aspect('auto')
    ax.voxels(volume, edgecolor="k")

    save_path = os.path.join(save_dir, 'voxels-%03d.png' % n_itr)
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()
    plt.close()
    return cv2.imread(save_path)
