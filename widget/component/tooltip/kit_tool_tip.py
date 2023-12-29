from PyQt5.QtCore import Qt, QEvent, QPoint, QObject, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from widget import KitFramelessWindow, KitButton


class KitToolTip(KitFramelessWindow):

    def __init__(self, content: str = None):
        super(KitToolTip, self).__init__()
        self.setWindowFlag(Qt.ToolTip)

        self.content = QLabel(content)
        self.content.adjustSize()

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setTitleBar(None)
        self.setStatusBar(None)
        self.hide()

        self.tool_tip_layout = QVBoxLayout()
        self.centralWidget().setLayout(self.tool_tip_layout)

        self.tool_tip_layout.addWidget(self.content, alignment=Qt.AlignCenter)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)


class ToolTipFilter(QObject):
    def __init__(self, parent: QWidget = None):
        super(ToolTipFilter, self).__init__(parent=parent)
        self.tool_tip = KitToolTip(parent.toolTip())
        self.tool_tip.hide()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.ToolTip:
            self.tool_tip.move(event.globalPos() + QPoint(0, 20))
            self.tool_tip.resize(self.tool_tip.content.size())
            self.tool_tip.show()
            return True
        elif event.type() == QEvent.Leave:
            self.tool_tip.hide()
            return True
        return super(ToolTipFilter, self).eventFilter(obj, event)


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

    btn = KitButton('123')
    btn.setToolTip('123')
    btn.installEventFilter(ToolTipFilter(btn))
    layout.addWidget(btn)

    window.setCentralWidget(main)
    window.show()

    sys.exit(app.exec_())
