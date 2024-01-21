
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from PyQt5.QtCore import Qt

from app_config.md_icons import Icons
from config import config
from widget import KitButton, KitFramelessWindow
from widget.component.collapse.kit_collapse import KitCollapse


class CollapseDemo(QWidget):
    def __init__(self, parent=None):
        super(CollapseDemo, self).__init__(parent=parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setSpacing(0)

        content = QWidget()
        content.setLayout(QVBoxLayout())
        content.layout().addWidget(QLabel('content'))
        content.layout().addWidget(QLabel('content'))
        content.layout().addWidget(QLabel('content'))
        content.layout().addWidget(KitButton('button'))
        collapse = KitCollapse('321', content)
        collapse.setIcon(Icons.md_account_circle)
        collapse.setTitleAlignment(Qt.AlignHCenter)
        layout.addWidget(collapse)

        layout.addStretch(1)


if __name__ == "__main__":
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = CollapseDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
