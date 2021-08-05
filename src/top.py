from PyQt5.Qt import *
from src.preference.preference import Preference
from src.tray.tray import Tray


class Top(QWidget):
    def __init__(self):
        super(Top, self).__init__()
        self.preference = Preference(self)
        self.tray = Tray(self)
