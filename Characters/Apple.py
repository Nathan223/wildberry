from Characters.Fruit import Fruit
from graphics import Point
from hitbox import hitbox


class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        self.image = "ImagesAndSprites/Apple.gif"
        self.mvtSpeed = 5


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