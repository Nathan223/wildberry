from updatedGraphics import *
class Stage(object):
    def __init__(self,win:GraphWin):
        self.background = Rectangle(Point(0,0), Point(1200,800))
        self.background.setFill("Black")
        self.background.draw(win)
        for i in range(3,0,-1):
            self.background
    def regStage(self,win:GraphWin):
        self.stage = Rectangle(Point(200,500),Point(1000,700))
        self.stage.setFill("Blue")
        self.stage.draw(win)
