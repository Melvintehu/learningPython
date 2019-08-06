from Player import Player
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Listener
import pyscreenshot as ImageGrab
mouse = Controller()
import pyautogui
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

player = Player()
# time.sleep(1)
  
# player.moveTo(51.78, 27.97)
# position = player.findOre()
# mousePosition = mouse.position
# mouse.position = (position[0], position[1])
# mouse.click(Button.right)
# time.sleep(2)
# mouse.click(Button.right)

position = player.findOre()
mousePosition = mouse.position
x = mousePosition[0] - position[0]
y = mousePosition[1] - position[1]
pyautogui.moveRel(-x, -y, 0.8)
mouse.click(Button.right)
time.sleep(3)


position = player.findOre()
mousePosition = mouse.position
x = mousePosition[0] - position[0]
y = mousePosition[1] - position[1]
pyautogui.moveRel(-x, -y, 0.5)
mouse.click(Button.right)
time.sleep(3)

# position = player.findOre()
# mousePosition = mouse.position

# x = mousePosition[0] - position[0]
# y = mousePosition[1] - position[1]


# mouse.position = (x + position[0], y + position[1])
# mouse.click(Button.right)


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