import time
from PIL import ImageGrab
import keyboard

alb1 = (245,245,245) 
alb2 = (246,245,246)
target_color = (60, 150, 60)  # verde pescar
def checkColor(x, y):
    im = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    rgbim = im.convert('RGB')
    (r,g,b) = rgbim.getpixel((0,0))
    return (r,g,b)

print("Script started\n")
while True:
    # Capture a screenshot of the region
    # Get the RGB values of the pixel at the center of the region
   
    print(checkColor(883,1040))
    if checkColor(960,105) == target_color:
        print('TRAGE PESTILI\n')
        keyboard.press('e')
        time.sleep(0.1)
        keyboard.release('e')
        time.sleep(0.1)
        keyboard.press('e')
        time.sleep(0.1)
        keyboard.release('e')
        print('L-am tras, acum incep iar')
        

    verif = checkColor(883,1040)
    if verif == alb1 or verif == alb2:
        #print('Culoare')
        #print(checkColor(883,1040))
        keyboard.press('e')
        time.sleep(0.1)
        keyboard.release('e')
        time.sleep(0.1)    
    
    # Wait for 1 second before checking again
    time.sleep(0.1)




