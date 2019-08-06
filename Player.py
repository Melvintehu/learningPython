from pynput.mouse import Button, Controller
import pyautogui
import time
import math
import numpy as np
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyController
try:
    from PIL import Image
except ImportError:
    import Image
from skimage.morphology import opening
from skimage.morphology import disk

# custom classes
from Screen import Screen

class Player:
    
    mouse = Controller()
    keyboard = KeyController()

    oldX = 0
    oldY = 0
    x = 0
    y = 0

    def __init__(self):
        self.screen = Screen()
        # self.getPosition()

    def getPosition(self):
        self.oldX = self.x
        self.oldY = self.y
        
        coordinates = self.screen.getScreenCoordinates()
        self.x = coordinates[0]
        self.y = coordinates[1]
    
    def getRotation(self):
        return self.screen.getScreenRotation()

    def getRotationToTarget(self, desX, desY):
        AN = self.getRotation()
        AD = self.getAngle(desX, desY)
        print(AN, AD)
        exit()
        return AD - (360 - AN) 
    

    def moveTo(self, desX, desY):
        AN = self.getRotationToTarget(desX, desY)
        


    def rotateDegrees(self, angleInDegrees, turnSpeed = 0.05, direction = 1):
        self.mouse.press(Button.right)

        for i in range(math.floor((1600 / 360) *  angleInDegrees)):
            time.sleep(turnSpeed)
            self.mouse.move(direction * 1, 0)            
        self.mouse.release(Button.right) 

    def getAngle(self, desX, desY):
        self.getPosition()
        self.keyboard.press('s')
        time.sleep(1.5)
        self.keyboard.release('s')    
        self.getPosition()

        a = np.array([self.oldX, self.oldY])
        b = np.array([self.x, self.y])
        c = np.array([desX, desY])


        ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
        return ang + 360 if ang < 0 else ang

    def inLandingArea(self, desX, desY, marginX, marginY):
        if desX != '' and desY != '' and self.x != '' and self.y != '':
            return abs(desX - self.x) <= marginX and abs(desY - self.y) <= marginY

        return False



    def changeImg(self, pathToImage):

        black = (0,0,0)
        white = (255,255,255)
        threshold = (190,190,190)

        # Open input image in grayscale mode and get its pixels.
        img = Image.open(pathToImage).convert("LA")
        pixels = img.getdata()

        newPixels = []

        # Compare each pixel 
        for pixel in pixels:
            if pixel < threshold:
                newPixels.append(black)
            else:
                newPixels.append(white)

        # Create and save new image.
        newImg = Image.new("RGB",img.size)
        newImg.putdata(newPixels)
        newImg.save(pathToImage)
        return newImg


    def ascend(self, seconds):
        pyautogui.press('c')
        time.sleep(1.5)

        self.keyboard.press(Key.space)
        time.sleep(seconds)
        self.keyboard.release(Key.space)



    def descend(self):
        # read current speed from UI, if currentspeed is 0% you've reached the ground
       

        self.mouse.click(Button.right)
        time.sleep(0.5)
        while True:
            time.sleep(0.5)   

            if(self.getSpeed() == 0):
                return


    def moveToOre(self):
        self.mouse.click(Button.right)
        while True:
            time.sleep(1)   

            if(self.getSpeed() == 0):
                return

    def mineOre(self):
        time.sleep(1)
        self.mouse.click(Button.right)
        time.sleep(3.5)

    def getSpeed(self):
        return self.screen.getPlayerSpeed()