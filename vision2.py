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
from CursorController import CursorController


player = Player()
cursorController = CursorController()

player.moveTo(42.79, 43.30)

time.sleep(1)

mouse.press(Button.right)
for i in range(50):
    time.sleep(0.05)
    mouse.move(0, i)
mouse.release(Button.right)    

time.sleep(1)
print('cursor to ore')
cursorController.toOre()
print('next to ore')
cursorController.moveNextToOre()
print('descending')
player.descend()
pyautogui.press('c')
print('cursor to ore')
cursorController.toOre(8) # use recu/rsive to make sure the cursor is at the ore
print('moving to ore')
player.moveToOre()
print('mining ore')
player.mineOre() 
print('ascending')
player.ascend(4)

# cursor = Cursor()
     
# time.sleep(1)

# player.moveTo(51.78, 27.97)

# move cursor to ore

# cursor.toOre()
# cursor.moveNextToOre()
# player.descend()
# cursor.toOre()
# player.moveToOre() # TODO: read movespeed
# player.mineOre()
# player.ascend(20)
# player.goToNextOre()



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