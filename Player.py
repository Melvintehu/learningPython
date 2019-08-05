from pynput.mouse import Button, Controller
import pyautogui
import time
import math
import numpy as np
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyController

# custom classes
from ScreenCoordinates import ScreenCoordinates

class Player:
    
    mouse = Controller()
    keyboard = KeyController()

    oldX = 0
    oldY = 0
    x = 0
    y = 0

    def __init__(self):
        self.screenCoordinates = ScreenCoordinates()
        self.getPosition()

    def getPosition(self):
        self.oldX = self.x
        self.oldY = self.y
        
        coordinates = self.screenCoordinates.getScreenCoordinates()
        self.x = coordinates[0]
        self.y = coordinates[1]
    
   


    def rotate(self, desX, desY):   
        
        self.rotateRecursive(desX, desY)

        self.mouse.release(Button.right)

    def rotateRecursive(self, desX, desY):
        self.mouse.press(Button.right)
        angle = self.getAngle(desX, desY)
        if(angle < 5):
            return

        if angle > 180:
            self.rotateDegrees(abs(angle - 360), 0.01, -1)
        else:
            self.rotateDegrees(angle, 0.01)   
        self.mouse.release(Button.right)
        self.rotateRecursive(desX, desY)    
        print('rotating recursive')
   

    def moveTo(self, desX, desY):
        # STAGE 1:
        # turn the player to atleast face the direction of the target coordinates
        print('Stage 1: Shadowbot is trying to face the player to the right direction')
        
        self.rotate(desX, desY)
        
       
        print('Stage 2: shadowbot is flying to the destination.')
        #stage 4: fly to your destination
        # fly to the destination and stop at the exact destination
        self.keyboard.press('w')

        while not(self.inLandingArea(desX, desY)):
            self.getPosition()
            
            if self.inLandingArea(desX, desY):
                print('in landing area')
                self.keyboard.release('w')
                break
        
        self.keyboard.release('w')


        self.rotate(desX, desY)


        self.keyboard.press('w')

        while not(self.onTopOfDestination(desX, desY)):
            self.getPosition()
            
            if self.onTopOfDestination(desX, desY):
                print('in landing area')
                self.keyboard.release('w')
                break
        
        self.keyboard.release('w')


    def rotateDegrees(self, angleInDegrees, turnSpeed = 0.05, direction = 1):
        # pixelsToTurn = (1600 / (360 * (np.pi/180))) * angleInDegrees * (np.pi/180)
        pixelsToTurn = (1600 / 360) *  angleInDegrees
        print(math.floor(pixelsToTurn))
        pixelsToTurn = math.floor(pixelsToTurn)

        self.mouse.press(Button.right)

        for i in range(pixelsToTurn):
            time.sleep(turnSpeed)
            self.mouse.move(direction * 1, 0)            
        self.mouse.release(Button.right) 

    def turnDegrees(self, angleInDegrees, turnSpeed = 0.05, direction = 1):
        pixelsToTurn = (1567 / 360) *  angleInDegrees
        print(math.floor(pixelsToTurn))
        pixelsToTurn = math.floor(pixelsToTurn)

        self.mouse.press(Button.right)

        for i in range(pixelsToTurn):
            time.sleep(turnSpeed)
            self.mouse.move(direction * 1, 0)            
        self.mouse.release(Button.right)            
        

    def getAngle(self, desX, desY):
        self.getPosition()
        self.keyboard.press('s')
        time.sleep(1)
        self.keyboard.release('s')    
        self.getPosition()

        a = np.array([self.oldX, self.oldY])
        b = np.array([self.x, self.y])
        c = np.array([desX, desY])


        ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
        return ang + 360 if ang < 0 else ang

    def inLandingArea(self, desX, desY):
        if desX != '' and desY != '' and self.x != '' and self.y != '':
            return abs(desX - self.x) <= 5 and abs(desY - self.y) <= 5

        return False

    def onTopOfDestination(self, desX, desY):
        if desX != '' and desY != '' and self.x != '' and self.y != '':
            return abs(desX - self.x) <= 0.1 and abs(desY - self.y) <= 0.1

        return False

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



     
        