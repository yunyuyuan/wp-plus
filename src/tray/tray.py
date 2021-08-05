from PyQt5.Qt import *


class Tray(QSystemTrayIcon):
    def __init__(self, top):
        super(Tray, self).__init__(QIcon('../../assets/icon.png'), top)

        self.show()
