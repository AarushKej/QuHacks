import math
import pyautogui

class Mouse():
    def __init__(self):
        pass
    def distanceBetweenFingers(self, x, X, y, Y):
        distance = math.sqrt(((x-X)**2)+((y-Y)**2))
        print(distance)
        return distance

    def leftClick(distance):
        if distance <= 80:
            pyautogui.moveTo(500, 500)




    