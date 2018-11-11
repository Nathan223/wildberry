# Importing
from graphics import *
from time import sleep

# Global constants
gravity = -2 # Amount of acceleration for gravity
objResistance = 1 # How much resistance on an object, needed to stop infinite acceleration

# Global variables
hitboxes = [] # Contains all the seperate hitboxes for each hitbox

# Hitbox class
class hitbox:
    def __init__(self, width, height, weight):
        global hitboxes # Makes the hitboxes global variable accessable
        self.velocity = [0, 0] # X, Y, This is how much to move left and right, can be manipulated using methods
        self.position = [0, 0] # X, Y, The position of the object, you set the image to this
        self.width = width # This is the width of the hitbox
        self.height = height # This is the height of the hitbox
        self.weight = weight # This is the weight of the hitbox, if its 1 its affected normally, 0 no gravity, 2 double physics
        self.hitbox = [self.position[0] - self.width / 2, self.position[0] + self.width / 2,
                        self.position[1] + self.height, self.position[1] - self.height] # Defines the hitbox as in Left, Right, Up, Down

        hitboxes.append(self.hitbox) # Add the hitbox to the global hitboxes
        self.hitboxID = len(hitboxes) - 1 # Set the hitbox ID to the last hitbox added

        self.inAir = False # If the player is in the air or not
        self.timeInAir = 0 # How long the player has been in the air

    def calculate(self):
        global gravity # Gets the gravity from the global constant
        global objResistance # Gets the object resistance
        global hitboxes # Gets the total amount of hitboxes

        # Update the hitbox
        self.hitbox = [self.position[0] - self.width / 2, self.position[0] + self.width / 2,
                        self.position[1] + self.height, self.position[1] - self.height] # Updates the hitbox assigned in the initializer
        hitboxes[self.hitboxID] = self.hitbox # Puts the hitbox into global hitboxes

        collidedLeft = False # If the hitbox was collided at the left
        collidedRight = False # If the hitbox was collided at the right
        collidedUp = False # If the hitbox was collided at the top
        collidedDown = False # If the hitbox was collided at the bottom

        projected = self.position[1] - ((gravity * self.weight) + self.velocity[1]) # Where the hitbox should be

        i = 0
        # Loop through each of the hitboxes available
        for box in hitboxes:
            # Make sure it doesnt collide with its own hitbox
            if i != self.hitboxID:
                # X calculations
                if self.position[0] + self.width > box[0]:
                    collidedLeft = True
                if self.position[0] + self.width < box[1]:
                    collidedRight = True
                # Y calculations
                if projected - self.height < box[2]:
                    collidedUp = True
                if projected + self.height > box[3]:
                    collidedDown = True

            i += 1

        # Check if the hitbox is in the air
        if collidedDown == True and collidedLeft == True and collidedRight == True and collidedUp == True:
            self.inAir = False
        else:
            self.inAir = True

        # Falling constant
        if self.inAir == True:
            self.timeInAir += 0.1
        else:
            self.timeInAir = 0

        if self.weight != 0:
            fallingVel = ((gravity * self.weight) + self.velocity[1]) * self.timeInAir # Formula that i barly know how it works (dont touch it)
        else:
            fallingVel = 0 # Set to zero if its weightless (dont move it)

        # Only move if possible
        if (collidedLeft == False or collidedRight == False) or (collidedUp == False or collidedDown == False):
            self.position[0] -= self.velocity[0] # Move the objects actual position
            self.position[1] -= fallingVel # Make it fall based on the falling velocity
        else:
            self.velocity[1] = 0

        # Lets the player move back if its still collided
        # X
        if self.velocity[0] > 0 and collidedLeft == True:
            self.position[0] -= self.velocity[0]
        if self.velocity[0] < 0 and collidedRight == True:
            self.position[0] -= self.velocity[0]
        # Y
        if self.velocity[1] > 0 and collidedDown == True:
            self.position[1] -= fallingVel
        if self.velocity[1] < 0 and collidedUp == True:
            self.position[1] -= fallingVel

        # Slow down the velocity at every physics calculation
        if self.velocity[0] > 0:
            self.velocity[0] -= objResistance
        else:
            self.velocity[0] = 0

        if self.velocity[0] < 0:
            self.velocity[0] += objResistance
        else:
            self.velocity[0] = 0

        if self.velocity[1] > 0:
            self.velocity[1] -= objResistance
        else:
            self.velocity[1] = 0

    def setForce(self, dir): # The first index is the left right force and the second index is up down force
        self.velocity[0] = dir[0]
        self.velocity[1] = dir[1]

    def addForce(self, dir): # Same as set, but additive
        self.velocity[0] += dir[0]
        self.velocity[1] += dir[1]

    def addXForce(self, x): # Adds force only on the X
        self.velocity[0] += x

    def addYForce(self, y): # Adds for only on the Y
        self.velocity[1] += y

    def getHitbox(self): # Returns the hitbox
        return self.hitbox

<<<<<<< HEAD:hitbox.py

=======
# this function should be kept, it sets the position
# instead of moving it
def setPos(obj, x, y):
    currentX = obj.getCenter().getX()
    currentY = obj.getCenter().getY()
    obj.move(x - currentX, y - currentY)



def main():
    window = GraphWin("Jump test", 640, 480)
    window.setBackground("white")

    # Hitbox defines as hitbox(XRANGE, YRANGE, WEIGHT)
    plyJump = hitbox(25, 25, 1)
    platform = hitbox(500, 1.5, 0)

    # This is just the objects
    plyJumpRender = Rectangle(Point(0, 0), Point(50, 50))
    plyJumpRender.setFill("black")
    plyJumpRender.draw(window)

    worldRenderer = Rectangle(Point(0, 0), Point(500, 3))
    worldRenderer.setFill("red")
    worldRenderer.draw(window)

    # Set the beginning position as [XPOS, YPOS]
    platform.position = [640/2, 480/2]
    plyJump.position = [220, 5]

    while True:
        # Controls
        controls = window.checkKeys()
        if "w" in controls and plyJump.inAir == False:
            plyJump.addYForce(20)
        if "s" in controls:
            plyJump.addYForce(-15)
        if "a" in controls:
            plyJump.addXForce(5)
        if "d" in controls:
            plyJump.addXForce(-5)

        # Physics calculations
        plyJump.calculate() # Needed to actual update the position of the hitbox
        platform.calculate()

        # Rendering
        setPos(plyJumpRender, plyJump.position[0], plyJump.position[1]) # This parents the object to the hitbox
        setPos(worldRenderer, platform.position[0], platform.position[1])

        sleep(0.0083) # Magic sleep number from jamie

#main()
>>>>>>> 13ed99ed920ab3da6a413ea8e05d33eba7388674:physics2.py

