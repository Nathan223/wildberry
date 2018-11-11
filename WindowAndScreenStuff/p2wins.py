from graphics import Image, Text, Point

class p2wins:
    def __init__(self,window):
        self.image = Image(Point(600,400),"ImagesAndSprites/MenuScreen.gif")
        self.text = Text(Point(600,600),"Player 2 Wins!")
        self.text.setSize(36)
        self.image.draw(window)
        self.text.draw(window)