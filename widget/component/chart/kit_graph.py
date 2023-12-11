from typing import List
import numpy as np

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QGraphicsEllipseItem, QGridLayout
from PyQt5.QtGui import QColor

import pyqtgraph as pg
from app_config.constant import Graph

from widget.component.window.kit_frameless_window import KitFramelessWindow


class KitGraphWidget(pg.PlotWidget):

    def __init__(self, chart_data: List = None, parent=None):
        super(KitGraphWidget, self).__init__(parent=parent)
        self.chart_data = chart_data if chart_data is not None else []
        self.setBackground('w')

    def setChartData(self, chart_data: List):
        self.chart_data = chart_data

    def setChartTitle(self, chart_title: str):
        self.plotItem.setTitle(chart_title)

    def setChartBackgroundColor(self, color):
        self.setBackground(QColor(color))

    def setAxisLabel(self, axis: str, label: str):
        try:
            self.plotItem.getAxis(axis).setLabel(label)
        except Exception as e:
            raise TypeError(e)


class KitGraph(QWidget):

    def __init__(self, chart_type: Graph = Graph.Histogram, chart_data=None, parent=None):
        super(KitGraph, self).__init__(parent=parent)

        self.chart_data = [] if chart_data is None else chart_data
        self.chart_type = chart_type
        self.chart = self.generateChart()

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setAttribute(Qt.WA_NativeWindow)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.chart)

    def __init_slot(self):
        self.chart.sigRangeChanged.connect(lambda: self.update())

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def generateChart(self):
        if self.chart_type == Graph.Histogram:
            return KitHistogramGraph(self.chart_data)
        elif self.chart_type == Graph.Line:
            return KitLineGraph(self.chart_data)
        elif self.chart_type == Graph.Polar:
            return KitPolarGraph(self.chart_data)
        else:
            raise TypeError("chart type error")

    def showEvent(self, a0):
        if self.parent() is not None:
            self.parent().setAttribute(Qt.WA_DontCreateNativeAncestors)
        super().showEvent(a0)


class KitHistogramGraph(KitGraphWidget):
    """
    柱状图
    @:param chart_data: 图表数据 [{label: '', value: 0, color: ''}]
        label: 标签
        value: 值
        color: 颜色 QColor or str
    """

    def __init__(self, chart_data: List = None, parent=None):
        super(KitHistogramGraph, self).__init__(chart_data=chart_data, parent=parent)

        self.labels = []
        self.values = []
        self.colors = []

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.fresh_chart()

    def fresh_chart(self):
        self.clear()
        self.labels = [item.get('label', '') for item in self.chart_data]
        self.values = [item.get('value', '0') for item in self.chart_data]
        self.colors = [item.get('color', 'b') for item in self.chart_data]

        # 创建柱状图项
        for i in range(len(self.chart_data)):
            color = QColor(self.colors[i])
            bar_item = pg.BarGraphItem(x=i, height=self.values[i], width=0.5,
                                       brush=QColor(color.red(), color.green(), color.blue(), 50))
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


class KitLineGraph(KitGraphWidget):
    """
    折线图
    @:param chart_data: 图表数据 [{x:[],y:[], color: ''}]
    """

    def __init__(self, chart_data: List = None, parent=None):
        super(KitLineGraph, self).__init__(chart_data=chart_data, parent=parent)

        self.chart_data = chart_data if chart_data is not None else []
        self.x_lists = []
        self.y_lists = []
        self.colors = []

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.fresh_chart()

    def fresh_chart(self):
        self.clear()
        self.x_lists = [item.get('x') for item in self.chart_data]
        self.y_lists = [item.get('y') for item in self.chart_data]
        self.colors = [item.get('color', 'b') for item in self.chart_data]

        # 创建柱状图项
        for i in range(len(self.chart_data)):
            color = QColor(self.colors[i])
            # 创建折线图
            line_plot = pg.PlotDataItem(x=self.x_lists[i], y=self.y_lists[i], pen=pg.mkPen(color=color, width=1),
                                        antialias=True)
            # 将折线图添加到绘图区域
            self.addItem(line_plot)

        # 设置 x 轴的刻度标签
        self.setAxisLabel('bottom', 'X')
        self.setXRange(0, max([max(item) for item in self.x_lists]) + 5)

        # 设置 y 轴的刻度范围和标签
        self.setAxisLabel('left', 'Y')
        self.setYRange(0, max([max(item) for item in self.y_lists]) + 5)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def __init_slot(self):
        pass


