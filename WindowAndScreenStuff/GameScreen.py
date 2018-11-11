from Stage import Stage
from graphics import Text,Image,Point
from Characters.Player import *
from physics2 import hitbox
import time
from WindowAndScreenStuff import p1wins, p2wins


class GameScreen:
    def __init__(self, window, player1, player2):
        self.p1 = Player(player1, None)
        self.p2 = Player(player2, None)
        background = Image(Point(600, 400), "ImagesAndSprites/StartScreen.gif")
        background.draw(window)
        self.createHealthBars(window)
        self.startGame(window)
        self.countDown = Text(Point(window.getWidth() / 2, window.getHeight() / 2), '')
        self.countdown(window)
        self.time1 = 0
        self.time2 = 0
        self.winner = 0

        if self.checkExit(window.checkKey()):
            window.close()

        # This is just the objects
        plyJumpRender = Image(Point(300, 50), "ImagesAndSprites/Apple.gif")
        plyJumpRender.draw(window)

        plyJumpRender2 = Image(Point(900, 50), "ImagesAndSprites/Apple.gif")
        plyJumpRender2.draw(window)
            # plyJumpRender2.move(150, 0)

        worldRenderer = Image(Point(800, 3), "ImagesAndSprites/blue.gif")
        worldRenderer.draw(window)
        worldRenderer.move(-200, 400)

            # Hitbox defines as
            # Obj, width, height, weight, pos, ignored
        plyJump = hitbox(plyJumpRender, 1)
        plyJump2 = hitbox(plyJumpRender2, 1)
        platform = hitbox(worldRenderer, 0)

        while True:
            # Controls
            controls = window.checkKeys()
            if "w" in controls and plyJump.inAir == False:
                plyJump.addYForce(20)
            if "a" in controls:
                plyJump.addXForce(5)
            if "d" in controls:
                plyJump.addXForce(-5)
            if "e" in controls and abs(plyJump.position[0] - plyJump2.position[0]) < 120 and abs(plyJump.position[1] - plyJump2.position[1]) < 120 and time.time() - self.time1 > .5:
                self.p2.health -= 5
                self.p2Text.setText(str(self.p2.health))
                self.time1 = time.time()
            if "Up" in controls and plyJump2.inAir == False:
                plyJump2.addYForce(20)
            if "Left" in controls:
                plyJump2.addXForce(5)
            if "Right" in controls:
                plyJump2.addXForce(-5)
            if "Insert" in controls and abs(plyJump.position[0] - plyJump2.position[0]) < 120 and abs(plyJump.position[1] - plyJump2.position[1]) < 120 and time.time() - self.time2 > .5:
                self.p1.health -= 5
                self.p1Text.setText(str(self.p1.health))
                self.time2 = time.time()

            #if self.p1.health <= 0:
                #self.winner = 2

            #if self.p2.health <= 0:
               # self.winner = 1
            #if self.p1.health <= 0

            # Physics calculations
            plyJump.calculate()  # Needed to actual update the position of the hitbox
            plyJump2.calculate()
            platform.calculate()

            time.sleep(0.0083)  # Magic sleep number from jamie

    def checkExit(self, key):
        if key == 'Escape':
            return True
        return False

    def checkLose(self):
        pass

    def getWinner(self):
        return self.winner



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
