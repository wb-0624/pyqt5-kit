import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from app_config import Icons, FluentIcons
from config import config
from widget import KitIcon, KitFramelessWindow, KitMovieIcon, KitFtIcon, KitFtFilledIcon


class IconDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        icon = KitIcon(Icons.md_add, self)
        icon.setProperty('type', 'success')
        layout.addWidget(icon)

        move_icon = KitMovieIcon(parent=self)
        move_icon.move(10,10)
        layout.addWidget(move_icon)

        ft_icon = KitFtIcon(FluentIcons.ft_home, self)
        layout.addWidget(ft_icon)

        ft_fill_icon = KitFtFilledIcon(FluentIcons.ft_home_add_filled, self)
        ft_fill_icon.setProperty('type', 'success')
        layout.addWidget(ft_fill_icon)
        


if __name__ == "__main__":

    # 适应分辨率
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()


    window = KitFramelessWindow()
    # window = KitWindow()

    demo = IconDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
