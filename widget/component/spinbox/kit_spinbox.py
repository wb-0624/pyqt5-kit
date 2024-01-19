from PyQt5.QtCore import Qt, QSize, QRect, QObject, QEvent
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QSpinBox, QStyleOptionSpinBox, QStyle, QDoubleSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit, \
    QAbstractSpinBox, QWidget

from ..icon import KitIcon
from app_config.md_icons import Icons


class SpinBoxEventFilter(QObject):
    def __init__(self, spinbox: QWidget):
        super(SpinBoxEventFilter, self).__init__()
        self.target = spinbox
        self.target.installEventFilter(self)

    def eventFilter(self, a0, a1) -> bool:
        if isinstance(self.target, QAbstractSpinBox):
            if a1.type() == QEvent.Paint:
                self.target.paintEvent(a1)
                painter = QPainter(self.target)
                opt = QStyleOptionSpinBox()
                opt.initFrom(self.target)

                arrow_up_rect = self.target.style().subControlRect(QStyle.CC_SpinBox, opt, QStyle.SC_SpinBoxUp,
                                                                   self.target)
                arrow_down_rect = self.target.style().subControlRect(QStyle.CC_SpinBox, opt, QStyle.SC_SpinBoxDown,
                                                                     self.target)

                opt.rect = QRect(arrow_up_rect.center().x() - self.target.indicator_size // 2,
                                 arrow_up_rect.center().y() - self.target.indicator_size // 2,
                                 self.target.indicator_size,
                                 self.target.indicator_size)
                icon = KitIcon(Icons.md_expand_less)
                icon.setObjectName('spinbox_icon')
                painter.drawPixmap(opt.rect, icon.toPixmap())
                opt.rect = QRect(arrow_down_rect.center().x() - self.target.indicator_size // 2,
                                 arrow_down_rect.center().y() - self.target.indicator_size // 2,
                                 self.target.indicator_size,
                                 self.target.indicator_size)
                icon = KitIcon(Icons.md_expand_more)
                icon.setObjectName('spinbox_icon')
                painter.drawPixmap(opt.rect, icon.toPixmap())
                return True
        return super().eventFilter(a0, a1)


class KitSpinBox(QSpinBox):

    def __init__(self, parent=None):
        super(KitSpinBox, self).__init__(parent=parent)
        self.indicator_size = 16
        self.event_filter = SpinBoxEventFilter(self)

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


class KitDoubleSpinBox(QDoubleSpinBox):

    def __init__(self, parent=None):
        super(KitDoubleSpinBox, self).__init__(parent=parent)
        self.indicator_size = 16

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.event_filter = SpinBoxEventFilter(self)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIndicatorIconSize(self, size):
        self.indicator_size = size
        self.update()

    def sizeHint(self):
        return QSize(100, 32)


class KitDateSpinBox(QDateEdit):

    def __init__(self, parent=None):
        super(KitDateSpinBox, self).__init__(parent=parent)
        self.indicator_size = 16

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.event_filter = SpinBoxEventFilter(self)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIndicatorIconSize(self, size):
        self.indicator_size = size
        self.update()

    def sizeHint(self):
        return QSize(100, 32)


class KitTimeSpinBox(QTimeEdit):

    def __init__(self, parent=None):
        super(KitTimeSpinBox, self).__init__(parent=parent)
        self.indicator_size = 16

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.event_filter = SpinBoxEventFilter(self)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIndicatorIconSize(self, size):
        self.indicator_size = size
        self.update()

    def sizeHint(self):
        return QSize(100, 32)


class KitDateTimeSpinBox(QDateTimeEdit):

    def __init__(self, parent=None):
        super(KitDateTimeSpinBox, self).__init__(parent=parent)
        self.indicator_size = 16

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.event_filter = SpinBoxEventFilter(self)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIndicatorIconSize(self, size):
        self.indicator_size = size
        self.update()

    def sizeHint(self):
        return QSize(100, 32)
