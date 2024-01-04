from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu


class KitMenu(QMenu):

    def __init__(self, parent=None):
        super(KitMenu, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        pass

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)