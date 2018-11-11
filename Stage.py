
from graphics import Image,Point,Rectangle
from physics2 import *
from graphics import Image,Point,Rectangle

class Stage(object):
    def __init__(self, window):
        self.pos1 = Point(0, 0)
        self.pos2 = Point(0, 0)
        self.platform1 = None
        self.hb = None

    def regStage(self,window):
        background = Image(Point(600,400),"ImagesAndSprites/StartScreen.gif")
        background.draw(window)
        self.platform1 = Image(Point(600,675),"ImagesAndSprites/blue.gif")
        self.platform1.draw(window)
        self.pos1 = Point(400,700)
        self.pos2 = Point(800,700)

    def getPos1(self):
        return self.pos1

    def getPos2(self):
        return self.pos2

    def regStageCreateHB(self):
        self.hb = hitbox(self.platform1,0)

    def getHB(self):
        return self.hb