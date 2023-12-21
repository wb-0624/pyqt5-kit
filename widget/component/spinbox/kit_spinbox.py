from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QSpinBox, QStyleOptionSpinBox, QStyle, QDoubleSpinBox

from ..icon import KitIcon
from app_config.constant import Icons


class KitSpinBox(QSpinBox):

    def __init__(self, parent=None):
        super(KitSpinBox, self).__init__(parent=parent)
        self.indicator_size = 16

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        pass

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIndicatorIconSize(self, size):
        self.indicator_size = size
        self.update()

    def sizeHint(self):
        return QSize(100, 32)

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        opt = QStyleOptionSpinBox()
        opt.initFrom(self)

        arrow_up_rect = self.style().subControlRect(QStyle.CC_SpinBox, opt, QStyle.SC_SpinBoxUp, self)
        arrow_down_rect = self.style().subControlRect(QStyle.CC_SpinBox, opt, QStyle.SC_SpinBoxDown, self)

        opt.rect = QRect(arrow_up_rect.center().x()-self.indicator_size//2,
                         arrow_up_rect.center().y()-self.indicator_size//2, self.indicator_size, self.indicator_size)
        icon = KitIcon(Icons.expand_less)
        icon.setObjectName('icon')
        painter.drawPixmap(opt.rect, icon.toPixmap())
        opt.rect = QRect(arrow_down_rect.center().x()-self.indicator_size//2,
                         arrow_down_rect.center().y()-self.indicator_size//2, self.indicator_size, self.indicator_size)
        icon = KitIcon(Icons.expand_more)
        icon.setObjectName('icon')
        painter.drawPixmap(opt.rect, icon.toPixmap())


class KitDoubleSpinBox(QDoubleSpinBox):

    def __init__(self, parent=None):
        super(KitDoubleSpinBox, self).__init__(parent=parent)
        self.indicator_size = 16

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        pass

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIndicatorIconSize(self, size):
        self.indicator_size = size
        self.update()

    def sizeHint(self):
        return QSize(100, 32)

    def paintEvent(self, e):
        super().paintEvent(e)

        painter = QPainter(self)
        opt = QStyleOptionSpinBox()
        opt.initFrom(self)

        arrow_up_rect = self.style().subControlRect(QStyle.CC_SpinBox, opt, QStyle.SC_SpinBoxUp, self)
        arrow_down_rect = self.style().subControlRect(QStyle.CC_SpinBox, opt, QStyle.SC_SpinBoxDown, self)

        opt.rect = QRect(arrow_up_rect.center().x()-self.indicator_size//2,
                         arrow_up_rect.center().y()-self.indicator_size//2, self.indicator_size, self.indicator_size)
        icon = KitIcon(Icons.expand_less)
        icon.setObjectName('spinbox_icon')
        painter.drawPixmap(opt.rect, icon.toPixmap())
        opt.rect = QRect(arrow_down_rect.center().x()-self.indicator_size//2,
                         arrow_down_rect.center().y()-self.indicator_size//2, self.indicator_size, self.indicator_size)
        icon = KitIcon(Icons.expand_more)
        icon.setObjectName('spinbox_icon')
        painter.drawPixmap(opt.rect, icon.toPixmap())
