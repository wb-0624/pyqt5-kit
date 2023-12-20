from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class DialogStack(QWidget):

    def __init__(self, parent=None):
        super(DialogStack, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)