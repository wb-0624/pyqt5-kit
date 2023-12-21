from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_NativeWindow, True)

        self.buffer = QPixmap()

    def paintEvent(self, event):
        if self.buffer.isNull():
            self.buffer = QPixmap(self.size())
            self.buffer.fill(Qt.transparent)

        painter = QPainter(self.buffer)
        painter.setRenderHint(QPainter.Antialiasing)

        # Perform your custom drawing operations
        self.drawCustomContent(painter)

        painter.end()

        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.buffer)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()