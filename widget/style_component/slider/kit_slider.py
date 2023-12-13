import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QRectF
from PyQt5.QtGui import QColor, QPainter, QFontDatabase
from PyQt5.QtWidgets import QProxyStyle, QStyle, QWidget, QStyleOptionSlider, QSlider, QApplication, QVBoxLayout

from config import config


class KitSliderStyle(QProxyStyle):
    """ 滑块样式 """

    def __init__(self, config: dict = None):
        super().__init__()

        self.config = {
            "groove.height": 3,
            "sub-page.color": QColor(255, 0, 0),
            "add-page.color": QColor(255, 255, 0, 64),
            "handle.inner-color": QColor(0, 0, 255),
            "handle.ring-color": QColor(255, 255, 255),
            "handle.ring-width": 4,
            "handle.inner-radius": 6,
        }

        config = config if config else {}
        self.config.update(config)

        # 计算 handle 的大小
        w = self.config["handle.ring-width"] + self.config["handle.inner-radius"]

        self.config["handle.size"] = QSize(2*w, 2*w)

    def subControlRect(self, cc: QStyle.ComplexControl, opt: QStyleOptionSlider, sc: QStyle.SubControl, widget: QWidget) -> QtCore.QRect:
        """ 返回子控件所占的矩形区域 """
        if cc != self.CC_Slider or opt.orientation != Qt.Horizontal or sc == self.SC_SliderTickmarks:
            return super().subControlRect(cc, opt, sc, widget)

        rect = opt.rect

        if sc == self.SC_SliderGroove:
            h = self.config["groove.height"]
            grooveRect = QRectF(self.config['handle.size'].width()//2, (rect.height() - h) // 2, rect.width()-self.config['handle.size'].width(), h)
            return grooveRect.toRect()

        if sc == self.SC_SliderHandle:
            size = self.config["handle.size"]
            x = self.sliderPositionFromValue(
                opt.minimum, opt.maximum, opt.sliderPosition, rect.width())
            # 解决滑块跑出滑动条的情况
            x *= (rect.width()-size.width())/rect.width()
            sliderRect = QRectF(x, (rect.height() - self.config['handle.size'].height()) // 2, size.width(), size.height())
            return sliderRect.toRect()

    def drawComplexControl(self, cc: QStyle.ComplexControl, opt: QStyleOptionSlider, painter: QPainter, widget: QWidget = ...):
        """ 绘制子控件 """
        if cc != self.CC_Slider or opt.orientation != Qt.Horizontal:
            return super().drawComplexControl(cc, opt, painter, widget)

        grooveRect = self.subControlRect(cc, opt, self.SC_SliderGroove, widget)
        handleRect = self.subControlRect(cc, opt, self.SC_SliderHandle, widget)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # 绘制滑槽
        painter.save()

        # sub page
        x = grooveRect.topLeft().x()
        w = handleRect.center().x() - handleRect.width()//2
        h = self.config['groove.height']
        y = (widget.rect().height() - h)//2
        painter.setBrush(self.config['sub-page.color'])
        painter.drawRect(x, y, w, h)

        # add page
        x = handleRect.center().x()
        w = grooveRect.width() - x + handleRect.width()//2
        painter.setBrush(self.config['add-page.color'])
        painter.drawRect(x, y, w, h)

        # 绘制滑块
        ringWidth = (self.config['handle.ring-width']+self.config['handle.inner-radius'])*2
        innerWidth = self.config['handle.inner-radius']*2

        x = handleRect.x()
        y = handleRect.y() + (handleRect.height() - ringWidth)//2
        painter.setBrush(self.config['handle.ring-color'])
        painter.drawEllipse(x, y, ringWidth, ringWidth)

        x = handleRect.x() + ringWidth//2 - innerWidth//2
        y = handleRect.y() + (handleRect.height() - innerWidth)//2
        painter.setBrush(self.config['handle.inner-color'])
        painter.drawEllipse(x, y, innerWidth, innerWidth)


class KitSlider(QSlider):
    """
    config = {
            "groove.height": 3,
            "sub-page.color": QColor(255, 0, 0),
            "add-page.color": QColor(255, 255, 255, 64),
            "handle.inner-color": QColor(0, 0, 255),
            "handle.ring-color": QColor(255, 255, 255),
            "handle.ring-width": 4,
            "handle.inner-radius": 6,
            "handle.margin": 0
    }
    """
    def __init__(self, orientation: Qt.Horizontal, parent=None):
        super().__init__(orientation=orientation, parent=parent)
        self.setStyle(KitSliderStyle())

    def sizeHint(self) -> QtCore.QSize:
        return QSize(100, 24)


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 150)
        self.setStyleSheet("Demo{background: rgb(184, 106, 106)}")

        self.slider = KitSlider(Qt.Horizontal)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.slider)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
    window = KitFramelessWindow()
    demo = Demo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())