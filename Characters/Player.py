from Characters.Apple import Apple
from physics2 import hitbox

class Player(object):
    def __init__(self,fruit, id):
        self.lives = 3
        self.currentHP = 100
        self.id = id
        self.fruit = fruit

    def getFruit(self):
        return self.fruit

    #def setImage(self,img):
       # self.image = img


   # def getImageFile(self):
       # return self.imageFile

# this function should be kept, it sets the position
# instead of moving it


    #
    # window = GraphWin("Jump test", 640, 480)
    # window.setBackground("white")
    #
    # # Hitbox defines as hitbox(XRANGE, YRANGE, WEIGHT)
    # plyJump = hitbox(25, 25, 1)
    # platform = hitbox(500, 1.5, 0)
    #
    # # This is just the objects
    # plyJumpRender = Rectangle(Point(0, 0), Point(50, 50))
    # plyJumpRender.setFill("black")
    # plyJumpRender.draw(window)
    #
    # worldRenderer = Rectangle(Point(0, 0), Point(500, 3))
    # worldRenderer.setFill("red")
    # worldRenderer.draw(window)
    #
    # # Set the beginning position as [XPOS, YPOS]
    # platform.position = [640/2, 480/2]
    # plyJump.position = [220, 5]
    #
    # while True:
    #     # Controls
    #     controls = window.checkKeys()
    #     if "w" in controls and plyJump.inAir == False:
    #         p1.jump()
    #     if "s" in controls:
    #         p1.slam()
    #     if "a" in controls:
    #         p1.left()
    #     if "d" in controls:
    #         p1.right()
    #
    #     # Physics calculations
    #     p1.calculate() # Needed to actual update the position of the hitbox
    #     platform.calculate()
    #
    #     # Rendering
    #     p1.setPos(plyJumpRender, plyJump.position[0], plyJump.position[1]) # This parents the object to the hitbox
    #     setPos(worldRenderer, platform.position[0], platform.position[1])
    #
    #     sleep(0.0083) # Magic sleep number from jamie