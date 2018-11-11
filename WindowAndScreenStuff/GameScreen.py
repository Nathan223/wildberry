from Stage import Stage
from updatedGraphics import *

class GameScreen:
    def __init__(self,window):
        stage = Stage(window)
        #Stage.createStage()
        Stage.regStage(stage,window)
        self.createHealthBars(window)
        self.startGame(window)
        self.countDown(window)
        while(True):
            pass

    def createHealthBars(self,window):
        pass

    def startGame(self,window):
        pass

    def countDown(self,window):
        pass