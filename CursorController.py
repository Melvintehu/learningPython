from pynput.mouse import Button, Controller
from skimage.morphology import opening
from skimage.morphology import disk
try:
    from PIL import Image
except ImportError:
    import Image
import pyautogui
import time

class CursorController:
    mouse = Controller()
    imgDir = "Melvi"
    def moveNextToOre(self):
        
        for i in range(40):
            time.sleep(0.05)
            self.mouse.move(0, 1)

    def toOre(self, surroundingPixelAmount = 5):
        width, height = pyautogui.size()
        img = pyautogui.screenshot()
        img.save(r"C:/Users/{}/Desktop/shadowbot/ore.png".format(self.imgDir))
        # img =  self.changeImg(r"C:/Users/Melvi/Desktop/shadowbot/ore.png")
        

        for x in range(600):
            for y in range(height-300):
                pX = (width / 2 - 300) + x
                pY = y + 100
                output = img.getpixel((pX, pY))
                r = output[0]
                g = output[1]
                b = output[2]

                rangePix = [
                    [255, 255, 255], 
                    # [248, 248, 255],
                ]
                
                found = False
                for i, val in enumerate(rangePix):
                    if(r > 240 and g > 240 and b > 240):
                        
                        for i in range(surroundingPixelAmount):
                            surroundingPixel = img.getpixel((pX + i, pY + i))
                            sR = surroundingPixel[0]
                            sG = surroundingPixel[1]
                            sB = surroundingPixel[2]
                            print(sR, sG, sB)
                            if(sR < 220 and sG < 220 and sB < 240 ):
                                found = False    
                            else:
                                found = True

                        mousePosition = self.mouse.position
                        x = mousePosition[0] - pX
                        y = mousePosition[1] - pY
                        pyautogui.moveRel(-x, -y, 0.3)
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