from PIL import Image
import keyboard
import time
import pyautogui

pyautogui.PAUSE = 0.00000001

def click(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

def get_change(path):
    
    img = Image.open(path)
    img = img.convert('1')

    # 获取屏幕的大小
    width, height = pyautogui.size()

    # 将图片缩放(视情况而定)
    img = img.resize((int(width*0.3), int(0.5*height)), Image.ANTIALIAS)


    pixels = img.load()

    width, height = img.size

    color = []
    locate = []

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            color.append(f"{pixel}")
            locate.append(f"[{x}, {y}]")

    color = [i.replace("255","1") for i in color]
    locate = [eval(i) for i in locate]

    img.save(r"D:/chicken.png")

    return color, locate

def start(color, locate):
    time.sleep(3)
    for i in range(len(locate)):
        if keyboard.is_pressed('q'):
            print("结束")
            break
        else:
            if color[i] == "0":
                click(locate[i][0]+800,locate[i][1]+200)
