from updatedGraphics import *
class Stage(object):
    def __init__(self,window):
        def __init__(self, window):
            self.pos1 = Point(0, 0)
            self.pos2 = Point(0, 0)

    def regStage(self,window):
        background = Image(Point(600,400),"ImagesAndSprites/StartScreen.gif")
        background.draw(window)
        stage = Rectangle(Point(200,650),Point(1000,700))
        stage.setFill("Blue")
        stage.draw(window)
        self.pos1 = Point