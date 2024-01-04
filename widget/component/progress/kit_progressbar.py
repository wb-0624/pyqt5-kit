from PyQt5.QtWidgets import QProgressBar


class KitProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTextVisible(False)

    def setColor(self, color: str):
        self.setStyleSheet(self.styleSheet() + f'KitProgressBar::chunk {{background-color: {color};}}')



