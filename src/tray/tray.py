from PyQt5.Qt import *


class Tray(QSystemTrayIcon):
    def __init__(self, top):
        super(Tray, self).__init__(QIcon('assets/icon.png'))
        self.top = top

        self.setVisible(True)
        self.show()

        self.menu = QMenu()
        self.action_next = QAction("next")
        self.action_quit = QAction("quit")
        self.action_next.triggered.connect(self.do_next)
        self.action_quit.triggered.connect(self.do_quit)

        self.menu.addActions([self.action_next, self.action_quit])
        self.setContextMenu(self.menu)

    def do_next(self):
        pass

    @staticmethod
    def do_quit():
        quit(0)
