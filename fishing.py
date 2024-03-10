import time
# imports ImageGrab for screenshot
from PIL import ImageGrab
import keyboard

white1 = (245,245,245) 
white2 = (246,245,246)
target_color = (60, 150, 60)  # The type of green used


# function to check color of pixel at (x, y)
def checkColor(x, y):
    # takes screenshot of 1x1 pixel at (x, y)
    im = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    # converts image to RGB forma
    rgbim = im.convert('RGB')
    # gets RGB value of top-left pixel
    (r,g,b) = rgbim.getpixel((0,0))
    # returns RGB value
    return (r,g,b)

print("Script started\n")

while True:
    # Capture a screenshot of the region
    # Get the RGB values of the pixel at the center of the region
   
    print(checkColor(883,1040))
    if checkColor(960,105) == target_color:
        print('Pulling Fish Now\n')
        keyboard.press('e')
        time.sleep(0.1)
        keyboard.release('e')
        time.sleep(0.1)
        keyboard.press('e')
        time.sleep(0.1)
        keyboard.release('e')
        print('Starting again')
        
    verif = checkColor(883,1040)
    if verif == white1 or verif == white2:
        #print('Color')
        #print(checkColor(883,1040))
        keyboard.press('e')
        time.sleep(0.1)
        keyboard.release('e')
        time.sleep(0.1)    
    
    # Wait for 1 second before checking again
    time.sleep(0.1)




