import math
import pyautogui as pg

class Mouse():
    def __init__(self):
        pass
    def distanceBetweenFingers(self, x, X, y, Y):
        distance = math.sqrt(((x-X)**2)+((y-Y)**2))
        #print(distance)
        return distance

    def leftClick(self, distance, x, y):
        if distance <= 80:
            pg.click(x, y)
    
    def rightClick(self, distance, x, y):
        if distance <= 80:
            pg.click(x, y)

    def updatePos(self, x, y):
        pg.moveTo(x, y)
    
