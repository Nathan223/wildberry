from updatedGraphics import *
from time import sleep

gravity = -1
hitboxes = []
mvtSpeed = 3

class hitbox:
    def __init__(self, width, height, static):
        global hitboxes
        self.yVel = 0 # Y
        self.xVel = 0 # X
        self.xPos = 0 # X
        self.yPos = 0 # Y

        self.static = static

        self.width = width
        self.height = height
        self.hitbox = [self.xPos - self.width / 2, self.xPos + self.width / 2,
                        self.yPos + self.height, self.yPos - self.height]

        hitboxes.append(self.hitbox)
        self.hitboxID = len(hitboxes) - 1

    def calculate(self):
        global gravity
        global objResistance
        global hitboxes

        # Update the hitbox
        self.hitbox = [self.xPos - self.width / 2, self.xPos + self.width / 2,
                        self.yPos + self.height, self.yPos - self.height]
        hitboxes[self.hitboxID] = self.hitbox

        collidedLeft = False
        collidedRight = False
        collidedUp = False
        collidedDown = False

        #projectedVelocity = (gravity * self.weight) * (self.velocity[1] + 1) * -1
        if self.static == 0:
            self.yVel = 0

        i = 0
        for box in hitboxes:
            # Make sure it doesnt collide with its own hitbox
            if i != self.hitboxID:
                # X calculations
                if self.xPos + self.width > box[0]:
                    collidedLeft = True
                if self.xPos + self.width < box[1]:
                    collidedRight = True
                # Y calculations
                if self.yPos + self.height < box[2]:
                    collidedUp = True
                if self.yPos + self.height > box[3]:
                    collidedDown = True

            i += 1

        # Only move if possible
        if (collidedLeft == False or collidedRight == False) or (collidedUp == False or collidedDown == False):
            self.xPos -= self.yVel
            self.yVel += self.yVel

        #print("Object ID", self.hitboxID, ": ", self.velocity)

        # Move back if you can
        # X
        if self.xVel > 0 and collidedLeft == True:
            self.xPos -= self.xVel
        if self.xVel < 0 and collidedRight == True:
            self.xPos -= self.xVel
        """
        # Y
        if self.velocity[1] > 0 and collidedDown == True:
            self.position[1] -= ((gravity * self.weight) + self.velocity[1])
        if self.velocity[1] < 0 and collidedUp == True:
            self.position[1] -= ((gravity * self.weight) + self.velocity[1])
        """
        if self.yVel > 0 and collidedDown == True:
            self.yVel -= 0#(gravity * self.weight) * (yVel + 1)
        if self.yVel < 0 and collidedUp == True:
            self.yVel -= 0#(gravity * self.weight) * (yVel + 1)

        if self.yVel < hitboxes[1][3]:
            self.yPos -= self.yVel
        else:
            self.yPos = hitboxes[1][3] - self.height
            self.yVel = 0

        self.move()

    def move(self):
        self.xPos -= self.xVel
        self.yPos -= self.yVel
    # def setForce(self, dir): # The first index is the left right force and the second index is up down force
    #     xVel = dir[0]
    #     yVel = dir[1]
    #
    # def addForce(self, dir):
    #     xVel += dir[0]
    #     yVel += dir[1]

    def getHitbox(self):
        return self.hitbox

# this function should be kept, it sets the position
# instead of moving it
def setPos(obj, x, y):
    currentX = obj.getCenter().getX()
    currentY = obj.getCenter().getY()
    obj.move(x - currentX, y - currentY)


#""" Example documentation
def main():
    window = GraphWin("Jump test", 640, 480)
    window.setBackground("white")

    plyJump = hitbox(25, 25, 1)
    platform = hitbox(500, 1.5, 0)

    plyJumpRender = Rectangle(Point(0, 0), Point(50, 50))
    plyJumpRender.setFill("black")
    plyJumpRender.draw(window)

    worldRenderer = Rectangle(Point(0, 0), Point(500, 3))
    worldRenderer.setFill("red")
    worldRenderer.draw(window)

    platform.xPos = 640/2
    platform.yPos = 480/2

    plyJump.xPos = 220
    plyJump.yPos = 5
    #plyJump.setForce([2, 0])

    while True:
        # Controls
        controls = window.checkKey()
        if controls == "w" and plyJump.yVel == 0:
            plyJump.yVel = mvtSpeed
        if controls == "a":
            plyJump.xVel = -1 * mvtSpeed
        if controls == "d":
            plyJump.xVel = mvtSpeed

        # Physics calculations
        plyJump.calculate()
        platform.calculate()

        plyJump.yVel += gravity

        print(plyJump.yPos)

        # Rendering
        setPos(plyJumpRender, plyJump.xPos, plyJump.yPos)
        setPos(worldRenderer, platform.xPos, platform.yPos)

        #sleep(0.0083)
        sleep(0.4)

main()
#"""
