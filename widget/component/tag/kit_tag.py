from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication, QSizePolicy


# `KitTag` 类是 `QLabel` 的子类，它表示具有可自定义文本和背景颜色的彩色标签。
# color: 能被QColor识别的颜色字符串， 边框颜色， 背景颜色是其透明化
class KitTag(QLabel):

    def __init__(self, text=None, color=None, parent=None):
        super(KitTag, self).__init__(text=text, parent=parent)

        self.color = color if color is not None else 'black'
        self.setColor(self.color)

        self.setFixedHeight(20)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setColor(self, color: str):
        if color is None:
            return
        self.color = color
        color = QColor(color)
        red = color.red()
        green = color.green()
        blue = color.blue()
        self.setStyleSheet(
            self.styleSheet() + f"background-color: rgba({red}, {green}, {blue}, 0.3); border: 1px solid rgb({red}, {green}, {blue})")


if __name__ == "__main__":
    from PyQt5.QtGui import QFontDatabase, QColor
    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    tag1 = KitTag("Tag1")
    tag2 = KitTag("Tag223151", "#6e6e6e")
    tag3 = KitTag("Tag3", "#ff11ff")

    layout.addWidget(tag1)
    layout.addWidget(tag2)
    layout.addWidget(tag3)

    main.show()
    sys.exit(app.exec_())
