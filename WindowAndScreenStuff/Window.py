from graphics import GraphWin


class Window:
    def __init__(self, title, rows, columns, auto_flush=True):
        self._window = GraphWin(title,rows,columns, auto_flush)

    def getWindow(self):
        return self._window
