from Player import Player
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Listener


mouse = Controller()
import pyautogui
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
import Cursor from Cursor


player = Player()
cursor = Cursor()

# time.sleep(1)

# player.moveTo(51.78, 27.97)

# move cursor to ore

cursor.toOre()
cursor.moveNextToOre()
player.descend() # TODO: read movespeed
cursor.toOre()
player.moveToOre() # TODO: read movespeed
player.mineOre()
player.ascend(20)
player.goToNextOre()



# nemo = cv2.imread('./ghostore.png')
# nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
# hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)


# h, s, v = cv2.split(hsv_nemo)
# fig = plt.figure()
# axis = fig.add_subplot(1, 1, 1, projection="3d")


# pixel_colors = nemo.reshape((np.shape(nemo)[0]*np.shape(nemo)[1], 3))
# norm = colors.Normalize(vmin=-1.,vmax=1.)
# norm.autoscale(pixel_colors)
# pixel_colors = norm(pixel_colors).tolist()

# axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
# axis.set_xlabel("Hue")
# axis.set_ylabel("Saturation")
# axis.set_zlabel("Value")
# plt.show()