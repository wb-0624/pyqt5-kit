from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from .demo_card import DemoCard
from ... import LineEchartsDemo, TemperatureEchartsDemo


class EchartsWidgetList(QListWidget):

    def __init__(self, parent=None):
        super(EchartsWidgetList, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSpacing(20)

        line_echarts_card = DemoCard('折线图', 'echarts_demo.py', 'LineEchartsDemo')
        line_echarts_card.setGraphicsEffect(None)
        line_echarts_demo = LineEchartsDemo()
        line_echarts_card.setDemoWidget(line_echarts_demo)
        self.addDemoCard(line_echarts_card)

        temperature_echarts_card = DemoCard('温度变化', 'echarts_demo.py', 'TemperatureEchartsDemo')
        temperature_echarts_card.setGraphicsEffect(None)
        temperature_echarts_demo = TemperatureEchartsDemo()
        temperature_echarts_card.setDemoWidget(temperature_echarts_demo)
        self.addDemoCard(temperature_echarts_card)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def addDemoCard(self, card: DemoCard):
        demo_item = QListWidgetItem(self)
        demo_item.setSizeHint(card.sizeHint())
        self.setItemWidget(demo_item, card)
