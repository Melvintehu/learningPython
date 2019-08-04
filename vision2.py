from Player import Player
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Listener

mouse = Controller()



player = Player()
time.sleep(1)
  
# player.moveUp(2)
player.moveTo(70.84, 39.32)
# player.moveDown()


