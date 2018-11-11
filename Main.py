from ImageGetter import getImage
from Window import Window
from updatedGraphics import Image, Point, Text, color_rgb

GAME_TITLE = "Wildberry"
WIDTH = 1200
HEIGHT = 800



class Game:
    def __init__(self):
        self._wildberryWindow = Window(GAME_TITLE,WIDTH,HEIGHT)

    def run(self):
        image = Image(Point(600,400),getImage("StartScreen.gif"))
        startText = Text(Point(600,600),"Press Any Key To Start")
        startText.setFace("arial")
        startText.setSize(36)
        startText.setStyle("normal")
        startText.setTextColor(color_rgb(255,255,255))
        image.draw(self.getGameWindow())
        startText.draw(self.getGameWindow())
        self.getGameWindow().getKey()


    def getGameWindow(self):
        return self._wildberryWindow.getWindow()

if __name__ == "__main__":
    game = Game()
    game.run()
