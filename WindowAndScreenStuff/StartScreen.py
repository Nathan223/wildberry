from updatedGraphics import Image, Text, Point, color_rgb


class StartScreen:
    def __init__(self,window):
        self.image = Image(Point(600,400),"ImagesAndSprites/StartScreen.gif")
        self.text = Text(Point(600,600),"Press Any Key To Start")
        self.text.setFace("arial")
        self.text.setSize(36)
        self.text.setStyle("normal")
        self.text.setTextColor(color_rgb(255, 255, 255))
        self.image.draw(window)
        self.text.draw(window)