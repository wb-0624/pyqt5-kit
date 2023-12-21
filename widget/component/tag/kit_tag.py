from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel, QSizePolicy


class KitTag(QLabel):
    """
    `KitTag` 类是 `QLabel` 的子类，它表示具有可自定义文本和背景颜色的彩色标签。
    """

    def __init__(self, text=None, color=None, parent=None):
        """
        :param text:   标签内容
        :param color:  能被QColor识别的颜色字符串， 边框颜色， 背景颜色是其透明化
        :param parent:
        """
        super(KitTag, self).__init__(text=text, parent=parent)

        self.color = color if color is not None else 'black'
        self.setColor(self.color)

        self.setFixedHeight(20)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setColor(self, color: str):
        if color is None:
            return
        self.color = color
        color = QColor(color)
        red = color.red()
        green = color.green()
        blue = color.blue()
        self.setStyleSheet(
            self.styleSheet() + f"background-color: rgba({red}, {green}, {blue}, 0.3); border: 1px solid rgb({red}, {green}, {blue})")



