from Stage import Stage
from graphics import Text,Image,Point
from Characters.Player import *
from physics2 import hitbox
import time



class GameScreen:
    def __init__(self, window, player1, player2):
        self.stage = Stage(window)
        self.stage.regStage(window)
        self.players [player1,player2 ]
        #self.p1Point = Point(self.stage.getPos1().getX(), self.stage.getPos1().getY() - (89 + 6))
        #self.p2Point = Point(self.stage.getPos2().getX(), self.stage.getPos2().getY() - (89 + 6))
        self.p1Text = Text(Point(50,50), str(self.players[0].currentHP))
        self.p2Text = Text(Point(1100, 50), str(self.players[1].currentHP))
        self.stage.regStageCreateHB()
        #Stage.createStage()
        self.createHealthBars(window)
        self.startGame(window)
        self.countDown = Text(Point(window.getWidth() / 2, window.getHeight() / 2), '')
        self.countdown(window)
        while True:
            if self.checkExit(window.checkKey()):
                window.close()
            self.update()

    def checkExit(self, key):
        if key == 'Escape':
            return True
        return False

    def checkLose(self):
        pass

    def update(self):
        self.p1Text.setText(str(self.players[0].currentHP))
        self.p2Text.setText(str(self.players[1].currentHP))

    def createHealthBars(self, window):
        self.p1Text.setTextColor("White")
        self.p2Text.setTextColor("White")
        self.p1Text.setSize(36)
        self.p2Text.setSize(36)
        self.p1Text.draw(window)
        self.p2Text.draw(window)

    def startGame(self, window):
        pass

    def countdown(self, window):

        self.countDown.setTextColor("White")
        self.countDown.setSize(20)
        self.countDown.setText("3")
        self.countDown.draw(window)
        self.countDown.setSize(36)
        for i in range(3, 0, -1):
            self.countDown.setText(str(i))
            if i==2:
                self.players[0].fruit.imageFile.draw(window)

            if i==1:
                self.players[1].fruit.imageFile.draw(window)
            time.sleep(1)
        self.countDown.setText("Fight!")
        self.countDown.setSize(36)
        time.sleep(1)
        self.countDown.setText("")

    def loadP1(self, window):
        self.p1Pic.draw(window)

    def loadP2(self, window):
        self.p2Pic.draw(window)
