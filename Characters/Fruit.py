from hitbox import hitbox
from graphics import Point, Image


class Fruit(object):
    def __init__(self):
        self.HP = 0
        self.xPos = 0
        self.yPos = 0
        self.xVelocity = 0
        self.yVelocity = 0
        self.image = None
        self.mvtSpeed = 0

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