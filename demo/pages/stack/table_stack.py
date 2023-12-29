from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QScrollArea, QWidget

from demo.widgets_demo import TableDemo


class TableStack(QScrollArea):

    def __init__(self, parent=None):
        super(TableStack, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.content = QWidget()
        self.content.resize(500, 500)
        self.setWidget(self.content)
        self.layout = QVBoxLayout()
        self.content.setLayout(self.layout)

        table_demo = TableDemo()
        self.layout.addWidget(table_demo)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)