class KitPolarGraph(KitGraphWidget):
    """
    极坐标图
    @:param chart_data: 图表数据 [{a:[], r:[], color: ''}]
    这里的a采用弧度制，而不是角度制。
    """

    def __init__(self, chart_data: List = None, parent=None):
        super(KitPolarGraph, self).__init__(chart_data=chart_data, parent=parent)

        self.theta_lists = []
        self.radius_lists = []
        self.colors = []
        self.tick_count = 10
        self.tick_interval = 10
        self.polar_color = QColor(0, 0, 0, 50)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setAspectLocked(True)
        self.setAntialiasing(True)
        self.fresh_chart()

    def __init_polar(self):
        self.plotItem.getAxis('left').hide()
        self.plotItem.getAxis('bottom').hide()
        # 绘制 极坐标 线
        for i in range(8):
            x, y = self.convertPolarToCartesian(i * np.pi / 4, (self.tick_count + 1) * self.tick_interval)
            line = pg.PlotDataItem(x=[0, x], y=[0, y], pen=pg.mkPen(width=0.8, color=self.polar_color), anlialias=True)
            self.addItem(line)
            label = pg.TextItem(str(i * 45), color=(0, 0, 0))
            label.setPos(x, y)
            label.setParentItem(line)

        for r in range(0, (self.tick_count + 1) * self.tick_interval, self.tick_interval):
            circle = QGraphicsEllipseItem(-r, -r, r * 2, r * 2)
            circle.setPen(pg.mkPen(width=1, color=self.polar_color))
            label = pg.TextItem(str(r), color=(0, 0, 0))
            label.setPos(0, r)
            label.setParentItem(circle)
            self.addItem(circle)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setTickCount(self, count: int):
        self.tick_count = count
        self.fresh_chart()

    def setTickInterval(self, interval: int):
        self.tick_interval = interval
        self.fresh_chart()

    def setPolarColor(self, color):
        self.polar_color = QColor(color)
        self.fresh_chart()

    def convertPolarToCartesian(self, theta, radius):
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return x, y

    def fresh_chart(self):
        self.clear()
        self.__init_polar()
        self.theta_lists = [item.get('a', '0') for item in self.chart_data]
        self.radius_lists = [item.get('r', '0') for item in self.chart_data]
        self.colors = [item.get('color', 'b') for item in self.chart_data]

        for i in range(len(self.chart_data)):
            theta = self.theta_lists[i]
            radius = self.radius_lists[i]
            x, y = self.convertPolarToCartesian(theta, radius)
            plot = pg.PlotDataItem(x, y, pen=pg.mkPen(self.colors[i], width=1), antialias=True)
            self.addItem(plot)


if __name__ == "__main__":
    from PyQt5.QtGui import QFontDatabase
    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(Qt.AA_NativeWindows)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
    window = KitFramelessWindow()
    main = QWidget()
    layout = QGridLayout()
    main.setLayout(layout)
    c_data = [
        {'label': 'A', 'value': 10, 'color': 'red'},
        {'label': 'B', 'value': 20, 'color': 'green'},
        {'label': 'C', 'value': 30, 'color': 'b'},
        {'label': 'D', 'value': 40, 'color': 'yellow'},
    ]
    chart_1 = KitGraph(Graph.Histogram, c_data)
    layout.addWidget(chart_1, 0, 0, 1, 1)

    l_data = [
        {'x': [1, 2, 3, 4, 5], 'y': [10, 2, 3, 4, 5], 'color': 'red'},
        {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 10, 2, 1], 'color': 'green'},
        {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 10, 5], 'color': 'blue'},
    ]
    chart_2 = KitGraph(Graph.Line, l_data)
    layout.addWidget(chart_2, 0, 1, 1, 1)

    p_data = [
        {'a': [0.78, 2, 3, 4, 5], 'r': [10, 2, 3, 4, 5], 'color': 'red'},
        {'a': [1, 2, 3, 4, 5], 'r': [5, 4, 10, 2, 1], 'color': 'green'},
        {'a': [1, 2, 3, 4, 5], 'r': [1, 2, 3, 10, 5], 'color': 'blue'},
    ]
    chart_3 = KitGraph(Graph.Polar, p_data)
    chart_3.chart.setTickInterval(1)
    chart_3.chart.setTickCount(10)
    layout.addWidget(chart_3, 1, 0, 1, 1)

    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
