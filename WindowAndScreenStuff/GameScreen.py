from Stage import Stage
from updatedGraphics import *

class GameScreen:
    def __init__(self, window):
        stage = Stage(window)
        #Stage.createStage()
        Stage.regStage(stage, window)
        self.createHealthBars(window)
        self.startGame(window)
        self.countDown = Text(Point(window.getWidth() / 2, window.getHeight() / 2), Text)
        self.countdown(window)
        while True:
            pass

    def createHealthBars(self, window):
        pass

    def startGame(self, window):
        pass

    def countdown(self, window):

        self.countDown.setTextColor("White")
        self.countDown.setSize(20)
        self.countDown.draw(window)
        self.countDown.setSize(36)
        for i in range(3, 0, -1):
            self.countDown.setText(str(i))
            time.sleep(1)
        self.countDown.setText("Fight")
        self.countDown.setSize(36)
        time.sleep(1)
        self.countDown.setText("")