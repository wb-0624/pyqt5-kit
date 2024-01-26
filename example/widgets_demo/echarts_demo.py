from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from widget import KitEcharts, KitFramelessWindow


class LineEchartsDemo(KitEcharts):

    def __init__(self, parent=None):
        super(LineEchartsDemo, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        option = {
            'xAxis': {
                'type': 'category',
                'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            'yAxis': {
                'type': 'value'
            },
            'series': [
                {
                    'data': [150, 230, 224, 218, 135, 147, 260],
                    'type': 'line'
                }
            ]
        }
        self.loadFinished.connect(lambda: self.setOptions(option))

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)


class TemperatureEchartsDemo(KitEcharts):

    def __init__(self, parent=None):
        super(TemperatureEchartsDemo, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        options = {
            'title': {
                'text': 'Temperature Change in the Coming Week'
            },
            'tooltip': {
                'trigger': 'axis'
            },
            'legend': {},
            'toolbox': {
                'show': True,
                'feature': {
                    'dataZoom': {
                        'yAxisIndex': 'none'
                    },
                    'dataView': {'readOnly': False},
                    'magicType': {'type': ['line', 'bar']},
                    'restore': {},
                    'saveAsImage': {}
                }
            },
            'xAxis': {
                'type': 'category',
                'boundaryGap': False,
                'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            'yAxis': {
                'type': 'value',
                'axisLabel': {
                    'formatter': '{value} °C'
                }
            },
            'series': [
                {
                    'name': 'Highest',
                    'type': 'line',
                    'data': [10, 11, 13, 11, 12, 12, 9],
                    'markPoint': {
                        'data': [
                            {'type': 'max', 'name': 'Max'},
                            {'type': 'min', 'name': 'Min'}
                        ]
                    },
                    'markLine': {
                        'data': [{'type': 'average', 'name': 'Avg'}]
                    }
                },
                {
                    'name': 'Lowest',
                    'type': 'line',
                    'data': [1, -2, 2, 5, 3, 2, 0],
                    'markPoint': {
                        'data': [{'name': '周最低', 'value': -2, 'xAxis': 1, 'yAxis': -1.5}]
                    },
                    'markLine': {
                        'data': [
                            {'type': 'average', 'name': 'Avg'},
                            [
                                {
                                    'symbol': 'none',
                                    'x': '90%',
                                    'Axis': 'max'
                                },
                                {
                                    'symbol': 'circle',
                                    'label': {
                                        'position': 'start',
                                        'formatter': 'Max'
                                    },
                                    'type': 'max',
                                    'name': '最高点'
                                }
                            ]
                        ]
                    }
                }
            ]
        }
        self.loadFinished.connect(lambda: self.setOptions(options))

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)


class BarEchartsDemo(KitEcharts):

    def __init__(self, parent=None):
        super(BarEchartsDemo, self).__init__(parent=parent)

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
    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()
    window = KitFramelessWindow()
    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)
    echarts = LineEchartsDemo()
    layout.addWidget(echarts)
    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
