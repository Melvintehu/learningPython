try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import pytesseract
from pytesseract import Output
import pyautogui
import numpy as np
from skimage.morphology import opening
from skimage.morphology import disk

class Screen:


    dir = "Melvi"

    def getScreenRotation(self):
        img = self.makeAngleImage()
        rotationData = pytesseract.image_to_data(img, output_type=Output.DICT, \
           config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')['text']
        
        print(rotationData)

        if len(rotationData) == 1:
            return 0

        return int(rotationData[-1])

    def getPlayerSpeed(self):
        img = self.makePlayerSpeedImage()
        speedData = pytesseract.image_to_data(img, output_type=Output.DICT, \
           config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')['text']

        if len(speedData) > 1:
            speedData = self.removeDiscrepanties(speedData)
            return int(speedData[-1])
        return 0

    def getScreenCoordinates(self):
        img = self.makeCoordinateImage()
        coordinateData = pytesseract.image_to_data(img, output_type=Output.DICT, \
           config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789.,')['text']
        
        return self.normalizeCoordinates(coordinateData)

    def normalizeCoordinates(self, coordinates):
        coordinates = coordinates[-1].split(',')
        
        for index, val in enumerate(coordinates):
            coordinates[index] = float(val)

        return coordinates

    def makeCoordinateImage(self):
        #coordinates voor thuis laptop: 5, 33, 180, 27
        #coordinates voor kantoor desktop: 0, 25, 160, 25

        coordinateImg = pyautogui.screenshot(region=(5, 4, 185, 27))
        
        coordinateImg.save(r"C:/Users/{}/Desktop/shadowbot/coordinates.png".format(self.dir))
        
        return coordinateImg

    def makeAngleImage(self):

        angleImg = pyautogui.screenshot(region=(335, 3, 70, 28))
        angleImg.save(r"C:/Users/{}/Desktop/shadowbot/angle.png".format(self.dir))
        self.changeImg(r"C:/Users/{}/Desktop/shadowbot/angle.png".format(self.dir))

        return angleImg

    def makePlayerSpeedImage(self):
        img = pyautogui.screenshot(region=(555, 2, 65, 30))
        img.save(r"C:/Users/{}/Desktop/shadowbot/speed.png".format(self.dir))
        img = self.changeImg(r"C:/Users/{}/Desktop/shadowbot/speed.png".format(self.dir))

        return img


    def removeDiscrepanties(self, data):
        newData = []
  
        for x in data:
            if x != "":
                x = x.replace(',', '') 
                x = x.replace(')', '')        
                x = x.replace('(', '') 
                x = x.replace('[', '')
                x = x.replace(']', '')
                x = x.replace('-', '')
                x = x.replace('~', '')
                
                newData.append(x)

        return newData

    def changeImg(self, pathToImage):

        black = (0,0,0)
        white = (255,255,255)
        threshold = (160,160,160)

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