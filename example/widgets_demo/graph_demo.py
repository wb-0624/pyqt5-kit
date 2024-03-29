from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

from app_config.constant import Graph
from widget import KitFramelessWindow, KitGraph


class HistogramGraphDemo(QWidget):
    def __init__(self, parent=None):
        super(HistogramGraphDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)
        c_data = [
            {'name': 'A', 'value': 10, 'color': 'red'},
            {'name': 'B', 'value': 20, 'color': 'green'},
            {'name': 'C', 'value': 30, 'color': 'b'},
            {'name': 'D', 'value': 40, 'color': 'blue'},
        ]
        chart_1 = KitGraph(Graph.Histogram, c_data)
        layout.addWidget(chart_1)


class LineGraphDemo(QWidget):
    def __init__(self, parent=None):
        super(LineGraphDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        l_data = [
            {'x': [1, 2, 3, 4, 5], 'y': [10, 2, 3, 4, 5], 'color': 'red', 'name': 'y1'},
            {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 10, 2, 1], 'color': 'green', 'name': 'y2'},
            {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 10, 5], 'color': 'blue', 'name': 'y3'},
        ]
        chart_2 = KitGraph(Graph.Line, l_data)
        layout.addWidget(chart_2)


class PolarGraphDemo(QWidget):
    def __init__(self, parent=None):
        super(PolarGraphDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        p_data = [
            {'a': [0.78, 2, 3, 4, 5], 'r': [10, 2, 3, 4, 5], 'color': 'red', 'name': 'y1'},
            {'a': [1, 2, 3, 4, 5], 'r': [5, 4, 10, 2, 1], 'color': 'green', 'name': 'y2'},
            {'a': [1, 2, 3, 4, 5], 'r': [1, 2, 3, 10, 5], 'color': 'blue', 'name': 'y3'},
        ]
        chart_3 = KitGraph(Graph.Polar, p_data)
        chart_3.chart.setTickInterval(2)
        chart_3.chart.setTickCount(5)
        layout.addWidget(chart_3)

class PieGraphDemo(QWidget):
    def __init__(self, parent=None):
        super(PieGraphDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        pie_data = [
            {'label': 'A', 'value': 10, 'color': 'red', 'name': 'y1'},
            {'label': 'B', 'value': 20, 'color': 'green', 'offset': 0.5, 'name': 'y2'},
            {'label': 'C', 'value': 30, 'color': 'blue', 'name': 'y3'},
        ]
        chart_4 = KitGraph(Graph.Pie, pie_data)
        layout.addWidget(chart_4)

class ScatterGraphDemo(QWidget):
    def __init__(self, parent=None):
        super(ScatterGraphDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        scatter_data = [
            {'x': [1, 2, 3, 4, 5], 'y': [10, 2, 3, 4, 5], 'symbol': {'color': 'red', 'size': 10, 'shape': 't'},
             'name': 'y1'},
            {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 10, 2, 1], 'symbol': {'color': 'green', 'size': 10, 'shape': 't2'},
             'name': 'y2'},
            {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 10, 5], 'symbol': {'color': 'blue', 'size': 10, 'shape': 'o'},
             'name': 'y3'},
        ]
        chart_5 = KitGraph(Graph.Scatter, scatter_data)
        layout.addWidget(chart_5)

if __name__ == "__main__":

    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()


    window = KitFramelessWindow()
    # window =  KitWindow()

    demo = ScatterGraphDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
