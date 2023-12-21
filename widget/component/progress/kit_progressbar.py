from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt


class KitProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTextVisible(False)

    def setColor(self, color: str):
        self.setStyleSheet(self.styleSheet() + f'KitProgressBar::chunk {{background-color: {color};}}')



