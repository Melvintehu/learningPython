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


    def findOre(self):
        width, height = pyautogui.size()
        img = pyautogui.screenshot()
        # img.save(r"C:/Users/Melvi/Desktop/shadowbot/ore.png")
        # img =  self.changeImg(r"C:/Users/Melvi/Desktop/shadowbot/ore.png")

        for x in range(200):
            for y in range(200):
                pX = (width / 2 - 100) + x
                pY = (height / 2 - 100) + y
                output = img.getpixel((pX, pY))
                r = output[0]
                g = output[1]
                b = output[2]

                rangePix = [
                    [255, 255, 255], 
                    [202, 227, 255], 
                    [136, 154, 189],
                    [88, 102, 126],
                    [79, 90, 113],
                    [115, 128, 157],
                    [52, 57, 69],
                    [173, 198, 245],
                    
                    

                ]
                
                for i, val in enumerate(rangePix):
                    if(r == val[0] and g == val[1] and b == val[2]):
                        return [pX, pY]



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










    def moveUp(self, seconds):
        self.keyboard.press(Key.space)
        time.sleep(1)
        self.keyboard.release(Key.space)

        self.mouse.press(Button.right)
        for i in range(50):
            time.sleep(0.05)
            self.mouse.move(0, -i)

        self.mouse.press(Button.left)
        time.sleep(seconds)
        self.mouse.release(Button.left)
        
        for i in range(25):
            time.sleep(0.05)
            self.mouse.move(0, i)
        self.mouse.release(Button.right)


    def moveDown(self):
        time.sleep(2)
        self.mouse.press(Button.right)
        for i in range(50):
            time.sleep(0.05)
            self.mouse.move(0, i)

        self.mouse.press(Button.left)

        self.getPosition()
        time.sleep(1)
        self.getPosition()
        self.moveDownRecursive()
        self.mouse.release(Button.left)
        self.mouse.release(Button.right)
        self.keyboard.press('s')
        print('shadowbot moving backwards to match the node')
        time.sleep(5)
        self.keyboard.release('s')

    def moveDownRecursive(self):
        if abs(self.x - self.oldX) > 0.2:
            return

        self.getPosition()
        self.moveDownRecursive()



     
        