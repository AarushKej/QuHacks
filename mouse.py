import math
import pyautogui as pg

class Mouse():
    def __init__(self):
        self.right_down = False
        self.left_down = False
        self.current_pos = None
        self.prev_pos = None

    def distanceBetweenFingers(self, x, X, y, Y):
        distance = math.sqrt(((x-X)**2)+((y-Y)**2))
        #print(distance)
        return distance

    def leftClick(self, distance, x, y):
        if distance <= 70:
            pg.click(x, y)
    
    def drag(self, distance, x, y):
        if  distance <= 70:
            pg.dragTo(x, y, button="left")
    
    def rightClick(self, distance, x, y):
        if distance <= 70:
            pg.click(x, y, button="right")

    def updatePos(self, x, y):
        pg.moveTo(x, y)
