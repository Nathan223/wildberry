<<<<<<< HEAD
from Fruit import Fruit


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
=======
from Fruit import Fruit


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
>>>>>>> db4992b12f3c154c67fc554fef579dab57fa28e2
        return self.image