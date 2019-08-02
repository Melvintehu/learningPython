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


def makeCoordinateImage():
    #coordinates voor thuis laptop: 0, 34, 180, 25
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
    

    while not(inRangeOfDestination(desX, desY, coordinates[0], coordinates[1])):
        
        print(coordinates)
        
   
        if coordinates[0] != '' and coordinates[1] != '':
            moveToDestination(desX, desY, coordinates[0], coordinates[1])

        if inRangeOfDestination(desX, desY, coordinates[0], coordinates[1]):
            pyautogui.keyDown('w')

        coordinates = getCurrentCoordinates()

    pyautogui.keyDown('w')


def inRangeOfDestination(desX, desY, x, y):
    if x == '' or y == '':
        return False

    return abs(desX - x) < 1 and abs(desY - y) < 1

oldDX = 0
oldDY = 0
oldLength = 0
oldX = 0
oldY = 0

moveKeysLookUp = {
    "topLeft":  {
        "topRight": "right",
        "bottomRight": "right",
        "bottomLeft": "left",
        "topLeft": "stay",
    },
    "topRight":  {
        "topLeft": "left",
        "bottomRight": "right",
        "bottomLeft": "right",
        "topRight": "stay",
    },
    "bottomRight":  {
        "topLeft": "left",
        "topRight": "left",
        "bottomLeft": "right",
        "bottomRight": "stay",
    },
    "bottomLeft":  {
        "topLeft": "right",
        "topRight": "right",
        "bottomRight": "left",
        "bottomLeft": "stay",
    },
}


def moveToDestination(desX, desY, x, y):
    global oldDX
    global oldDY
    global oldLength
    global mouse
    global oldX
    global oldY
    global moveKeysLookUp

    # Get the directions 

    currentDirection = getDirection(x, y, oldX, oldY)
    destinationDirection = getDirection(x, y, desX, desY)
    turnKey = moveKeysLookUp[destinationDirection][currentDirection]

    print('the current Direction', currentDirection)
    print('the destination direction is', destinationDirection)
    print('tuning to ', turnKey)

    dx = desX - x
    dy = desY - y

    length = np.sqrt(dx*dx+dy*dy)

    if(oldLength < length or (oldDX < dx and dx > 0) or (oldDY < dy and dy > 0)):
        width, height = pyautogui.size()
        pyautogui.keyUp('w')
        
        mouse.position = (width/2, height/2)

        # click the correct mouse button
        
        mouse.press(Button.right)

        
      
        # TODO: when destination is very close, change the direction less
        amountOfPixelsToTurn = 20
        for i in range(amountOfPixelsToTurn): 
            if turnKey == 'right':
                mouse.move(i, 0)            
            elif turnKey == 'left': 
                mouse.move(-i, 0)
            else:
                mouse.move(0, 0)

            time.sleep(0.05)

        # release the correct mouse button 
    
        mouse.release(Button.right)
      

        pyautogui.keyDown('w')
       

    oldDX = dx
    oldDY = dy
    oldLength = length


def getDirection(x, y, oldX, oldY):
    xIncreasing = True
    yIncreasing = True

    if (x - oldX) > 0:
        xIncreasing = True 
    else: 
        xIncreasing = False

    if (y - oldY) > 0:
        yIncreasing = True
    else:
        yIncreasing = False


    # Find the current direction the player is moving to
    if xIncreasing and yIncreasing:
        return "bottomRight"
    elif xIncreasing and not(yIncreasing):
        return "topRight"
    elif not(xIncreasing) and not(yIncreasing):
        return "topLeft"
    elif not(xIncreasing) and yIncreasing:
        return "bottomLeft"



time.sleep(4)
moveTo(30.07, 35.75)


# if x is increasing and y is decreasing direction = top right of the map
# if x is increasing and y is increasing direction = bottom right of the map
# if x is decreasing and y is decreasing direction = top left of the map
# if x is decreasing and y is increasing direction = bottom left of the map


# find out in what direction the destination is and use that to move the player to the left or right
    # is the direction topLeft, topRight, bottomLeft, bottomRight
    # is the player moveing to the topLeft, topRight, bottomLeft, bottomRight?




# use the green/yellow circles on the minimap to check if a node is present in the target location


