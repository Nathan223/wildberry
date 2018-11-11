# Importing
from graphics import *
from time import sleep

# Global constants
gravity = -2 # Amount of acceleration for gravity
objResistance = 1 # How much resistance on an object, needed to stop infinite acceleration

# Global variables
hitboxes = [] # Contains all the seperate hitboxes for each hitbox

# this function should be kept, it sets the position
# instead of moving it
def setPos(obj, x, y):
    currentX = obj.getAnchor().getX()
    currentY = obj.getAnchor().getY()
    obj.move(x - currentX, y - currentY)

# Hitbox class
class hitbox: # Obj, width, height, weight, pos, ignored
    def __init__(self, obj, weight):
        global hitboxes # Makes the hitboxes global variable accessable
        self.velocity = [0, 0] # X, Y, This is how much to move left and right, can be manipulated using methods
        self.position = [obj.getAnchor().getX(), obj.getAnchor().getY()] # X, Y, The position of the object, you set the image to this
        self.width = obj.getWidth()/1.1 # This is the width of the hitbox
        self.height = obj.getHeight()/2 # This is the height of the hitbox
        self.weight = weight # This is the weight of the hitbox, if its 1 its affected normally, 0 no gravity, 2 double physics
        self.hitbox = [self.position[0] - self.width / 2, self.position[0] + self.width / 2,
                        self.position[1] + self.height, self.position[1] - self.height] # Defines the hitbox as in Left, Right, Up, Down

        self.obj = obj

        hitboxes.append(self.hitbox) # Add the hitbox to the global hitboxes
        self.hitboxID = len(hitboxes) - 1 # Set the hitbox ID to the last hitbox added

        self.inAir = False # If the player is in the air or not
        self.timeInAir = 0 # How long the player has been in the air

        self.collidedLeft = False
        self.collidedRight = False
        self.collidedUp = False
        self.collidedDown = False
        self.playerCollidedLeft = False
        self.playerCollidedRight = False

        self.projectedX = 0
        self.projectedY = 0

    def calculate(self):
        global gravity # Gets the gravity from the global constant
        global objResistance # Gets the object resistance
        global hitboxes # Gets the total amount of hitboxes

        # Update the hitbox
        self.hitbox = [self.position[0] - self.width / 2, self.position[0] + self.width / 2,
                        self.position[1] + self.height, self.position[1] - self.height] # Updates the hitbox assigned in the initializer
        hitboxes[self.hitboxID] = self.hitbox # Puts the hitbox into global hitboxes

        self.collidedLeft = False # If the hitbox was collided at the left
        self.collidedRight = False # If the hitbox was collided at the right
        self.collidedUp = False # If the hitbox was collided at the top
        self.collidedDown = False # If the hitbox was collided at the bottom
        self.playerCollidedLeft = False
        self.playerCollidedRight = False

        self.projectedX = self.position[0] + self.velocity[0] # Where the hitbox should be
        self.projectedY = self.position[1] - ((gravity * self.weight) + self.velocity[1]) # Where the hitbox should be

        self.fallingVel = 0

        i = 0
        # Loop through each of the hitboxes available
        for box in hitboxes:
            # Make sure it doesnt collide with its own hitbox
            if i == 2:
                # X calculations
                if self.projectedX + self.width > box[0]:
                    self.collidedLeft = True
                if self.projectedX - self.width < box[1]:
                    self.collidedRight = True
                # Y calculations
                if self.projectedY - self.height < box[2]:
                    self.collidedUp = True
                if self.projectedY + self.height > box[3]:
                    self.collidedDown = True
            if i == 1 and self.hitboxID == 0:
                # X calculations
                if self.projectedX + self.width > box[0]:
                    self.playerCollidedLeft = True
                if self.projectedX - self.width < box[1]:
                    self.playerCollidedRight = True
            if i == 0 and self.hitboxID == 1:
                # X calculations
                if self.projectedX + self.width > box[0]:
                    self.playerCollidedLeft = True
                if self.projectedX - self.width < box[1]:
                    self.playerCollidedRight = True

            i += 1

        # Check if the hitbox is in the air
        if self.collidedDown == True and self.collidedLeft == True and self.collidedRight == True and self.collidedUp == True:
            self.inAir = False
        else:
            self.inAir = True

        # Falling constant
        if self.inAir == True:
            self.timeInAir += 0.1
        else:
            self.timeInAir = 0

        if self.weight != 0:
            self.fallingVel = ((gravity * self.weight) + self.velocity[1]) * self.timeInAir # Formula that i barly know how it works (dont touch it)
        else:
            self.fallingVel = 0 # Set to zero if its weightless (dont move it)

        # Only move if possible
        if self.playerCollidedLeft == False or self.playerCollidedRight == False:
            self.position[0] -= self.velocity[0] # Move the objects actual position
        else:
            self.velocity[0] = 0

        if (self.collidedLeft == False or self.collidedRight == False) or (self.collidedUp == False or self.collidedDown == False):
            self.position[1] -= self.fallingVel # Make it fall based on the falling velocity
        else:
            self.velocity[1] = 0

        # Lets the player move back if its still collided
        # X
        if self.velocity[0] > 0 and self.playerCollidedLeft == True:
            self.position[0] -= self.velocity[0]
        if self.velocity[0] < 0 and self.playerCollidedRight == True:
            self.position[0] -= self.velocity[0]
        # Y
        if self.velocity[1] > 0 and self.collidedDown == True:
            self.position[1] -= self.fallingVel
        if self.velocity[1] < 0 and self.collidedUp == True:
            self.position[1] -= self.fallingVel

        # Slow down the velocity at every physics calculation
        print(self.velocity)
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

        setPos(self.obj, self.position[0], self.position[1])

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

# Example documentation
# def main():
#     window = GraphWin("Jump test", 640, 480)
#     window.setBackground("white")
#
#     # This is just the objects
#     plyJumpRender = Image(Point(50, 50), "Cherry.png")
#     plyJumpRender.draw(window)
#
#     plyJumpRender2 = Image(Point(50, 50), "Cherry.png")
#     plyJumpRender2.draw(window)
#     plyJumpRender2.move(150, 0)
#
#     worldRenderer = Image(Point(500, 3), "platform.png")
#     worldRenderer.draw(window)
#     worldRenderer.move(-200, 400)
#
#     # Hitbox defines as
#     # Obj, width, height, weight, pos, ignored
#     plyJump = hitbox(plyJumpRender, 1)
#     plyJump2 = hitbox(plyJumpRender2, 1)
#     platform = hitbox(worldRenderer, 0)
#
#     while True:
#         # Controls
#         controls = window.checkKeys()
#         if "w" in controls and plyJump.inAir == False:
#             plyJump.addYForce(20)
#         if "a" in controls:
#             plyJump.addXForce(5)
#         if "d" in controls:
#             plyJump.addXForce(-5)
#         if "Up" in controls and plyJump2.inAir == False:
#             plyJump2.addYForce(20)
#         if "Left" in controls:
#             plyJump2.addXForce(5)
#         if "Right" in controls:
#             plyJump2.addXForce(-5)
#
#         # Physics calculations
#         plyJump.calculate() # Needed to actual update the position of the hitbox
#         plyJump2.calculate()
#         platform.calculate()
#
#         sleep(0.0083) # Magic sleep number from jamie
#
# main()
