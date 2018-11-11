from Stages import getStages
from random import randint


class GameScreen:
    def __init__(self,window):
        #ran = randint(0,getStages().length)
        getStages(window)
        self.createHealthBars(window)

    def createHealthBars(self,window):
        pass


