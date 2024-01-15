from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import QLabel, QSizePolicy


class KitIcon(QLabel):
    def __init__(self, icon_str=None, parent=None):
        super().__init__(parent=parent)
        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

        self.icon_str = None
        self.setIcon(icon_str)

    def __init_widget(self):
        self.setAlignment(Qt.AlignCenter)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIcon(self, icon_str: str):
        self.icon_str = icon_str
        self.setText(icon_str)

    def iconStr(self):
        return self.icon_str

    def setIconColor(self, color):
        self.setStyleSheet(self.styleSheet()+"color: %s;" % color)

    def toQIcon(self) -> QIcon:
        img = self.grab().toImage()
        pixmap = QPixmap.fromImage(img)

        return QIcon(pixmap)

    def toPixmap(self) -> QPixmap:
        img = self.grab().toImage()
        pixmap = QPixmap.fromImage(img)

        return pixmap



