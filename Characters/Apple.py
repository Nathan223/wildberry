from Characters.Fruit import Fruit


class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        self.image = "ImagesAndSprites/Apple.gif"

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