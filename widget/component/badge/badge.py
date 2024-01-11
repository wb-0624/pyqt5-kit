from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QLabel, QWidget

from app_config import Badge


class KitBadge(QLabel):

    def __init__(self, parent: QWidget):
        super(KitBadge, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setContentsMargins(4, 0, 4, 0)
        self.setAlignment(Qt.AlignCenter)
        self.parent().installEventFilter(self)
        self.setFixedHeight(14)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def __fresh_position(self):
        self.move(self.parent().rect().topRight().x() - self.width() - 2, 2)

    def eventFilter(self, obj, e: QEvent):
        if obj is self.parent():
            if e.type() in [QEvent.Resize, QEvent.Move, QEvent.Show]:
                self.__fresh_position()

        return super().eventFilter(obj, e)

    def setType(self, badge_type: Badge):
        self.setProperty('type', badge_type)
        self.style().polish(self)

    def setNum(self, a0: int) -> None:
        if 99 < a0 < 999:
            self.setText('99+')
        elif a0 > 999:
            self.setText('999+')
        else:
            self.setText(str(a0))


class KitDotBadge(KitBadge):

    def __init__(self, parent=None):
        super(KitDotBadge, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setFixedSize(8, 8)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setText(self, a0: str):
        raise TypeError('Dot badge cannot set text')
