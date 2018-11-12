from WindowAndScreenStuff.Window import Window
from WindowAndScreenStuff.StartScreen import StartScreen
from WindowAndScreenStuff.GameScreen import GameScreen
from Characters.Apple import Apple
import threading

GAME_TITLE = "wildberry"
WIDTH = 1200
HEIGHT = 800

class Game:
    def __init__(self):
        self._wildberryWindow = Window(GAME_TITLE,WIDTH,HEIGHT)

    def getGameWindow(self):
        return self._wildberryWindow.getWindow()

    def run(self):
        StartScreen(self.getGameWindow())
        p1 = "Apple"
        p2 = "Apple"
        GameScreen(self.getGameWindow(),p1,p2)
        self.getGameWindow().close()

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
