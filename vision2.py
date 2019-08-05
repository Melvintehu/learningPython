from Player import Player
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Listener

mouse = Controller()



player = Player()
time.sleep(1)
  
player.moveTo(54.38, 36.11)
player.moveTo(37.12, 24.64)
player.moveTo(15.45, 31.64)
player.moveTo(11.95, 47.20)
player.moveTo(32.45, 62.18)
player.moveTo(71.31, 34.13)



