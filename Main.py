from WindowAndScreenStuff.Window import Window
from WindowAndScreenStuff.StartScreen import StartScreen
from WindowAndScreenStuff.GameScreen import GameScreen
from Characters.Apple import Apple
import threading
from Characters import Player

GAME_TITLE = "Wildberry"
WIDTH = 1200
HEIGHT = 800

class Game:
    def __init__(self):
        self._wildberryWindow = Window(GAME_TITLE,WIDTH,HEIGHT)

    def getGameWindow(self):
        return self._wildberryWindow.getWindow()

    def run(self):
        StartScreen(self.getGameWindow())
        GameScreen(self.getGameWindow(),Player(Apple(), "p1"),Player(Apple(), "p2"))

class MusicPlayer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        exec(open("Music.py").read())


if __name__ == "__main__":
    m = MusicPlayer()
    m.start()
    game = Game()
    game.run()
