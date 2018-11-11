from Stage import Stage
from graphics import Text,Image,Point
from physics2 import hitbox
import time

class GameScreen:
    def __init__(self, window, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.hb1 = None
        self.hb2 = None
        self.p1Pic = None
        self.p2Pic = None
        self.stage = Stage(window)
        #Stage.createStage()
        Stage.regStage(self.stage, window)
        self.createHealthBars(window)
        self.startGame(window)
        self.countDown = Text(Point(window.getWidth() / 2, window.getHeight() / 2), Text)
        self.countdown(window)
        while True:
            if self.checkExit(window.checkKey()):
                window.close()

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
                self.loadP1(window)
            if i==1:
                self.loadP2(window)
            time.sleep(1)
        self.countDown.setText("Fight")
        self.countDown.setSize(36)
        time.sleep(1)
        self.countDown.setText("")

    def loadP1(self, window):
        p1Point = Point(self.stage.getPos1().getX(),self.stage.getPos1().getY()-(89+6))
        self.p1Pic = Image(p1Point,self.p1.getImage())
        self.hb1 = hitbox()
        self.p1Pic.draw(window)

    def loadP2(self, window):
        p2Point = Point(self.stage.getPos2().getX(), self.stage.getPos2().getY() - (89 + 6))
        self.p2Pic = Image(p2Point, self.p2.getImage())
        self.hb2 = hitbox()
        self.p2Pic.draw(window)
