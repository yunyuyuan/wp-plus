from PyQt5.Qt import *


class Preference(QWidget):
    def __init__(self, top):
        super(Preference, self).__init__(parent=top)

        # set ui
        layout = QGridLayout(self)
        self.setLayout(layout)
