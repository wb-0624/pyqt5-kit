from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from widget import KitFramelessWindow, KitSwitch

if __name__ == "__main__":
    from config import config
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)

    QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")

    window = KitFramelessWindow()
    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)
    switch = KitSwitch()
    switch.setChecked(True)
    switch2 = KitSwitch()
    switch2.setChecked(True)
    switch2.setDisabled(True)
    layout.addWidget(switch)
    layout.addWidget(switch2)

    switch.checkedChanged.connect(lambda checked: switch2.setDisabled(checked))

    label = QLabel()
    switch.checkedChanged.connect(lambda checked: label.setText(str(checked)))
    layout.addWidget(label)

    layout.addStretch(1)
    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
