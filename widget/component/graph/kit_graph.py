from typing import List
import numpy as np

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QGraphicsEllipseItem, QGridLayout
from PyQt5.QtGui import QColor, QBrush, QFont

import pyqtgraph as pg

from app_config.constant import Graph


def convertPolarToCartesian(theta, radius):
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y


class KitGraphWidget(pg.PlotWidget):

    def __init__(self, chart_data: List = None, parent=None):
        super(KitGraphWidget, self).__init__(parent=parent)
        self.chart_data = chart_data if chart_data is not None else []
        self.chart_text_size = 8
        self.setBackground('w')
        self.addLegend(offset=(0, 0))

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
        elif self.chart_type == Graph.Scatter:
            return KitScatterGraph(self.chart_data)
        elif self.chart_type == Graph.Pie:
            return KitPieGraph(self.chart_data)
        else:
            raise TypeError("graph type error")

    def showEvent(self, a0):
        super().showEvent(a0)


class KitHistogramGraph(KitGraphWidget):
    """
    柱状图
    @:param chart_data: 图表数据 [{name: '', value: 0, color: ''}]
        label: 标签
        value: 值
        color: 颜色 QColor or str
    """

    def __init__(self, chart_data: List = None, parent=None):
        super(KitHistogramGraph, self).__init__(chart_data=chart_data, parent=parent)

        self.names = []
        self.values = []
        self.colors = []

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.fresh_graph()

    def fresh_graph(self):
        self.clear()
        self.names = [item.get('name', '') for item in self.chart_data]
        self.values = [item.get('value', '0') for item in self.chart_data]
        self.colors = [item.get('color', 'b') for item in self.chart_data]

        self.setXRange(-1, len(self.names) + 1)
        self.setYRange(0, max(self.values) + 1)

        # 创建柱状图项
        for i in range(len(self.chart_data)):
            color = QColor(self.colors[i])
            bar_item = pg.BarGraphItem(x=i, height=self.values[i], width=0.5, name=self.names[i],
                                       brush=QColor(color.red(), color.green(), color.blue(), 50))
            bar_item.setOpts(pen={'width': 2, 'color': color})
            self.addItem(bar_item)

        # 设置 x 轴的刻度标签
        x_axis = self.getAxis('bottom')
        x_axis.setTicks([list(enumerate(self.names))])
        x_axis.setLabel('Categories')

        # 设置 y 轴的刻度范围和标签
        y_axis = self.getAxis('left')
        y_axis.setLabel('Values')

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)


class KitLineGraph(KitGraphWidget):
    """
    折线图
    @:param chart_data: 图表数据 [{x:[],y:[], color: '', name:''}]
    """

    def __init__(self, chart_data: List = None, parent=None):
        super(KitLineGraph, self).__init__(chart_data=chart_data, parent=parent)

        self.chart_data = chart_data if chart_data is not None else []
        self.x_lists = []
        self.y_lists = []
        self.names = []
        self.colors = []

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.fresh_graph()

    def fresh_graph(self):
        self.clear()
        self.x_lists = [item.get('x') for item in self.chart_data]
        self.y_lists = [item.get('y') for item in self.chart_data]
        self.names = [item.get('name', '') for item in self.chart_data]
        self.colors = [item.get('color', 'b') for item in self.chart_data]

        x_arr = np.array(self.x_lists)
        y_arr = np.array(self.y_lists)
        # 获取二维数组的最大值
        self.setXRange(-1, np.amax(x_arr) + 2)
        self.setYRange(-1, np.amax(y_arr) + 2)

        # 创建柱状图项
        for i in range(len(self.chart_data)):
            color = QColor(self.colors[i])
            # 创建折线图
            line_plot = pg.PlotDataItem(x=self.x_lists[i], y=self.y_lists[i], pen=pg.mkPen(color=color, width=1),
                                        antialias=True, name=self.names[i])
            # 将折线图添加到绘图区域
            self.addItem(line_plot)

        # 设置 x 轴的刻度标签
        self.setAxisLabel('bottom', 'X')

        # 设置 y 轴的刻度范围和标签
        self.setAxisLabel('left', 'Y')

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def __init_slot(self):
        pass


