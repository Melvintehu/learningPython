from Player import Player
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Listener
import pyscreenshot as ImageGrab
mouse = Controller()



player = Player()
# time.sleep(1)
  
# player.moveTo(51.78, 27.97)
position = player.findOre()
mousePosition = mouse.position
mouse.position = (position[0], position[1])
mouse.click(Button.right)
time.sleep(2)
mouse.click(Button.right)

