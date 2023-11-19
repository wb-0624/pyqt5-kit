from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QSizePolicy


class KitHDivider(QWidget):

    def __init__(self, parent=None):
        super(KitHDivider, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setFixedHeight(1)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)


class KitVDivider(QWidget):

    def __init__(self, parent=None):
        super(KitVDivider, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setFixedWidth(1)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)