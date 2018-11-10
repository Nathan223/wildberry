from Window import Window


GAME_TITLE = "Wildberry"
WIDTH = 900
HEIGHT = 1440

class Game:
    def __init__(self):
        self._wildberryWindow = Window(GAME_TITLE,WIDTH,HEIGHT)

    def run(self):
        self._wildberryWindow.getWindow().getMouse()

if __name__ == "__main__":
    game = Game()
    game.run()