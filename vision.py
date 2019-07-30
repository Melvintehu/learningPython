try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import pyautogui
from pytesseract import Output
import time

width, heigth = pyautogui.size()

def makeCoordinateImage():
    coordinateImg = pyautogui.screenshot(region=(0, 25, 140, 20))
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
            coordinates.append(x)

    return coordinates


def moveTo(x, y):
    coordinates = getCurrentCoordinates()
    pyautogui.keyDown('w')

    while True:
        if isfloat(coordinates[0]) and isfloat(coordinates[1]):
            print(coordinates[0], coordinates[1])
            moveToDestination(coordinates[0], coordinates[1], x, y)

        coordinates = getCurrentCoordinates()

def destinationReached(x, y, destinationX, destinationY):
    return x == destinationX and y == destinationY


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def moveToDestination(x, y, destinationX, destinationY):
    if isfloat(x) and isfloat(y):
        coordinates = getCurrentCoordinates()
        newX = coordinates[0]
        newY = coordinates[1]
        

        if float(destinationX) - float(x) < float(destinationX) - float(newX):
            pyautogui.keyDown('d')
            time.sleep(0.1)
            pyautogui.keyUp('d')

        if float(destinationY) - float(y) < float(destinationY) - float(newY):
            pyautogui.keyDown('d')
            time.sleep(0.1)
            pyautogui.keyUp('d')



time.sleep(4)
moveTo(50.00, 32.00)

# def walkTo(posX, posY):
    # make a new screenshot
    # get the coordinates of the screenshot
    # check if destination is reaced


#     # start walking in a random direction
#     # get the coordinates and check if you are walking into the right direction
#     # if the coordinates are futher adway from the target posX and posY, change direction using the a,s,w,d keys
#     # repeat until the destination has been reachedwww

# def clickNode():
#     # when the player has arrived at a certain coordinate
#     # try to detect the color of the node within a screenshot
#     # the area with the most dense matching pixel colors is the node
#     # click the node
#     # make a chat screenshot
#     # check if the player has looted new ores.
