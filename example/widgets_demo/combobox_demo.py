import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from PyQt5.QtCore import Qt

from config import config
from widget import KitComboBox, KitButton, KitFramelessWindow


class ComboBoxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboBoxDemo, self).__init__(parent=parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        combo = KitComboBox()
        combo.setContentList(
            [{'id': 1, 'name': 'test1213512351'}, {'id': 2, 'name': 'test2'}, {'id': 3, 'name': 'test3'},
             {'id': 4, 'name': 'test4'}, {'id': 5, 'name': 'test5'}])

        btn1 = KitButton("set1")
        btn1.clicked.connect(lambda: combo.setCurrentId(1))
        btn2 = KitButton("set2")
        btn2.clicked.connect(lambda: combo.setCurrentId(2))

        layout.addWidget(combo)
        layout.addWidget(btn1)
        layout.addWidget(btn2)


if __name__ == "__main__":
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
