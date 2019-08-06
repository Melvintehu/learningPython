from pynput.mouse import Button, Controller
import pyautogui


class Cursor:
    mouse = Controller()
    
    def moveNextToOre():
        for i in range(10):
            time.sleep(0.05)
            self.mouse.move(0, 1)

    def toOre(self):
        width, height = pyautogui.size()
        img = pyautogui.screenshot()
        img.save(r"C:/Users/Melvin Tehubijuluw/Desktop/shadowbot/ore.png")
        # img =  self.changeImg(r"C:/Users/Melvi/Desktop/shadowbot/ore.png")
        

        for x in range(400):
            for y in range(height-200):
                pX = (width / 2 - 200) + x
                pY = y + 100
                output = img.getpixel((pX, pY))
                r = output[0]
                g = output[1]
                b = output[2]

                rangePix = [
                    [255, 255, 255], 
                    [180, 192, 247],
                    [254, 253, 255],
                    [196, 207, 254],
                    [224, 234, 255],     
                    [160, 170, 222],       
                    [134, 142, 187],    
                    [186, 184, 193],
                    [248, 255, 255], 
                    [184, 196, 250],
                    [228, 243, 255],
                    [219, 230, 255],   
                    [165, 178, 230], # darker
                    [188, 204, 254]
                ]
                
                for i, val in enumerate(rangePix):
                    if(r == val[0] and g == val[1] and b == val[2]):
                        mousePosition = self.mouse.position
                        x = mousePosition[0] - pX
                        y = mousePosition[1] - pY
                        pyautogui.moveRel(-x, -y, 0.8)
                        return [pX, pY]