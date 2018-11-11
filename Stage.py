from updatedGraphics import Image,Point,Rectangle
from physics2 import *

class Stage(object):
    def __init__(self, window):
        self.pos1 = Point(0, 0)
        self.pos2 = Point(0, 0)

    def regStage(self,window):
        background = Image(Point(600,400),"ImagesAndSprites/StartScreen.gif")
        background.draw(window)
        stage = Rectangle(Point(200,650),Point(1000,700))
        stage.setFill("Blue")
        stage.draw(window)
        self.hb = hitbox(800, 50, 0)
        self.hb.position = [stage.getCenter().getX(), stage.getCenter().getY()]
        self.pos1 = Point(400,700)
        self.pos2 = Point(800,700)

    def getPos1(self):
        return self.pos1

    def getPos2(self):
        return self.pos2