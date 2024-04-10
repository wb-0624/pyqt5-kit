from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QSizePolicy

"""
如果卡片组件的内容是需要频繁刷新的，则将卡片组件的阴影去掉，否则会导致卡顿。 card.setGraphicsEffect(None)
"""


class KitCard(QWidget):

    def __init__(self, parent=None):
        super(KitCard, self).__init__(parent=parent)

        self._hover_animation = True

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setMouseTracking(True)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor('#b4b4b4'))
        self.setGraphicsEffect(self.shadow)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setHoverAnimation(self, enable: bool):
        self._hover_animation = enable

    def enterEvent(self, a0):
        if not self._hover_animation or self.graphicsEffect() is None:
            return
        self.shadow.setBlurRadius(30)
        self.setGraphicsEffect(self.shadow)

    def leaveEvent(self, a0):
        if not self._hover_animation or self.graphicsEffect() is None:
            return
        self.shadow.setBlurRadius(10)
        self.setGraphicsEffect(self.shadow)



