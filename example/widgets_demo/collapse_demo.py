
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from PyQt5.QtCore import Qt

from app_config.md_icons import Icons
from config import config
from widget import KitButton, KitFramelessWindow
from widget.component.collapse.kit_collapse import KitCollapse


class ComboBoxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboBoxDemo, self).__init__(parent=parent)
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

        content2 = QWidget()
        content2.setLayout(QVBoxLayout())
        content2.layout().addWidget(QLabel('content2'))
        content2.layout().addWidget(QLabel('content2'))
        content2.layout().addWidget(QLabel('content2'))
        content2.layout().addWidget(KitButton('button2'))
        collapse2 = KitCollapse('123', content2)
        collapse2.setIcon(Icons.md_account_circle)
        collapse2.setTitleAlignment(Qt.AlignRight)
        layout.addWidget(collapse2)

        layout.addStretch(1)


if __name__ == "__main__":
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = ComboBoxDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
