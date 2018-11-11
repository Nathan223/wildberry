from ImageGetter import getImage
from Window import Window
from updatedGraphics import Image, Point

GAME_TITLE = "Wildberry"
WIDTH = 1200
HEIGHT = 800



class Game:
    def __init__(self):
        self._wildberryWindow = Window(GAME_TITLE,WIDTH,HEIGHT)

    def run(self):
        gradiant = Image(Point(600,400),getImage("Gradiant.gif"))
        gradiant.draw(self.getGameWindow())
        self.getGameWindow().getKey()

    def getGameWindow(self):
        return self._wildberryWindow.getWindow()

if __name__ == "__main__":
    game = Game()
    game.run()
