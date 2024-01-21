from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QHBoxLayout

from app_config.md_icons import Icons
from widget import KitTabBar, KitIcon, KitMenu

from .stack import DialogWidgetList, BasicWidgetList
from .stack.data_widget_list import DataWidgetList
from .stack.graph_widget_list import GraphWidgetList
from .stack.input_widget_list import InputWidgetList
from .stack.state_widget_list import StateWidgetList
from .stack.table_widget_list import TableWidgetList


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
        basic_list = BasicWidgetList()
        self.stack.addWidget(basic_list)
        self.navigation.setCurrentIndex(0)

        self.navigation.addTab('state', Icons.md_query_stats)
        state_list = StateWidgetList(self)
        self.stack.addWidget(state_list)

        # add data tab
        self.navigation.addTab('data', Icons.md_data_usage)
        data_list = DataWidgetList(self)
        self.stack.addWidget(data_list)

        # add input tab
        self.navigation.addTab('input', Icons.md_input)
        input_list = InputWidgetList(self)
        self.stack.addWidget(input_list)

        self.navigation.addTab('dialog', Icons.md_comment)
        dialog_stack = DialogWidgetList(self)
        self.stack.addWidget(dialog_stack)

        self.navigation.addTab('graph', Icons.md_pie_chart)
        chart_stack = GraphWidgetList(self)
        self.stack.addWidget(chart_stack)

        self.navigation.addTab('table', Icons.md_table_view)
        table_stack = TableWidgetList(self)
        self.stack.addWidget(table_stack)

        self.navigation.layout.addStretch(1)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def contextMenuEvent(self, a0) -> None:
        menu = KitMenu(self)
        menu.addAction(KitIcon(Icons.md_add).toQIcon(), '添加')
        menu.addAction('删除')
        menu.exec_(a0.globalPos())
