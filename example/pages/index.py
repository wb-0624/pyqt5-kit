from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QHBoxLayout

from app_config.md_icons import Icons
from widget import KitTabBar

from .stack import DialogStack, BasicWidgetList
from .stack.graph_stack import GraphStack
from .stack.table_stack import TableStack


class Index(QWidget):

    def __init__(self, parent=None):
        super(Index, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_tab()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.navigation = KitTabBar()
        self.navigation.setFixedWidth(200)
        self.stack = QStackedWidget()
        self.layout.addWidget(self.navigation)
        self.layout.addWidget(self.stack)
        self.navigation.connectStackedWidget(self.stack)

    def __init_tab(self):
        self.navigation.addTab('basic', Icons.md_widgets)
        basic_stack = BasicWidgetList()
        self.stack.addWidget(basic_stack)
        self.navigation.setCurrentIndex(0)

        self.navigation.addTab('dialog', Icons.md_comment)
        dialog_stack = DialogStack()
        self.stack.addWidget(dialog_stack)

        self.navigation.addTab('graph', Icons.md_pie_chart)
        chart_stack = GraphStack()
        self.stack.addWidget(chart_stack)

        self.navigation.addTab('table', Icons.md_table_view)
        table_stack = TableStack()
        self.stack.addWidget(table_stack)

        self.navigation.layout.addStretch(1)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)