import pyautogui
from PIL import Image, ImageGrab
import time


def click(key):
    pyautogui.keyDown(key)
    return


def isCollision(data):
    for i in range(530, 560):
        for j in range(80, 127):
            if data[i, j] < 171:
                click("down")
                return

    for i in range(530, 620):
        for j in range(130, 160):
            if data[i, j] > 100:
                click("up")
                return

    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    print("3.. 2.. 1..")
    print("Started")
    while True:
        image = ImageGrab.grab().convert('L')
        img_data = image.load()
        isCollision(img_data)
