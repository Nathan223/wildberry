from Stage import Stage
from graphics import Text,Image,Point
import time

class GameScreen:
    def __init__(self, window, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.stage = Stage(window)
        #Stage.createStage()
        Stage.regStage(self.stage, window)
        self.createHealthBars(window)
        self.startGame(window)
        self.countDown = Text(Point(window.getWidth() / 2, window.getHeight() / 2), Text)
        self.countdown(window)


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
        p1Pic = Image(p1Point,self.p1.getImage())
        p1Pic.draw(window)

    def loadP2(self, window):
        p1Point = Point(self.stage.getPos2().getX(), self.stage.getPos2().getY() - (89 + 6))
        p1Pic = Image(p1Point, self.p2.getImage())
        p1Pic.draw(window)

