from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QScrollArea, QWidget

from example.widgets_demo import GraphDemo


class GraphStack(QScrollArea):

    def __init__(self, parent=None):
        super(GraphStack, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.content = QWidget()
        self.content.resize(500, 1000)
        self.setWidget(self.content)
        self.layout = QVBoxLayout()
        self.content.setLayout(self.layout)

        graph_demo = GraphDemo()
        self.layout.addWidget(graph_demo)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)