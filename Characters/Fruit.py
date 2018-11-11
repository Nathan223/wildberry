from physics2 import hitbox
from graphics import Point, Image


INITIAL_JUMP_SPEED = 10

class Fruit(object):
    def __init__(self, img):
        self.maxHP = 0
        self.xPos = 0
        self.yPos = 0
        self.xVelocity = 0
        self.yVelocity = 0
        self.image = img
        self.hb = None
        self.mvtSpeed = None
        self.imageFile = None

    def setPos(self, x, y):
        currentX = self.getCenter().getX()
        currentY = self.getCenter().getY()
        self.move(x - currentX, y - currentY)

    def jump(self):
        self.setYForce(INITIAL_JUMP_SPEED)

    def slam(self):
        self.addYForce(self.fruit.mvtSpeed * -3)

    def right(self):
        self.setXForce(self.fruit.mvtSpeed)

    def left(self):
        self.addXForce(self.fruit.mvtSpeed * -1)

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

    def setHB(self):
        self.hb = (self.image,1)

    def getImageFile(self):
        return self.imageFile