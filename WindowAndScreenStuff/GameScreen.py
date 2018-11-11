from Stage import Stage


class GameScreen:
    def __init__(self,window):
        stage = Stage(window)
        #Stage.createStage()
        Stage.regStage(stage,window)
        self.createHealthBars(window)
        self.startGame(window)
        while(True):
            pass

    def createHealthBars(self,window):
        pass

    def startGame(self,window):
        pass