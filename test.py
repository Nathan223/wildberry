from updatedGraphics import *
def main():
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    click = win.getMouse() # Pause to view result
    print(click)
    win.close()    # Close window when done
main()