from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget

from app_config.constant import Icons
from widget import KitTabBar


class Index(QWidget):

    def __init__(self, parent=None):
        super(Index, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_tab()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.navigation = KitTabBar()
        self.stack = QStackedWidget()
        self.layout.addWidget(self.navigation)
        self.layout.addWidget(self.stack)

    def __init_tab(self):
        self.navigation.addTab('basic', Icons.widgets)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)