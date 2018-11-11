gravity = -1
objResistance = 1

class hitbox:
    def __init__(self, width, height):
        self.velocity = [0, 0] # X, Y
        self.position = [0, 0] # X, Y
        self.hitbox = [self.position[0] - self.width / 2, self.position[0] + self.width / 2,
                        self.position[1] + self.height, self.position[1] - self.height]

    def calculate(self, allBoundingBoxes):
        global gravity
        global objResistance

        collidedLeft = False
        collidedRight = False
        collidedUp = False
        collidedDown = False
        for box in allBoundingBoxes:
            # X calculations
            if self.position[0] + self.width > box[0]:
                collidedLeft = True
            if self.position[0] + self.width < box[1]:
                collidedRight = True
            # Y calculations
            if self.position[1] + self.height < box[2]:
                collidedUp = True
            if self.position[1] + self.height > box[3]:
                collidedDown = True

        # Only move if possible
        if (collidedLeft == False or collidedRight == False) or (collidedUp == False or collidedDown == False):
            self.position[0] -= self.velocity[0]
            self.position[1] -= (gravity + self.velocity[1])

        # Move back if you can
        # X
        if self.velocity[0] > 0 and collidedLeft == True:
            self.position[0] -= self.velocity[0]
        if self.velocity[0] < 0 and collidedRight == True:
            self.position[0] -= self.velocity[0]
        # Y
        if self.velocity[1] > 0 and collidedDown == True:
            self.position[1] -= (gravity + self.velocity[1])
        if self.velocity[1] < 0 and collidedUp == True:
            self.position[1] -= (gravity + self.velocity[1])

        # Slow down the velocity at every physics calculation
        if self.velocity[0] > 0:
            self.velocity[0] -= objResistance
        else:
            self.velocity[0] = 0

        if self.velocity[1] > 0:
            self.velocity[1] -= objResistance
        else:
            self.velocity[1] = 0

        # Update the hitbox
        self.hitbox = [self.position[0] - self.width / 2, self.position[0] + self.width / 2,
                        self.position[1] + self.height, self.position[1] - self.height]

    def setForce(self, dir): # The first index is the left right force and the second index is up down force
        self.velocity[0] = dir[0]
        self.velocity[1] = dir[1]

    def getHitbox(self):
        return self.hitbox

# this function should be kept, it sets the position
# instead of moving it 
def setPos(obj, x, y):
    currentX = obj.getCenter().getX()
    currentY = obj.getCenter().getY()
    obj.move(x - currentX, y - currentY)


""" Example documentation
def main():
    window = GraphWin("Jump test", 640, 480)
    window.setBackground("white")

    plyJump = hitbox(25, 25)
    platform = world(250, 1.5)

    plyJumpRender = Rectangle(Point(0, 0), Point(50, 50))
    plyJumpRender.setFill("black")
    plyJumpRender.draw(window)

    worldRenderer = Rectangle(Point(0, 0), Point(500, 3))
    worldRenderer.setFill("red")
    worldRenderer.draw(window)
    setPos(worldRenderer, 640/2, 480/2)

    plyJump.position = [220, 5]
    plyJump.setForce([2, 0])

    while True:
        # Controls
        controls = window.checkKey()
        if controls == "w":
            plyJump.setForce([0, 15])
        if controls == "a":
            plyJump.setForce([5, 0])
        if controls == "d":
            plyJump.setForce([-5, 0])

        # Physics calculations
        plyJump.calculate(allBoundingBoxes)

        # Rendering
        setPos(plyJumpRender, plyJump.position[0], plyJump.position[1])

        sleep(0.0083)

main()
"""
