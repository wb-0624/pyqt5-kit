from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
import pyqtgraph as pg

from widget.component.window.kit_frameless_window import KitFramelessWindow


class KitHistogramChart(pg.PlotWidget):
    """
    柱状图
    @:param chart_data: 图表数据 [{label: '', value: 0, color: ''}]
        label: 标签
        value: 值
        color: 颜色 QColor or str
    """

    def __init__(self, chart_data: List = None, parent=None):
        super(KitHistogramChart, self).__init__(parent=parent)

        self.chart_data = chart_data
        self.labels = []
        self.values = []
        self.colors = []

        if chart_data is None:
            self.chart_data = []

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setBackground('w')
        self.__fresh_chart_data()

    def setChartBackgroundColor(self, color: [QColor, str]):
        self.setBackground(color)

    def setChartData(self, chart_data: List):
        self.chart_data = chart_data

    def __fresh_chart_data(self):
        self.labels = [item['label'] for item in self.chart_data]
        self.values = [item['value'] for item in self.chart_data]
        self.colors = [item['color'] for item in self.chart_data]

        # 创建柱状图项
        for i in range(len(self.chart_data)):
            color = QColor(self.colors[i])
            bar_item = pg.BarGraphItem(x=i, height=self.values[i], width=0.5, brush=QColor(color.red(), color.green(), color.blue(), 80))
            bar_item.setOpts(pen={'width': 2, 'color': color})
            self.addItem(bar_item)

        # 设置 x 轴的刻度标签
        x_axis = self.getAxis('bottom')
        x_axis.setTicks([list(enumerate(self.labels))])
        x_axis.setLabel('Categories')

        # 设置 y 轴的刻度范围和标签
        y_axis = self.getAxis('left')
        y_axis.setRange(0, max(self.values) + 5)
        y_axis.setLabel('Values')

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)


class KitChart(QWidget):

    def __init__(self, parent=None):
        super(KitChart, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        pass

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)


if __name__ == "__main__":
    from PyQt5.QtGui import QFontDatabase
    from config import config
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
    window = KitFramelessWindow()

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    bar_chart = KitHistogramChart(
        [
            {'label': 'A', 'value': 10, 'color': 'red'},
            {'label': 'B', 'value': 20, 'color': 'green'},
            {'label': 'C', 'value': 30, 'color': 'blue'},
            {'label': 'D', 'value': 40, 'color': 'yellow'},
        ]
    )

    layout.addWidget(bar_chart)

    window.setCentralWidget(main)

    window.show()
    sys.exit(app.exec_())