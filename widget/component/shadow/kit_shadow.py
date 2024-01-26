from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QWidget


class KitShadow(QWidget):

    def __init__(self, parent, target: QWidget = None):
        super(KitShadow, self).__init__(parent=parent)

        self.target = target if target else parent

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.parent().installEventFilter(self)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self._shadow = QGraphicsDropShadowEffect(self)
        self._shadow.setOffset(0, 0)
        self._shadow.setBlurRadius(10)
        self._shadow.setColor(QColor('#808080'))
        self.setGraphicsEffect(self._shadow)

    def eventFilter(self, a0, a1) -> bool:
        if a1.type() == QEvent.Resize and isinstance(a0, QWidget):
            self.resize(self.target.size())
            self.move(self.target.pos())
        return super().eventFilter(a0, a1)

    def setTarget(self, target: QWidget):
        self.target = target

    def shadowEffect(self):
        return self._shadow

    def setShadowColor(self, color: QColor):
        self._shadow.setColor(color)
