from physics import hitbox
from updatedGraphics import Point
from updatedGraphics import Image


class Fruit(object):
    def __init__(self):
        self.HP = 0
        self.xPos = 0
        self.yPos = 0
        self.xVelocity = 0
        self.yVelocity = 0
        self.image = None
        self.hitbox = None


    def quickAttack(self):
        pass

    def secondaryAttack(self):
        pass

    def utility(self):
        pass

    def ultimate(self):
        pass

    def getImage(self):
        return self.image