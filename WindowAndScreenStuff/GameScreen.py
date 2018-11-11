from Stage import Stage


class GameScreen:
    def __init__(self,window):
        stage = Stage(window)
        #Stage.createStage()
        Stage.regStage()
        self.createHealthBars(window)
        self.startGame(window)

    def createHealthBars(self,window):
        pass