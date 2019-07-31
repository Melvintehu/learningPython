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

width, heigth = pyautogui.size()

def makeCoordinateImage():
    coordinateImg = pyautogui.screenshot(region=(0, 25, 160, 25))
    coordinateImg.save(r"C:/Users/Melvin Tehubijuluw/Desktop/shadowbot/coordinates.png")
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
    

    while True:
        print(coordinates)
        pyautogui.keyDown('w')   
        
        if coordinates[0] != '' and coordinates[1] != '':
            moveToDestination(desX, desY, coordinates[0], coordinates[1])

        coordinates = getCurrentCoordinates()

oldDX = 0
oldDY = 0
oldLength = 0

def moveToDestination(desX, desY, x, y):
    global oldDX
    global oldDY
    global oldLength

    dx = desX - x
    dy = desY - y

    length = np.sqrt(dx*dx+dy*dy)

    # dx /= length
    # dy /= length
    print(oldDX, oldDY, oldLength)
    print(dx, dy, length)

    if(oldDX > dx or oldDY > dy or oldLength > length or dx < 0 or dy < 0 or length < 0):
        width, height = pyautogui.size()
        print(width, height)
        pyautogui.moveTo(width/2, height/2)
        pyautogui.dragTo(width/2 + 10, height/2 - 45, 0.5, button='right')
    

    oldDX = dx
    oldDY = dy
    oldLength = length

    # the length must always got to zero.






time.sleep(4)
moveTo(49.99, 49.99)

