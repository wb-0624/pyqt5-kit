import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

from config import config
from widget import KitSpinBox, KitDoubleSpinBox, KitFramelessWindow, KitDateSpinBox, KitTimeSpinBox, KitDateTimeSpinBox


class SpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        spin = KitSpinBox()
        spin.setRange(0, 10)
        layout.addWidget(spin)

        spin_step_2 = KitSpinBox()
        spin_step_2.setRange(0, 15)
        spin_step_2.setSingleStep(2)
        layout.addWidget(spin_step_2)


class DoubleSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        double_spin = KitDoubleSpinBox()
        double_spin.setSingleStep(0.5)
        layout.addWidget(double_spin)


class DateSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        date_spin = KitDateSpinBox()
        layout.addWidget(date_spin)


class TimeSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        time_spin = KitTimeSpinBox()
        layout.addWidget(time_spin)


class DateTimeSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        date_time_spin = KitDateTimeSpinBox()
        layout.addWidget(date_time_spin)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = SpinBoxDemo()
    window.setCentralWidget(demo)

    window.show()
    sys.exit(app.exec_())
