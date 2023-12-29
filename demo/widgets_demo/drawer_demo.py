from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from app_config.constant import Position, ClosePolicy
from config import config
from widget import KitDrawer, KitButton, KitFramelessWindow, KitWindow

class DrawerDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        drawer_left = KitDrawer(self.window(), orientation=Position.Left)
        drawer_left.setWidth(600)
        drawer_left.setClosePolicy(ClosePolicy.CloseOnEscape)
        btn = KitButton('left')
        btn.clicked.connect(lambda: drawer_left.open())
        drawer_left.setLayout(QVBoxLayout())
        close_left = KitButton('close')
        close_left.clicked.connect(lambda: drawer_left.close())
        drawer_left.layout().addWidget(close_left)

        drawer_right = KitDrawer(self.window(), orientation=Position.Right)
        btn2 = KitButton('right')
        btn2.clicked.connect(lambda: drawer_right.open())
        drawer_right.setLayout(QVBoxLayout())
        close_right = KitButton('close')
        close_right.clicked.connect(lambda: drawer_right.close())
        drawer_right.layout().addWidget(close_right)

        drawer_top = KitDrawer(self.window(), orientation=Position.Top)
        btn3 = KitButton('top')
        btn3.clicked.connect(lambda: drawer_top.open())
        drawer_top.setLayout(QVBoxLayout())
        close_top = KitButton('close')
        close_top.clicked.connect(lambda: drawer_top.close())
        drawer_top.layout().addWidget(close_top)

        drawer_bottom = KitDrawer(self.window(), orientation=Position.Bottom)
        btn4 = KitButton('bottom')
        btn4.clicked.connect(lambda: drawer_bottom.open())
        drawer_bottom.setLayout(QVBoxLayout())
        close_bottom = KitButton('close')
        close_bottom.clicked.connect(lambda: drawer_bottom.close())
        drawer_bottom.layout().addWidget(close_bottom)

        main_layout.addWidget(btn)
        main_layout.addWidget(btn2)
        main_layout.addWidget(btn3)
        main_layout.addWidget(btn4)



if __name__ == '__main__':
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()




    window = KitFramelessWindow()
    # window = KitWindow()

    demo = DrawerDemo(window)
    window.setCentralWidget(demo)

    window.show()
    sys.exit(app.exec_())
