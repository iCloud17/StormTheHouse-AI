import pyautogui
#import keyboard
import time

def find_rgb(image, target_r, target_g, target_b, rng):
    #img = Image.open(imagename)
    pm = 20
    rgb = image.convert('RGB')
    for y in range(image.size[1]):
        for x in range(image.size[0]):
           r, g, b, = rgb.getpixel((x, y))
           if rng:
               if r >= target_r-pm and r <= target_r+pm and g >= target_g-pm and g <= target_g+pm and b >= target_b-pm and b <= target_b+pm:
                   return x, y 
           else:     
               if r == target_r and g == target_g and b == target_b:
                   return x, y 

    return -1, -1

def getGround(): 
    img = pyautogui.screenshot(region=(575, 695, 625, 220))
    return img

def getAmmo():
    img = pyautogui.screenshot(region=(590, 390, 5, 5))
    return img


while True:
    currentMouseX, currentMouseY = pyautogui.position()
    if currentMouseX < 1:
        break
while True:
    #if keyboard.is_pressed('p'):
        ammo = getAmmo()
        #ammo.save('ammo.png')
        amX, amY = find_rgb(ammo, 203, 209, 71, True)
        if amX == -1:
            print("RELOADING")
            pyautogui.press('space') #PRESS SPACE TO RELOAD
            time.sleep(1)
        ground = getGround()
        posx, posy = find_rgb(ground, 0, 0, 0, False)
        if posx != -1:
            #img.save('screenshot.png')
            posx += 575
            posy += 685
            print(posx)
            print(posy)
            pyautogui.click(posx+15, posy+4)
            pyautogui.click(posx+19, posy+4)
