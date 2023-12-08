from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QHBoxLayout


class KitStatusBar(QWidget):

    def __init__(self, parent=None):
        super(KitStatusBar, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setFixedHeight(20)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(4, 0, 4, 0)
        self.setLayout(self.layout)

        self.status_label = QLabel('Ready')
        self.layout.addWidget(self.status_label)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def sizeHint(self):
        return QSize(800, 20)