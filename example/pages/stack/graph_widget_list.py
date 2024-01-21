from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from widget import KitIcon
from widget.component.menu.kit_menu import KitMenu
from .demo_card import DemoCard
from ... import HistogramGraphDemo, LineGraphDemo, PolarGraphDemo, PieGraphDemo, ScatterGraphDemo
from ...widgets_demo.combobox_demo import ComboBoxDemo
from ...widgets_demo.button_demo import *
from ...widgets_demo.checkbox_demo import *



class GraphWidgetList(QListWidget):

    def __init__(self, parent=None):
        super(GraphWidgetList, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSpacing(20)

        histogram_graph_card = DemoCard('柱状图', 'graph_demo.py', 'HistogramGraphDemo')
        histogram_graph_demo = HistogramGraphDemo()
        histogram_graph_card.setDemoWidget(histogram_graph_demo)
        self.addDemoCard(histogram_graph_card)

        line_graph_card = DemoCard('折线图', 'graph_demo.py', 'LineGraphDemo')
        line_graph_demo = LineGraphDemo()
        line_graph_card.setDemoWidget(line_graph_demo)
        self.addDemoCard(line_graph_card)

        polar_graph_card = DemoCard('极坐标图', 'graph_demo.py', 'PolarGraphDemo')
        polar_graph_demo = PolarGraphDemo()
        polar_graph_card.setDemoWidget(polar_graph_demo)
        self.addDemoCard(polar_graph_card)

        pie_graph_card = DemoCard('饼图', 'graph_demo.py', 'PieGraphDemo')
        pie_graph_demo = PieGraphDemo()
        pie_graph_card.setDemoWidget(pie_graph_demo)
        self.addDemoCard(pie_graph_card)

        scatter_graph_card = DemoCard('散点图', 'graph_demo.py', 'ScatterGraphDemo')
        scatter_graph_demo = ScatterGraphDemo()
        scatter_graph_card.setDemoWidget(scatter_graph_demo)
        self.addDemoCard(scatter_graph_card)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def contextMenuEvent(self, a0) -> None:
        menu = KitMenu(self)
        menu.addAction(KitIcon(Icons.md_add).toQIcon(), '添加')
        menu.addAction('删除')
        menu.exec_(a0.globalPos())

    def addDemoCard(self, card: DemoCard):
        demo_item = QListWidgetItem(self)
        demo_item.setSizeHint(card.sizeHint())
        self.setItemWidget(demo_item, card)
