from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class KitHistogramChart(QWidget):

    def __init__(self, parent=None):
        super(KitHistogramChart, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        pass

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)


import pyqtgraph as pg

if __name__ == '__main__':

    # 创建一个应用程序对象
    app = QApplication([])

    # 创建一个 PlotWidget 对象
    pw = pg.PlotWidget()

    # 创建一个 BarGraphItem 对象
    bg = pg.BarGraphItem(x=[1, 2, 3], height=[10, 20, 30], width=0.3)

    # 将 BarGraphItem 添加到 PlotWidget 中
    pw.addItem(bg)

    # 显示 PlotWidget
    pw.show()

    # 运行应用程序
    app.exec_()
