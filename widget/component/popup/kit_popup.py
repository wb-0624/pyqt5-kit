from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QApplication

from app_config.constant import Position


class KitPopup(QWidget):

    def __init__(self, parent):
        super(KitPopup, self).__init__(parent=parent)

        self.position = Position.Center

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.resize(self.sizeHint())
        shadow = QGraphicsDropShadowEffect()
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setBlurRadius(8)
        shadow.setColor(Qt.black)
        self.setGraphicsEffect(shadow)
        self.hide()

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def __init_position(self):
        # 当前窗口大小， 用来计算tip展示的位置
        window_size = self.parent().size()
        if self.position == Position.Center:
            self.move((window_size.width() - self.width()) // 2, (window_size.height() - self.height()) // 2)
        elif self.position == Position.Left:
            self.move(0 + self.offset, (window_size.height() - self.height()) // 2)
        elif self.position == Position.Right:
            self.move(window_size.width() - self.width() - self.offset,
                      (window_size.height() - self.height()) // 2)
        elif self.position == Position.Top:
            self.move((window_size.width() - self.width()) // 2, 0 + self.offset)
        elif self.position == Position.Bottom:
            self.move((window_size.width() - self.width()) // 2,
                      window_size.height() - self.height() - self.offset)
        elif self.position == Position.TopLeft:
            self.move(0 + self.offset, 0 + self.offset)
        elif self.position == Position.TopRight:
            self.move(window_size.width() - self.width() - self.offset, 0 + self.offset)
        elif self.position == Position.BottomLeft:
            self.move(0 + self.offset, window_size.height() - self.height() - self.offset)
        elif self.position == Position.BottomRight:
            self.move(window_size.width() - self.width() - self.offset,
                      window_size.height() - self.height() - self.offset)

    def show(self):
        self.__init_position()
        self.raise_()
        super().show()

    def paintEvent(self, a0):
        self.__init_position()
        super().paintEvent(a0)

    def sizeHint(self):
        return QSize(300, 180)

    def setPosition(self, position: int):
        self.position = position
