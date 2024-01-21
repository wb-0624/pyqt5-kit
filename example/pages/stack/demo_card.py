from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QWidget, QApplication, QHBoxLayout, QLabel

from widget import KitCard, KitFramelessWindow, KitTag, KitHDivider, KitButton, KitToolTip, KitToolTipFilter


class DemoCard(KitCard):

    def __init__(self, title: str, file_location: str, class_name: str, parent=None):
        super(DemoCard, self).__init__(parent=parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.title = QLabel(title)

        self.file_location = KitTag(file_location)
        self.file_location.setToolTip('路径基于 example/widgets_demo')
        self.file_location.installEventFilter(KitToolTipFilter(self.file_location))

        self.class_name = KitTag(class_name, 'green')
        self.class_name.setToolTip('这是demo在文件中的类名')
        self.class_name.installEventFilter(KitToolTipFilter(self.class_name))

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.info_widget = QWidget()
        self.info_widget.setObjectName('demo-card-info')
        self.info_layout = QVBoxLayout()
        self.info_widget.setLayout(self.info_layout)
        self.info_layout.addWidget(self.title)
        self.tag_layout = QHBoxLayout()
        self.tag_layout.addWidget(self.file_location)
        self.tag_layout.addWidget(self.class_name)
        self.tag_layout.addStretch(1)
        self.info_layout.addLayout(self.tag_layout)

        self.layout.addWidget(self.info_widget)
        self.layout.addWidget(QWidget(), stretch=1)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setDemoWidget(self, demo_widget: QWidget):
        self.layout.removeWidget(self.layout.itemAt(self.layout.count() - 1).widget())
        self.layout.addWidget(demo_widget, stretch=1)


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
    card = DemoCard('简单的按钮', 'example/widgets_demo/demo.py')
    card.setDemoWidget(KitButton('132'))
    layout.addWidget(card)
    layout.addStretch(1)
    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
