try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import pyautogui
from pytesseract import Output
import time

def getCoordinatesFromImage(img):
    coordinateData = pytesseract.image_to_data(img, output_type=Output.DICT)['text']
    x = 0
    y = 0
    coordinates = []

    for x in coordinateData:
        if x != "":
            x = x.replace(',', '')        
            coordinates.append(x)

    return coordinates



for x in range(10):        
    
    img = cv2.imread(r'coordinates.png')
    print(getCoordinatesFromImage(img))


# def walkTo(posX, posY):
#     # start flying up high in the air
#     # start walking in a random direction
#     # get the coordinates and check if you are walking into the right direction
#     # if the coordinates are futher away from the target posX and posY, change direction using the a,s,w,d keys
#     # repeat until the destination has been reached

# def clickNode():
#     # when the player has arrived at a certain coordinate
#     # try to detect the color of the node within a screenshot
#     # the area with the most dense matching pixel colors is the node
#     # click the node
#     # make a chat screenshot
#     # check if the player has looted new ores.
