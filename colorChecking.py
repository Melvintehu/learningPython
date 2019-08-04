import cv2
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import colors

from mpl_toolkits.mplot3d import Axes3D  # noqa
from matplotlib.colors import hsv_to_rgb
light_orange = (145,12,254)
dark_orange = (161,78,232)

lo_square = np.full((10, 10, 3), light_orange, dtype=np.uint8) / 255.0
do_square = np.full((10, 10, 3), dark_orange, dtype=np.uint8) / 255.0

plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.show()


green = np.uint8([[[0, 108, 255]]]) #here insert the bgr values which you want to convert to hsv
print(green)
hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

print(hsvGreen)

lowerLimit = hsvGreen[0][0][0] - 10, 100, 100
upperLimit = hsvGreen[0][0][0] + 10, 255, 255

print(lowerLimit, upperLimit)