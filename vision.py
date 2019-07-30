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
    coordinateImg = pyautogui.screenshot(region=((width / 2) - 80, 30, 85, 20))
    coordinateImg.save(r"C:/Users/Melvi/Desktop/shadowbot/coordinates.png")
    return coordinateImg;




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

time.sleep(2)
coordinateImg = makeCoordinateImage()
print(getCoordinatesFromImage(coordinateImg))

# def walkTo(posX, posY):
    # make a new screenshot
    # get the coordinates of the screenshot
    # 


#     # start flying up high in the air
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
