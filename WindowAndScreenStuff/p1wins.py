from graphics import Image, Point, Text

class StartScreen:
    def __init__(self,window):
        self.image = Image(Point(600,400),"ImagesAndSprites/MenuScreen.gif")
        self.text = Text(Point(600,600),"Player 1 Wins!")
        self.image.draw(window)
        self.text.draw(window)