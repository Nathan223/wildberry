from Stage import Stage
from graphics import Text,Image,Point
from Characters.Player import *
from physics2 import hitbox
import time



class GameScreen:
    def __init__(self, window, player1, player2):
        self.stage = Stage(window)
        Stage.regStage(self.stage, window)
        self.p1 = Player(player1, None)
        self.p2 = Player(player2, None)
        self.p1Point = Point(self.stage.getPos1().getX(), self.stage.getPos1().getY() - (89 + 6))
        self.p2Point = Point(self.stage.getPos2().getX(), self.stage.getPos2().getY() - (89 + 6))
        self.p1Pic = Image(self.p1Point,player1.getFruit.getImageFile())
        self.p2Pic = Image(self.p2Point,player2.getFruit.getImageFile())
        self.p1.setImage(self.p1Pic)
        self.p2.setImage(self.p2Pic)
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
        pass

    def createHealthBars(self, window):
        pass

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
                self.p1Pic.draw(window)
            if i==1:
                self.p2Pic.draw(window)
            time.sleep(1)
        self.countDown.setText("Fight")
        self.countDown.setSize(36)
        time.sleep(1)
        self.countDown.setText("")

    def loadP1(self, window):
        self.p1Pic.draw(window)

    def loadP2(self, window):
        self.p2Pic.draw(window)
