from src.top import Top

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    from sys import argv
    app = QApplication(argv)
    Top = Top()
    app.exec()