class KitPolarGraph(KitGraphWidget):
    """
    极坐标图
    @:param chart_data: 图表数据 [{a:[], r:[], color: '',name:''}]
    这里的a采用弧度制，而不是角度制。
    """

    def __init__(self, chart_data: List = None, parent=None):
        super(KitPolarGraph, self).__init__(chart_data=chart_data, parent=parent)

        self.theta_lists = []
        self.radius_lists = []
        self.names = []
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
        self.plotItem.getAxis('left').hide()
        self.plotItem.getAxis('bottom').hide()
        self.fresh_graph()

    def __init_polar(self):
        # 绘制 极坐标 线
        for i in range(8):
            x, y = convertPolarToCartesian(i * np.pi / 4, self.tick_count * self.tick_interval)
            line = pg.PlotDataItem(x=[0, x], y=[0, y], pen=pg.mkPen(width=0.8, color=self.polar_color), anlialias=True)
            self.addItem(line)
            label_x, label_y = convertPolarToCartesian(i * np.pi / 4, self.tick_count * self.tick_interval)
            label = pg.TextItem(str(i * 45), color=(0, 0, 0))
            label.setPos(label_x, label_y)
            label.setFont(QFont('Arial', self.chart_text_size))
            # 调整标签的位置
            if i == 0:
                label.setAnchor((0, 0.5))
            elif i == 1:
                label.setAnchor((0, 1))
            elif i == 2:
                label.setAnchor((0.5, 1))
            elif i == 3:
                label.setAnchor((1, 1))
            elif i == 4:
                label.setAnchor((1, 0.5))
            elif i == 5:
                label.setAnchor((1, 0))
            elif i == 6:
                label.setAnchor((0.5, 0))
            elif i == 7:
                label.setAnchor((0, 0))
            label.setParentItem(line)

        for r in range(0, (self.tick_count + 1) * self.tick_interval, self.tick_interval):
            circle = QGraphicsEllipseItem(-r, -r, r * 2, r * 2)
            circle.setPen(pg.mkPen(width=1, color=self.polar_color))
            label = pg.TextItem(str(r), color=(0, 0, 0))
            label.setFont(QFont('Arial', self.chart_text_size))
            label.setPos(0, r)
            label.setParentItem(circle)
            self.addItem(circle)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setTickCount(self, count: int):
        self.tick_count = count
        self.fresh_graph()

    def setTickInterval(self, interval: int):
        self.tick_interval = interval
        self.fresh_graph()

    def setPolarColor(self, color):
        self.polar_color = QColor(color)
        self.fresh_graph()

    def fresh_graph(self):
        self.clear()
        self.__init_polar()
        self.theta_lists = [item.get('a', '0') for item in self.chart_data]
        self.radius_lists = [item.get('r', '0') for item in self.chart_data]
        self.names = [item.get('name', '') for item in self.chart_data]
        self.colors = [item.get('color', 'b') for item in self.chart_data]

        for i in range(len(self.chart_data)):
            theta = self.theta_lists[i]
            radius = self.radius_lists[i]
            x, y = convertPolarToCartesian(theta, radius)
            plot = pg.PlotDataItem(x, y, pen=pg.mkPen(self.colors[i], width=1), antialias=True, name=self.names[i])
            self.addItem(plot)


class KitPieGraph(KitGraphWidget):
    """
    饼图
    @:param chart_data: 图表数据 [{name:'', value:'', color: '', offset:0}]
    """

    def __init__(self, chart_data: List = None, parent=None):
        super(KitPieGraph, self).__init__(chart_data=chart_data, parent=parent)

        self.names = []
        self.values = []
        self.colors = []
        self.offsets = []

        self._chart_size = 10

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setAspectLocked(True)
        self.setAntialiasing(True)
        self.plotItem.getAxis('left').hide()
        self.plotItem.getAxis('bottom').hide()
        self.fresh_graph()

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def fresh_graph(self):
        self.clear()
        self.names = [item.get('label', '') for item in self.chart_data]
        self.values = [item.get('value', 0) for item in self.chart_data]
        self.colors = [item.get('color', 'b') for item in self.chart_data]
        self.offsets = [item.get('offset', 0) for item in self.chart_data]

        values_sum = sum(self.values)
        start_angle = 0
        for i in range(len(self.chart_data)):
            color = QColor(self.colors[i])

            pie_item = QGraphicsEllipseItem(0, 0, self._chart_size, self._chart_size)
            pie_item.setPen(pg.mkPen(color, width=2))
            pie_item.setBrush(QBrush(QColor(color.red(), color.green(), color.blue(), 50)))
            pie_item.setStartAngle(int(start_angle) * 16)
            span_angle = self.values[i] / values_sum * 360
            pie_item.setSpanAngle(int(span_angle) * 16)

            label = pg.TextItem(str(round(self.values[i] / values_sum * 100, 2)) + '%', color='black')
            label.setParentItem(pie_item)
            label.setFont(QFont('Arial', self.chart_text_size))
            label_x, label_y = convertPolarToCartesian((start_angle + span_angle / 2) * np.pi / 180, 2.5)
            label.setPos(self._chart_size / 2 + label_x, self._chart_size / 2 - label_y)
            self.addItem(
                pg.PlotDataItem([label.pos().x()], [label.pos().y()], pen=pg.mkPen(color, width=1), antialias=True,
                                name=self.names[i]))
            label.setAnchor((0.5, 0.5))

            if float(self.offsets[i]) > 0:
                offset_x, offset_y = convertPolarToCartesian((start_angle + span_angle / 2) * np.pi / 180,
                                                             self.offsets[i])
                pie_item.moveBy(offset_x, -offset_y)
            start_angle += span_angle
            self.addItem(pie_item)


class KitScatterGraph(KitGraphWidget):
    """
    散点图
    @:param chart_data: 图表数据 [{name:'', x:'', y:'', symbol:{color,size,shape}}]
    """

    def __init__(self, chart_data: List = None, parent=None):
        super(KitScatterGraph, self).__init__(chart_data=chart_data, parent=parent)
        self.x_lists = []
        self.y_lists = []
        self.names = []

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.fresh_graph()

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def fresh_graph(self):
        self.clear()
        self.x_lists = [item.get('x', []) for item in self.chart_data]
        self.y_lists = [item.get('y', []) for item in self.chart_data]
        self.names = [item.get('name', '') for item in self.chart_data]

        self.setXRange(min([min(x) for x in self.x_lists]), max([max(x) for x in self.x_lists])+1)
        self.setYRange(min([min(y) for y in self.y_lists]), max([max(y) for y in self.y_lists])+1)

        for i in range(len(self.chart_data)):
            x = self.chart_data[i].get('x', [])
            y = self.chart_data[i].get('y', [])
            symbol = self.chart_data[i].get('symbol', {})
            plot = pg.ScatterPlotItem(x, y, pen=None, size=symbol.get('size', 10),
                                      symbol=symbol.get('shape', 'o'), antialias=True, name=self.chart_data[i].get('name', ''))
            color = QColor(symbol.get('color', 'black'))
            plot.setPen(pg.mkPen(color, width=1))
            plot.setBrush(QBrush(QColor(color.red(), color.green(), color.blue(), 50)))
            self.addItem(plot)


