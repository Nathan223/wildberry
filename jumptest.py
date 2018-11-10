from updatedGraphics import *

gravity = -10

class block:
    def __init__(self, inertia, weight, radius):
        self.inertia = inertia
        self.weight = weight
        self.velocity = 0
        self.position = [0, 0]

    def calculate(self):
        global gravity
        self.position[1] -= gravity

def setPos(obj, x, y):
    currentX = obj.getCenter().getX()
    currentY = obj.getCenter().getY()
    obj.move(x - currentX, y - currentY)

def main():
    window = GraphWin("Jump test", 640, 480)
    window.setBackground("white")

    plyJump = block(1, 10)

    plyJumpRender = Rectangle(Point(0, 0), Point(50, 50))
    plyJumpRender.setFill("black")
    plyJumpRender.draw(window)

    while True:
        #plyJump.calculate()
        setPos(plyJumpRender, plyJump.position[0], plyJump.position[1])

main()
