from Stage import Stage
from graphics import Text,Image,Point
from Characters.Player import *
from physics2 import hitbox
from WindowAndScreenStuff.p1wins import p1wins
from WindowAndScreenStuff.p2wins import p2wins
import time


class GameScreen:
    def __init__(self, window, player1, player2):
        self.window = window
        self.p1 = Player(player1, None)
        self.p2 = Player(player2, None)
        background = Image(Point(600, 400), "ImagesAndSprites/StartScreen.gif")
        background.draw(window)
        self.createHealthBars(window)
        self.startGame(window)
        self.countDown = Text(Point(window.getWidth() / 2, window.getHeight() / 2), '')
        self.countdown(window)
        self.plyJumpRender = Image(Point(300, 50), "ImagesAndSprites/Apple.gif")
        self.plyJumpRender.draw(window)

        self.plyJumpRender2 = Image(Point(900, 50), "ImagesAndSprites/Apple.gif")
        self.plyJumpRender2.draw(window)
        # plyJumpRender2.move(150, 0)

        self.worldRenderer = Image(Point(800, 3), "ImagesAndSprites/blue.gif")
        self.worldRenderer.draw(window)
        self.worldRenderer.move(-200, 400)

        # Hitbox defines as
        # Obj, width, height, weight, pos, ignored
        self.plyJump = hitbox(self.plyJumpRender, 1)
        self.plyJump2 = hitbox(self.plyJumpRender2, 1)
        self.platform = hitbox(self.worldRenderer, 0)
        self.time1 = 0
        self.time2 = 0
        while True:
            self.update(window)
            if(self.getWinner()==1):
                p1wins(window)
                time.sleep(2)
                break
            if(self.getWinner()==2):
                p2wins(window)
                time.sleep(2)
                break


    def checkExit(self, key):
        if key == 'Escape':
            return True
        return False

    def getWinner(self):
        if(self.p1.health<=0 or self.plyJump.position[1] > 800 or self.plyJump.position[0]<0 or self.plyJump.position[0]>1200):
            return 2
        if(self.p2.health<=0 or self.plyJump2.position[1] > 800 or self.plyJump2.position[0]<0 or self.plyJump2.position[0]>1200):
            return 1
        else:
            return 0

    def checkLose(self):
        pass

    def update(self,window):
        self.p1Text.setText(str(self.p1.health))
        self.p2Text.setText(str(self.p2.health))
        controls = window.checkKeys()
        if "Escape" in controls:
            self.window.close()
        if "w" in controls and self.plyJump.inAir == False:
            self.plyJump.addYForce(20)
        if "a" in controls:
            self.plyJump.addXForce(5)
        if "d" in controls:
            self.plyJump.addXForce(-5)
        if "e" in controls and abs(self.plyJump.position[0] - self.plyJump2.position[0]) < 120 and abs(
                self.plyJump.position[1] - self.plyJump2.position[1]) < 120 and time.time() - self.time1 > 1:
            self.p2.health -= 5
            self.p2Text.setText(str(self.p2.health))
            self.time1 = time.time()
        if "Up" in controls and self.plyJump2.inAir == False:
            self.plyJump2.addYForce(20)
        if "Left" in controls:
            self.plyJump2.addXForce(5)
        if "Right" in controls:
            self.plyJump2.addXForce(-5)
        if "Insert" in controls and abs(self.plyJump.position[0] - self.plyJump2.position[0]) < 120 and abs(
                self.plyJump.position[1] - self.plyJump2.position[1]) < 120 and time.time() - self.time2 > 1:
            self.p1.health -= 5
            self.p1Text.setText(str(self.p1.health))
            self.time2 = time.time()

        # Physics calculations
        self.plyJump.calculate()  # Needed to actual update the position of the hitbox
        self.plyJump2.calculate()
        self.platform.calculate()

        time.sleep(.0083)  # Magic sleep number from jamie

    def createHealthBars(self, window):
        self.p1Text = Text(Point(50,50), str(self.p1.health))
        self.p2Text = Text(Point(1100, 50), str(self.p2.health))
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
            time.sleep(1)
        self.countDown.setText("Fight!")
        self.countDown.setSize(36)
        time.sleep(1)
        self.countDown.setText("")
