from updatedGraphics import Image, Text, Point, color_rgb


class StartScreen:
    def __init__(self,window):
        self.image = Image(Point(600,400),"ImagesAndSprites/StartScreen.gif")
        self.text = Text(Point(600,600),"Press Any Key To Start")
        self.text.setFace("arial")
        self.text.setSize(36)
        self.text.setStyle("normal")
        self.text.setTextColor(color_rgb(0, 0, 0))
        self.image.draw(window)
        self.text.draw(window)
        self.run(window)

    def run(self,window):
        r=1
        b=2
        g=3
        while(window.checkKey()==''):
            self.text.setTextColor(color_rgb(r,b,g))
            r+=1
            b+=2
            g+=3
            r=r%256
            b=b%256
            g=g%256
