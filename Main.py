from WindowAndScreenStuff.Window import Window
from WindowAndScreenStuff.StartScreen import StartScreen

GAME_TITLE = "Wildberry"
WIDTH = 1200
HEIGHT = 800



class Game:
    def __init__(self):
        self._wildberryWindow = Window(GAME_TITLE,WIDTH,HEIGHT)

    def run(self):
        startScreen = StartScreen(self.getGameWindow())
        self.getGameWindow().getKey()


    def getGameWindow(self):
        return self._wildberryWindow.getWindow()

if __name__ == "__main__":
    game = Game()
    game.run()
