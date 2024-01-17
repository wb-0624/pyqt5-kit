from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QSizePolicy

from widget import KitCard


class StackCard(KitCard):

    def __init__(self, parent=None):
        super(StackCard, self).__init__(parent=parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        pass

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def sizeHint(self):
        return QSize(100, 80)