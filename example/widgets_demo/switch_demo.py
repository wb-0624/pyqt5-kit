from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout

from widget import KitFramelessWindow, KitSwitch


class SwitchDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        switch = KitSwitch()
        switch.setChecked(True)
        layout.addWidget(switch)
        switch2 = KitSwitch()
        switch2.setChecked(True)
        switch2.setDisabled(True)
        layout.addWidget(switch2)

        switch.checkedChanged.connect(lambda checked: switch2.setDisabled(checked))

        label = QLabel()
        switch.checkedChanged.connect(lambda checked: label.setText(str(checked)))
        layout.addWidget(label)

        layout.addStretch(1)


if __name__ == "__main__":
    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()


    window = KitFramelessWindow()
    # window = KitWindow()

    demo = SwitchDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
