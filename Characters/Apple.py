    from Characters.Fruit import Fruit
from graphics import Point
from physics2 import hitbox


class Apple(Fruit):
    def __init__(self, image):
        Fruit.__init__(self, image)
        self.imageFile= "ImagesAndSprites/Apple.gif"
        self.mvtSpeed = 5


    def quickAttack(self):
        pass

    def secondaryAttack(self):
        pass

    def utility(self):
        pass

    def ultimate(self):
        pass

    def getImageFile(self):
        return self.imageFile