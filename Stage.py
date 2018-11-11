from updatedGraphics import *
class Stage(object):
    def __init__(self,window):
        self.pos = 1

    def regStage(self,window):
        background = Image(Point(600,400),"ImagesAndSprites/StartScreen.gif")
        background.draw(window)
        stage = Rectangle(Point(200,650),Point(1000,700))
        stage.setFill("Blue")
        stage.draw(window)
