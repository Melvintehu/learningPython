try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import pytesseract
from pytesseract import Output
import pyautogui

class ScreenCoordinates:

    def getScreenCoordinates(self):
        img = self.makeCoordinateImage()
        coordinateData = pytesseract.image_to_data(img, output_type=Output.DICT)['text']
        return self.normalizeCoordinates(self.removeDiscrepanties(coordinateData))

    def normalizeCoordinates(self, coordinates):
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

    def makeCoordinateImage(self):
        #coordinates voor thuis laptop: 5, 33, 180, 27
        #coordinates voor kantoor desktop: 0, 25, 160, 25

        coordinateImg = pyautogui.screenshot(region=(0, 25, 160, 25))
        coordinateImg.save(r"C:/Users/Melvin Tehubijuluw/Desktop/shadowbot/coordinates.png")
        
        return coordinateImg

    def removeDiscrepanties(self, coordinateData):
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

        return coordinates