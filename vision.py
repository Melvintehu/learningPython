try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import pyautogui
from pytesseract import Output
import time
import numpy as np
from pynput.mouse import Button, Controller


width, heigth = pyautogui.size()
mouse = Controller()
oldDX = 0
oldDY = 0
oldLength = 0

def makeCoordinateImage():
    coordinateImg = pyautogui.screenshot(region=(0, 34, 180, 25))
    coordinateImg.save(r"C:/Users/Melvi/Desktop/shadowbot/coordinates.png")
    return coordinateImg


def getCurrentCoordinates():
    img = makeCoordinateImage()
    coordinateData = pytesseract.image_to_data(img, output_type=Output.DICT)['text']
    coordinates = []
  
    for x in coordinateData:
        if x != "":
            x = x.replace(',', '') 
            x = x.replace(')', '')        
            x = x.replace('(', '') 
            x = x.replace('[', '')
            x = x.replace(']', '')
            x = x.replace('-', '')
            coordinates.append(x)

    return normalizeCoordinates(coordinates)

def normalizeCoordinates(coordinates):
    normalizedCoordinates = []
    if len(coordinates) >= 2:
        normalizedCoordinates.append(coordinates[0])
        normalizedCoordinates.append(coordinates[1])
    else:
        normalizedCoordinates.append("")
        normalizedCoordinates.append("")

    for index, value in enumerate(normalizedCoordinates):
        tempValue = value.replace('.', '')
        if len(tempValue) == 4 and tempValue.isdigit():
            normalizedCoordinates[index] = float(value)
        else:
            normalizedCoordinates[index] = ""

    return normalizedCoordinates


def moveTo(desX, desY):
    coordinates = getCurrentCoordinates()
    

    while not(inRangeOfDestination(desX, desY, coordinates[0], coordinates[1])):
        
        print(coordinates)
        
   
        if coordinates[0] != '' and coordinates[1] != '':
            moveToDestination(desX, desY, coordinates[0], coordinates[1])

        
        
        if inRangeOfDestination(desX, desY, coordinates[0], coordinates[1]):
            pyautogui.keyDown('w')
        
        coordinates = getCurrentCoordinates()
        
    


def inRangeOfDestination(desX, desY, x, y):
    if x == '' or y == '':
        return False

    return abs(desX - x) < 1 and abs(desY - y) < 1

def moveToDestination(desX, desY, x, y):
    global oldDX
    global oldDY
    global oldLength
    global mouse

    dx = desX - x
    dy = desY - y

    length = np.sqrt(dx*dx+dy*dy)

    # dx /= length
    # dy /= length




    if(oldLength < length or (oldDX < dx and dx > 0) or (oldDY < dy and dy > 0)):
        width, height = pyautogui.size()
        pyautogui.keyUp('w')
        
        mouse.position = (width/2, height/2)
        mouse.press(Button.right)
        # TODO: when destination is very close, change the direction less
        amountOfPixelsToTurn = 20
        for i in range(amountOfPixelsToTurn): 
            mouse.move(i, 0)
            time.sleep(0.05)
        mouse.release(Button.right)
        pyautogui.keyDown('w')
       

    oldDX = dx
    oldDY = dy
    oldLength = length

time.sleep(4)
moveTo(30.07, 35.75)







