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
